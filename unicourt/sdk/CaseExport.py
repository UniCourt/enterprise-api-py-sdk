from unicourt.api.case_export_api import CaseExportApi
from unicourt import utils
class CaseExport:

    @staticmethod
    def export_case(
        case_id,
        **kwargs
    ):

        """Gets case exported for a requested Case ID.  


        Retrieve information about the specified case export.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).export_case(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_export_callback_by_id(
        case_export_callback_id,
        **kwargs
    ):

        """Get Case Export Callback for a requested Case Export Callback Id.  


        Retrieve the specified case export callback object.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).get_case_export_callback_by_id(
        case_export_callback_id,
        **kwargs
    )

    @staticmethod
    def get_case_export_callbacks(
        **kwargs
    ):

        """Get Case Export Callback list for a requested Date.  


        Retrieve callbacks according to the specified criteria.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).get_case_export_callbacks(
        **kwargs
    )
