from unicourt.api.court_availability_api import CourtAvailabilityApi
from unicourt import utils
class CourtAvailability:

    @staticmethod
    def get_court_coverage(
        court_id,
        **kwargs
    ):

        """Gets Court Coverage of all courts of specific type.  


        Determine whether the specified court is covered by UniCourt.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtAvailabilityApi(api_client).get_court_coverage(
        court_id,
        **kwargs
    )
