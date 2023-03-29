from unicourt.sdk.CaseExport import CaseExport


class TestCaseExport:
    def test_export_case():
        return CaseExport.export_case(
            case_id='CASEhq2c3224900a48'
        )

    def test_get_case_export_callback_by_id():
        response, _ = CaseExport.export_case(
            case_id='CASEhq2c3224900a48'
        )

        return CaseExport.get_case_export_callback_by_id(
            case_export_callback_id=response.case_export_callback_id
        )

    def test_get_case_export_callbacks():
        return CaseExport.get_case_export_callbacks(
            date='2023-03-08T10:17:56+00:00', status='IN_PROGRESS'
        )
