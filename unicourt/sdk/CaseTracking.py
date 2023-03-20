from unicourt.api.case_tracking_api import CaseTrackingApi
from unicourt import utils
class CaseTracking:

    @staticmethod
    def get_case_track_by_id(
        case_id,
        **kwargs
    ):

        """Get Case Track for a requested Case Id.  


        Retrieve case tracking information for the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseTrackingApi(api_client).get_case_track_by_id(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_tracks(
        **kwargs
    ):

        """Get Case Track list.  


        Retrieve a list of all tracked cases.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseTrackingApi(api_client).get_case_tracks(
        **kwargs
    )

    @staticmethod
    def remove_case_track_by_id(
        case_id,
        **kwargs
    ):

        """Remove Case Track for a specific Case Id.  


        Remove Case Track for a specific Case Id.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseTrackingApi(api_client).remove_case_track_by_id(
        case_id,
        **kwargs
    )

    @staticmethod
    def track_case(
        **kwargs
    ):

        """Add Case Track for the requested Case Id.  


        Track the specified case.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseTrackingApi(api_client).track_case(
        **kwargs
    )
