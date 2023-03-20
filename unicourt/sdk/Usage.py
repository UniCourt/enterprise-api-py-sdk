from unicourt.api.usage_api import UsageApi
from unicourt import utils
class Usage:

    @staticmethod
    def get_billing_cycles(
        **kwargs
    ):

        """Get all the previous 12 billing cycles.  


        An endpoint to obtain information on the previous 12 billing cycles.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return UsageApi(api_client).get_billing_cycles(
        **kwargs
    )

    @staticmethod
    def get_billing_usage_by_billing_cycle(
        billing_cycle,
        **kwargs
    ):

        """Specify the billing cycle to know the API usage.  


        An endpoint to obtain information on API usage for a specific billing cycle.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return UsageApi(api_client).get_billing_usage_by_billing_cycle(
        billing_cycle,
        **kwargs
    )

    @staticmethod
    def get_daily_usage_by_date(
        date,
        **kwargs
    ):

        """Get API usage for a requested Date.  


        An endpoint to obtain information on API usage for a specific day.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return UsageApi(api_client).get_daily_usage_by_date(
        date,
        **kwargs
    )
