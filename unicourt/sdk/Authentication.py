from unicourt.api.authentication_api import AuthenticationApi
from unicourt import utils
class Authentication:

    @staticmethod
    def generate_new_token(
        **kwargs
    ):

        """Generate new token to access API.  


        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).generate_new_token(
        **kwargs
    )

    @staticmethod
    def invalidate_all_tokens(
        **kwargs
    ):

        """API to invalidate all access tokens.  


        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).invalidate_all_tokens(
        **kwargs
    )

    @staticmethod
    def invalidate_token(
        **kwargs
    ):

        """API to invalidate the access token.  


        An endpoint which allows you to invalidate a given access token.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).invalidate_token(
        **kwargs
    )

    @staticmethod
    def list_all_token_ids(
        **kwargs
    ):

        """API to list all the access tokens Id.  


        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).list_all_token_ids(
        **kwargs
    )
