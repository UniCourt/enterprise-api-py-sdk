from unicourt.api.case_update_api import CaseUpdateApi
from unicourt import utils
class CaseUpdate:

    @staticmethod
    def get_case_update_by_case_id(
        case_id,
        **kwargs
    ):

        """Get Case Updates for a requested CaseId.  


        Retrieve case updates for the specified case object.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseUpdateApi(api_client).get_case_update_by_case_id(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_updates(
        **kwargs
    ):

        """Get Case Update  list for a requested Date.  


        Retrieve case updates for the specified date.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseUpdateApi(api_client).get_case_updates(
        **kwargs
    )

    @staticmethod
    def update_case(
        **kwargs
    ):

        """Add Case Update for the requested Case Id.  


        Request case updates for the specified case.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseUpdateApi(api_client).update_case(
        **kwargs
    )
