import unittest
from unittest.mock import patch

import tracker


class ReportTests(unittest.TestCase):
    def test_organization_matches_domain_boundaries(self):
        for address, expected in [
            ('Author <person@linux.intel.com>', 'Intel'),
            ('person@RAMBUS.COM', 'Rambus'),
            ('person@ti.com', 'Texas Instruments'),
            ('person@seu.edu.cn', '东南大学'),
            ('intel.com@gmail.com', 'Individual Contributor'),
            ('person@notintel.com', '归属待核实（notintel.com）'),
            ('person@unknown.example', '归属待核实（unknown.example）'),
            ('', '归属待核实（无邮箱）'),
        ]:
            with self.subTest(address=address):
                self.assertEqual(tracker.extract_organization(address), expected)

    def make_patch(self, pid, status='已合入'):
        return {
            'id': pid, 'title': 'crypto: test patch', 'date': '2026-07-10',
            'status': status, 'subsystem': 'General Crypto',
            'organization': 'Rambus', 'submitter': 'Author',
            'email': 'author@rambus.com', 'url': 'https://example.org/patch',
            'series_id': 10, 'series_name': 'crypto: test series',
        }

    def test_cover_preserves_all_author_addresses_in_details_only(self):
        first, second = self.make_patch(1), self.make_patch(2)
        second.update(submitter='Another', email='another@ti.com')
        covers, _ = tracker.apply_cover_letters([first, second], [], [first, second])
        for status in ('已合入', '社区讨论中'):
            covers[0]['status'] = status
            report, _ = tracker.generate_report(
                covers, '2026-07-01', '2026-08-31', tracker.MODULES['crypto'])
            details = report.split('## 已合入 Patches', 1)[1]
            self.assertIn('<author@rambus.com>', details)
            self.assertIn('<another@ti.com>', details)
            table = report.split('## 重点 Patch Top20 清单', 1)[1].split('## 已合入 Patches', 1)[0]
            self.assertNotIn('@', table)

    def test_summaries_reject_code_but_keep_readable_technical_names(self):
        for summary in ('调用 aes_zeroize_ctx() 清理密钥。',
                        '修改 drivers/crypto/test.c。',
                        '修改 Kconfig 启用功能。'):
            self.assertIsNone(tracker._valid_table_summary(summary))
        plain = '在 AES 加密结束后清除内存中的密钥，避免已完成请求的密钥残留。'
        self.assertEqual(tracker._valid_table_summary(plain), plain)
        specific = ('修复 Marvell CESA 加密驱动在映射 SRAM 失败时的清理问题：'
                    '现在先判断映射是否成功，失败时不再执行解除映射，避免对无效地址操作。')
        self.assertEqual(tracker._valid_table_summary(specific), specific)
        self.assertTrue(tracker._looks_generic_summary('新增 hardware support for crypto engine。'))
        conditional = ('修复加密请求失败后的状态残留问题：此前失败可能留下无效标记，'
                       '导致后续请求崩溃，现在提前清除标记，避免继续使用旧状态。')
        self.assertEqual(tracker._valid_table_summary(conditional), conditional)
        p = self.make_patch(1)
        p.update(title='crypto: clear the crypto_aes_ctx',
                 table_summary=plain, table_summary_source='llm-mail-batch')
        self.assertEqual(tracker.report_summary(p), plain)

    def test_reasoning_is_never_used_as_final_answer(self):
        self.assertEqual(tracker._extract_text_from_llm_response({
            'choices': [{'message': {'content': '', 'reasoning_content': 'private reasoning'}}]
        }), '')
        self.assertIsNone(tracker._valid_table_summary('"vCPU" ok。'))
        self.assertIsNone(tracker._valid_table_summary(
            '这是技术名词，可以保留，没有函数名，应该符合要求，我们现在写出最终回答。'))

    def test_reads_member_mail_bodies_not_transport_headers(self):
        raw = ('From sender Thu Jan 1 00:00:00 2026\nSubject: cover\n'
               'Received: noisy header\nContent-Type: text/plain; charset=utf-8\n\n'
               'Series rationale.\n---\nfile | 4 ++\n'
               'From sender Thu Jan 1 00:00:00 2026\nSubject: member\n\n'
               'Fix actual failure.\nSigned-off-by: Author <a@example.org>\n'
               'diff --git a/a.c b/a.c\n+ code')
        excerpt = tracker._mail_body_excerpt(raw)
        self.assertIn('Series rationale.', excerpt)
        self.assertIn('Fix actual failure.', excerpt)
        self.assertNotIn('noisy header', excerpt)
        self.assertNotIn('+ code', excerpt)

    def test_batches_all_details_and_reuses_duplicate_results(self):
        items = [self.make_patch(i) for i in range(1, 4)]
        duplicate = dict(items[0])
        summary = '在 AES 加密结束后清除内存中的密钥，避免已完成请求的密钥残留。'
        def evidence(p):
            return p, p['title'], '', 'Actual mail rationale', ''
        def summaries(entries, **kwargs):
            return {entry[0]: summary for entry in entries}
        with patch.object(tracker, 'LLM_API_KEY', 'test'), \
             patch.object(tracker, 'LLM_TABLE_BATCH_SIZE', 8), \
             patch.object(tracker, '_table_evidence_task', side_effect=evidence), \
             patch.object(tracker, '_batch_llm_table_summaries', side_effect=summaries) as batch, \
             patch.object(tracker, '_save_llm_cache'):
            tracker.enrich_top_table_summaries(items + [duplicate], '2026-07-01', '2026-08-31')
        self.assertEqual(batch.call_count, 1)
        self.assertEqual(len(batch.call_args[0][0]), 3)
        for p in items + [duplicate]:
            self.assertEqual(tracker.report_summary(p), summary)

    def test_failed_summaries_are_retried_in_small_batches(self):
        items = [self.make_patch(i) for i in range(1, 7)]
        summary = '设备收到异常请求时先停止当前操作并清理状态，避免后续正常请求沿用错误状态。'
        responses = [
            {},
            {'E01': summary, 'E02': summary, 'E03': summary, 'E04': summary},
            {'E05': summary, 'E06': summary},
        ]
        with patch.object(tracker, 'LLM_API_KEY', 'test'), \
             patch.object(tracker, 'LLM_TABLE_BATCH_SIZE', 8), \
             patch.object(tracker, '_table_evidence_task',
                          side_effect=lambda p: (p, p['title'], '', 'mail', '')), \
             patch.object(tracker, '_batch_llm_table_summaries',
                          side_effect=responses) as batch, \
             patch.object(tracker, '_save_llm_cache'):
            tracker.enrich_top_table_summaries(items, '2026-07-01', '2026-08-31')
        self.assertEqual([len(call[0][0]) for call in batch.call_args_list], [6, 4, 2])
        self.assertTrue(all(p['summary_source'] == 'llm-mail-batch' for p in items))

    def test_retry_receives_the_rejected_summary(self):
        p = self.make_patch(1)
        entries = [('E01', p, p['title'], '', 'mail evidence', '')]
        coded = '修复 AF_ALG 接口在请求失败后未清除合并标记的问题，避免后续调用因残留状态崩溃。'
        plain = '修复内核加密套接字接口在请求失败后未清除合并标记的问题，避免后续调用因残留状态崩溃。'
        with patch.object(tracker, '_SUMMARY_CACHE', {}), \
             patch.object(tracker, '_save_llm_cache'), \
             patch.object(tracker, '_post_llm', side_effect=[
                 tracker.json.dumps({'E01': coded}), tracker.json.dumps({'E01': plain})
             ]) as model:
            self.assertEqual(tracker._batch_llm_table_summaries(entries), {})
            self.assertEqual(p['_summary_feedback'], coded)
            self.assertEqual(tracker._batch_llm_table_summaries(
                entries, cache_tag='test-retry'), {'E01': plain})
            self.assertIn(coded, model.call_args[0][1])


if __name__ == '__main__':
    unittest.main()
