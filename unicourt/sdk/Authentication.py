import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import Field
from typing import Optional
from typing_extensions import Annotated

import unicourt
from unicourt.model.access_token_id_list_response import AccessTokenIdListResponse
from unicourt.model.access_token_request import AccessTokenRequest
from unicourt.model.access_token_response import AccessTokenResponse
from unicourt.model.invalidate_access_token_request import InvalidateAccessTokenRequest
from unicourt.model.success import Success
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.authentication_api import AuthenticationApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils

class Authentication:

    def update_api_client_after_login():
        """
        This method is used to update the api_client object after 
        the generate_new_token is called so that we can use the same 
        api client for rest of the api calls.
        """
        unicourt.configuration = unicourt.Configuration(
            access_token=unicourt.ACCESS_TOKEN)
        unicourt.api_client = unicourt.ApiClient(unicourt.configuration)

    @staticmethod
    def generate_new_token(
        client_id: Annotated[str, Field(description="Your Client ID obtainable by logging into your UniCourt account.")] = None,
        client_secret: Annotated[str, Field(description="Your Client Secret ID obtainable by logging into your UniCourt account.")]= None
    ) -> SdkResponse[AccessTokenResponse]:

        """Generate new token to access API.

        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

        :param client_id: Your Client ID obtainable by logging into your UniCourt account.
        :type client_id: str
        :param client_secret: Your Client Secret ID obtainable by logging into your UniCourt account.
        :type client_secret: str
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            unicourt.CLIENT_ID = client_id or unicourt.CLIENT_ID
            unicourt.CLIENT_SECRET = client_secret or unicourt.CLIENT_SECRET
            payload = AccessTokenRequest(
                client_id=unicourt.CLIENT_ID,
                client_secret=unicourt.CLIENT_SECRET,
            )
            response = AuthenticationApi(api_client).generate_new_token_with_http_info(
                access_token_request=payload)
            unicourt.ACCESS_TOKEN = response.data.access_token
            unicourt.TOKEN_ID = response.data.token_id
            Authentication.update_api_client_after_login()
            return (response.data, response.status_code)

    @staticmethod
    def invalidate_all_tokens(
        client_id: Annotated[str, Field(description="Your Client ID obtainable by logging into your UniCourt account.")] = None,
        client_secret: Annotated[str, Field(description="Your Client Secret ID obtainable by logging into your UniCourt account.")]= None
    ) -> SdkResponse[Success]:

        """API to invalidate all access tokens.

        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

        :param client_id: Your Client ID obtainable by logging into your UniCourt account.
        :type client_id: str
        :param client_secret: Your Client Secret ID obtainable by logging into your UniCourt account.
        :type client_secret: str
        :return: Returns the result object.
        """
        access_token_request = AccessTokenRequest(
            client_id=client_id or unicourt.CLIENT_ID,
            client_secret=client_secret or unicourt.CLIENT_SECRET,
        )

        with utils.api_client() as api_client:
            response = AuthenticationApi(api_client).invalidate_all_tokens_with_http_info(access_token_request = access_token_request)
            return (response.data, response.status_code)

    @staticmethod
    def invalidate_token(
        client_id: Annotated[str, Field(description="Your Client ID obtainable by logging into your UniCourt account.")] = None,
        client_secret: Annotated[str, Field(description="Your Client Secret ID obtainable by logging into your UniCourt account.")]= None,
        token_id: Annotated[str, Field(description="The Token ID of token being invalidated.")]= None
    ) -> SdkResponse[Success]:

        """API to invalidate the access token.

        An endpoint which allows you to invalidate a given access token.

        :param client_id: Your Client ID obtainable by logging into your UniCourt account.
        :type client_id: str
        :param client_secret: Your Client Secret ID obtainable by logging into your UniCourt account.
        :type client_secret: str
        :param token_id: The Token ID of token being invalidated.
        :type token_id: str
        :return: Returns the result object.
        """
        invalidate_access_token_request = InvalidateAccessTokenRequest(
            client_id=client_id or unicourt.CLIENT_ID,
            client_secret=client_secret or unicourt.CLIENT_SECRET,
            token_id=token_id or unicourt.TOKEN_ID
        )
        with utils.api_client() as api_client:
            response = AuthenticationApi(api_client).invalidate_token_with_http_info(invalidate_access_token_request = invalidate_access_token_request)
            return (response.data, response.status_code)

    @staticmethod
    def list_all_token_ids(
        client_id: Annotated[str, Field(description="Your Client ID obtainable by logging into your UniCourt account.")] = None,
        client_secret: Annotated[str, Field(description="Your Client Secret ID obtainable by logging into your UniCourt account.")]= None
    ) -> SdkResponse[AccessTokenIdListResponse]:

        """API to list all the access tokens Id.

        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

        :param client_id: Your Client ID obtainable by logging into your UniCourt account.
        :type client_id: str
        :param client_secret: Your Client Secret ID obtainable by logging into your UniCourt account.
        :type client_secret: str
        :return: Returns the result object.
        """
        access_token_request = AccessTokenRequest(
            client_id=client_id or unicourt.CLIENT_ID,
            client_secret=client_secret or unicourt.CLIENT_SECRET,
        )

        with utils.api_client() as api_client:
            response = AuthenticationApi(api_client).list_all_token_ids_with_http_info(access_token_request = access_token_request)
            return (response.data, response.status_code)
