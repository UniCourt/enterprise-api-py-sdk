from unicourt.api.case_documents_api import CaseDocumentsApi
from unicourt import utils
class CaseDocuments:

    @staticmethod
    def get_case_document_download_by_id(
        case_document_id,
        **kwargs
    ):

        """Gets downloadable URL for a requested Document ID.  


        Gets downloadable URL for a requested Document ID.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_document_download_by_id(
        case_document_id,
        **kwargs
    )

    @staticmethod
    def get_case_document_order_callback_by_id(
        case_document_order_callback_id,
        **kwargs
    ):

        """Get Case Document Order Callback for a requested Case Document Order Callback Id.  


        Get Case Document Order Callback for a requested Case Document Order Callback Id.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_document_order_callback_by_id(
        case_document_order_callback_id,
        **kwargs
    )

    @staticmethod
    def get_case_document_order_callbacks(
        **kwargs
    ):

        """Get Case Document Order Callback list for a requested Date.  


        Get Case Document Order Callback list for a requested Date.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_document_order_callbacks(
        **kwargs
    )

    @staticmethod
    def get_case_documents(
        case_id,
        **kwargs
    ):

        """Gets Documents for a requested Case ID.  


        Gets Documents for a requested Case ID.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_documents(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_document_by_id(
        case_document_id,
        **kwargs
    ):

        """Gets details for a requested Document ID.  


        Gets details for a requested Document ID.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_document_by_id(
        case_document_id,
        **kwargs
    )

    @staticmethod
    def order_case_document(
        **kwargs
    ):

        """Add Case Document Order for requested Document Ids.  


        Add Case Document Order for requested Document Ids. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).order_case_document(
        **kwargs
    )
