import unicourt
from unicourt.api.authentication_api import AuthenticationApi
from unicourt.model.access_token_request import AccessTokenRequest
from unicourt.model.invalidate_access_token_request import InvalidateAccessTokenRequest
from unicourt import utils


class Authentication(object):

    def update_api_client_after_login():
        """
        This method is used to update the api_client object after 
        the generate_new_token is called so that we can use the same 
        api client for rest of the api calls.
        """
        unicourt.configuration = unicourt.Configuration(
            access_token=unicourt.ACCESS_TOKEN)
        unicourt.api_client = unicourt.ApiClient(unicourt.configuration)

    def generate_new_token(client_id=None, client_secret=None):
        """Generate new token to access API. 
        Generate new access token, UniCourt provides clientId and client Secret. 
        Each time you will get new Access token. At a time you can have max 10 access tokens. 
        There will not be any expiry for access token. If you request for more than 10 tokens you will get error message.
        """
        with utils.api_client() as api_client:
            unicourt.CLIENT_ID = client_id or unicourt.CLIENT_ID
            unicourt.CLIENT_SECRET = client_secret or unicourt.CLIENT_SECRET
            payload = AccessTokenRequest(
                client_id=unicourt.CLIENT_ID,
                client_secret=unicourt.CLIENT_SECRET,
            )
            response, status = AuthenticationApi(api_client).generate_new_token(
                access_token_request=payload)
            unicourt.ACCESS_TOKEN = response.access_token
            unicourt.TOKEN_ID = response.token_id
            Authentication.update_api_client_after_login()
        return response, status

    def invalidate_token(client_id=None, client_secret=None, token_id=None):
        """API to invalidate all access tokens.  
        Logout API to invalidate all access tokens.
        """
        invalidate_access_token_request = InvalidateAccessTokenRequest(
            client_id=client_id or unicourt.CLIENT_ID,
            client_secret=client_secret or unicourt.CLIENT_SECRET,
            token_id=token_id or unicourt.TOKEN_ID
        )
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).invalidate_token(
                invalidate_access_token_request=invalidate_access_token_request)

    def invalidate_all_tokens(client_id=None, client_secret=None):
        """API to invalidate the access token.  # noqa: E501
        API to invalidate the access token
        """
        access_token_request = AccessTokenRequest(
            client_id=unicourt.CLIENT_ID,
            client_secret=unicourt.CLIENT_SECRET,
        )
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).invalidate_all_tokens(
                access_token_request=access_token_request)

    def list_all_token_ids(client_id=None, client_secret=None):
        """API to list all the access tokens Id. 
        API to list all the access tokens Id.
        """
        access_token_request = AccessTokenRequest(
            client_id=unicourt.CLIENT_ID,
            client_secret=unicourt.CLIENT_SECRET,
        )
        with utils.api_client() as api_client:
            return AuthenticationApi(api_client).list_all_token_ids(
                access_token_request=access_token_request)
