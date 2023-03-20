from unicourt.api.callback_api import CallbackApi
from unicourt import utils
class Callback:

    @staticmethod
    def get_callbacks(
        **kwargs
    ):

        """Get list of callback types with count for a requested Date.  


        Get list of callback types with count for a requested Date.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CallbackApi(api_client).get_callbacks(
        **kwargs
    )
