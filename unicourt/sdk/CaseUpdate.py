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


        Request case updates for the specified case. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseUpdateApi(api_client).update_case(
        **kwargs
    )
