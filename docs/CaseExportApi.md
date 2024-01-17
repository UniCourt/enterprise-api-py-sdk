# openapi_client.CaseExportApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_case**](CaseExportApi.md#export_case) | **GET** /caseExport/{caseId} | Gets case exported for a requested Case ID.
[**get_case_export_callback_by_id**](CaseExportApi.md#get_case_export_callback_by_id) | **GET** /caseExport/callbacks/{caseExportCallbackId} | Get Case Export Callback for a requested Case Export Callback Id.
[**get_case_export_callbacks**](CaseExportApi.md#get_case_export_callbacks) | **GET** /caseExport/callbacks | Get Case Export Callback list for a requested Date.


# **export_case**
> CaseExportCallback export_case(case_id)

Gets case exported for a requested Case ID.

Retrieve information about the specified case export.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_export_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_export_callback import CaseExportCallback
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
    api_instance = case_export_api.CaseExportApi(api_client)
    case_id = "CASEhq2c3224900a48" # str | The caseId value of the case for which case export information is to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Gets case exported for a requested Case ID.
        api_response = api_instance.export_case(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseExportApi->export_case: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value of the case for which case export information is to be retrieved. |

### Return type

[**CaseExportCallback**](CaseExportCallback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_export_callback_by_id**
> CaseExportCallback get_case_export_callback_by_id(case_export_callback_id)

Get Case Export Callback for a requested Case Export Callback Id.

Retrieve the specified case export callback object.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_export_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_export_callback import CaseExportCallback
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
    api_instance = case_export_api.CaseExportApi(api_client)
    case_export_callback_id = "CBCEG63f4e233eXqD1" # str | The caseExportCallbackId value of the case export callback object to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Get Case Export Callback for a requested Case Export Callback Id.
        api_response = api_instance.get_case_export_callback_by_id(case_export_callback_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseExportApi->get_case_export_callback_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_export_callback_id** | **str**| The caseExportCallbackId value of the case export callback object to be retrieved. |

### Return type

[**CaseExportCallback**](CaseExportCallback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_export_callbacks**
> CaseExportCallbackListResponse get_case_export_callbacks()

Get Case Export Callback list for a requested Date.

Retrieve callbacks according to the specified criteria.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_export_api
from openapi_client.model.case_export_callback_list_response import CaseExportCallbackListResponse
from openapi_client.model.exception import Exception
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
    api_instance = case_export_api.CaseExportApi(api_client)
    date = dateutil_parser('2023-03-08T10:17:56+00:00') # datetime | The date for which callbacks are to be retrieved. (optional)
    status = "" # str | The status code of the callbacks to be retrieved. (optional)
    page_number = 1 # int | The page number of the callbacks to be retrieved.<br>   - Minimum: 1  (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Case Export Callback list for a requested Date.
        api_response = api_instance.get_case_export_callbacks(date=date, status=status, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseExportApi->get_case_export_callbacks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| The date for which callbacks are to be retrieved. | [optional]
 **status** | **str**| The status code of the callbacks to be retrieved. | [optional]
 **page_number** | **int**| The page number of the callbacks to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional] if omitted the server will use the default value of 1

### Return type

[**CaseExportCallbackListResponse**](CaseExportCallbackListResponse.md)

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

