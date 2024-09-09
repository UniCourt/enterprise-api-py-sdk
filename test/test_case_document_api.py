from unicourt.model.case_document_order_request import CaseDocumentOrderRequest
from unicourt.sdk.CaseDocuments import CaseDocuments


class TestCaseDocuments:
    def test_get_case_document_download_by_id_with_no_preview():
        return CaseDocuments.get_case_document_download_by_id(
            case_document_id='CDOCaqe42a86394f63',
            is_preview_document=False
        )

    def test_get_case_document_download_by_id_with_preview():
        return CaseDocuments.get_case_document_download_by_id(
            # id with document preview is present
            case_document_id='CDOCagf8a7c8bac76a',
            is_preview_document=True
        )

    def test_get_case_document_order_callback_by_id():
        case_document_order_request = CaseDocumentOrderRequest(
            case_document_id="CDOCcre989d654fa05",
            is_preview_only=True
        )
        response, _ = CaseDocuments.order_case_document(
            case_document_order_request=case_document_order_request
        )
        cbk_id = response.case_document_order_callback_id
        return CaseDocuments.get_case_document_order_callback_by_id(
            case_document_order_callback_id=cbk_id
        )

    def test_get_case_document_order_callbacks():
        return CaseDocuments.get_case_document_order_callbacks(
            date='2022-03-08T10:17:56+00:00', status='FAILURE', page_number=1
        )

    def test_get_case_documents():
        return CaseDocuments.get_case_documents(
            case_id='CASEgua4c06e119ea8'
        )

    def test_get_document_by_id():
        return CaseDocuments.get_document_by_id(
            case_document_id='CDOCaqe42a86394f63'
        )

    def test_order_case_document():
        case_document_order_request = CaseDocumentOrderRequest(
            case_document_id="CDOCcre989d654fa05",
            is_preview_only=True
        )
        return CaseDocuments.order_case_document(
            case_document_order_request=case_document_order_request
        )
