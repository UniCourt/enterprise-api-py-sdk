# openapi_client.CallbackApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_callbacks**](CallbackApi.md#get_callbacks) | **GET** /callbacks | Get list of callback types with count for a requested Date.


# **get_callbacks**
> CallbackListResponse get_callbacks()

Get list of callback types with count for a requested Date.

Get list of callback types with count for a requested Date.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import callback_api
from openapi_client.model.exception import Exception
from openapi_client.model.callback_list_response import CallbackListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = callback_api.CallbackApi(api_client)
    date = dateutil_parser('2023-03-08T00:00:00+00:00') # datetime | Date for which fetch the callback type list. By default, the date will be set to current date. (optional)
    status = "IN_PROGRESS" # str | Status of the callbacks. Default status will fetch all callbacks. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of callback types with count for a requested Date.
        api_response = api_instance.get_callbacks(date=date, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CallbackApi->get_callbacks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| Date for which fetch the callback type list. By default, the date will be set to current date. | [optional]
 **status** | **str**| Status of the callbacks. Default status will fetch all callbacks. | [optional]

### Return type

[**CallbackListResponse**](CallbackListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

