# openapi_client.AuthenticationApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_new_token**](AuthenticationApi.md#generate_new_token) | **POST** /generateNewToken | Generate new token to access API.
[**invalidate_all_tokens**](AuthenticationApi.md#invalidate_all_tokens) | **PUT** /invalidateAllTokens | API to invalidate all access tokens.
[**invalidate_token**](AuthenticationApi.md#invalidate_token) | **PUT** /invalidateToken | API to invalidate the access token.
[**list_all_token_ids**](AuthenticationApi.md#list_all_token_ids) | **PUT** /listAllTokenIds | API to list all the access tokens Id.


# **generate_new_token**
> AccessTokenResponse generate_new_token()

Generate new token to access API.

This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token_request import AccessTokenRequest
from openapi_client.model.exception import Exception
from openapi_client.model.access_token_response import AccessTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    access_token_request = AccessTokenRequest(
        client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
        client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
    ) # AccessTokenRequest | The endpoint accepts your Client ID and Client Secret ID as part of the request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate new token to access API.
        api_response = api_instance.generate_new_token(access_token_request=access_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->generate_new_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)| The endpoint accepts your Client ID and Client Secret ID as part of the request. | [optional]

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_all_tokens**
> Success invalidate_all_tokens()

API to invalidate all access tokens.

An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token_request import AccessTokenRequest
from openapi_client.model.exception import Exception
from openapi_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    access_token_request = AccessTokenRequest(
        client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
        client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
    ) # AccessTokenRequest | The endpoint accepts your Client ID and Secret Client ID as part of the request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to invalidate all access tokens.
        api_response = api_instance.invalidate_all_tokens(access_token_request=access_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->invalidate_all_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)| The endpoint accepts your Client ID and Secret Client ID as part of the request. | [optional]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_token**
> Success invalidate_token()

API to invalidate the access token.

An endpoint which allows you to invalidate a given access token.

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.exception import Exception
from openapi_client.model.invalidate_access_token_request import InvalidateAccessTokenRequest
from openapi_client.model.success import Success
from pprint import pprint
# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    invalidate_access_token_request = InvalidateAccessTokenRequest(
        client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
        client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
        token_id="TKID384a057WFC3Dp3",
    ) # InvalidateAccessTokenRequest | The endpoint accepts your Client ID, Client Secret ID and the Token ID for the access token you wish to invalidate as part of the request. You can obtain a list of all Token IDs from the /listAllTokenIds endpoint within this API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to invalidate the access token.
        api_response = api_instance.invalidate_token(invalidate_access_token_request=invalidate_access_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->invalidate_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_access_token_request** | [**InvalidateAccessTokenRequest**](InvalidateAccessTokenRequest.md)| The endpoint accepts your Client ID, Client Secret ID and the Token ID for the access token you wish to invalidate as part of the request. You can obtain a list of all Token IDs from the /listAllTokenIds endpoint within this API. | [optional]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_token_ids**
> AccessTokenIdListResponse list_all_token_ids()

API to list all the access tokens Id.

An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from openapi_client.model.access_token_request import AccessTokenRequest
from openapi_client.model.access_token_id_list_response import AccessTokenIdListResponse
from openapi_client.model.exception import Exception
from pprint import pprint
# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    access_token_request = AccessTokenRequest(
        client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
        client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
    ) # AccessTokenRequest | The endpoint accepts your Client ID and Client Secret ID as part of the request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to list all the access tokens Id.
        api_response = api_instance.list_all_token_ids(access_token_request=access_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->list_all_token_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)| The endpoint accepts your Client ID and Client Secret ID as part of the request. | [optional]

### Return type

[**AccessTokenIdListResponse**](AccessTokenIdListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

