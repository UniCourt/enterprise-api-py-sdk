# openapi_client.CaseDocumentsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case_document_download_by_id**](CaseDocumentsApi.md#get_case_document_download_by_id) | **GET** /caseDocumentDownload/{caseDocumentId} | Gets downloadable URL for a requested Document ID.
[**get_case_document_order_callback_by_id**](CaseDocumentsApi.md#get_case_document_order_callback_by_id) | **GET** /caseDocumentOrder/callbacks/{caseDocumentOrderCallbackId} | Get Case Document Order Callback for a requested Case Document Order Callback Id.
[**get_case_document_order_callbacks**](CaseDocumentsApi.md#get_case_document_order_callbacks) | **GET** /caseDocumentOrder/callbacks | Get Case Document Order Callback list for a requested Date.
[**get_case_documents**](CaseDocumentsApi.md#get_case_documents) | **GET** /case/{caseId}/documents | Gets Documents for a requested Case ID.
[**get_document_by_id**](CaseDocumentsApi.md#get_document_by_id) | **GET** /caseDocument/{caseDocumentId} | Gets details for a requested Document ID.
[**order_case_document**](CaseDocumentsApi.md#order_case_document) | **PUT** /caseDocumentOrder | Add Case Document Order for requested Document Ids.


# **get_case_document_download_by_id**
> DocumentDownload get_case_document_download_by_id(case_document_id)

Gets downloadable URL for a requested Document ID.

Gets downloadable URL for a requested Document ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.exception import Exception
from openapi_client.model.document_download import DocumentDownload
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    case_document_id = "CDOCaqe42a86394f63" # str | Document ID which you want to download.
    is_preview_document = True # bool | If the document you want to download is a preview of a document. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Gets downloadable URL for a requested Document ID.
        api_response = api_instance.get_case_document_download_by_id(case_document_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_document_download_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets downloadable URL for a requested Document ID.
        api_response = api_instance.get_case_document_download_by_id(case_document_id, is_preview_document=is_preview_document)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_document_download_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_document_id** | **str**| Document ID which you want to download. |
 **is_preview_document** | **bool**| If the document you want to download is a preview of a document. | [optional] if omitted the server will use the default value of False

### Return type

[**DocumentDownload**](DocumentDownload.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_document_order_callback_by_id**
> CaseDocumentOrderCallback get_case_document_order_callback_by_id(case_document_order_callback_id)

Get Case Document Order Callback for a requested Case Document Order Callback Id.

Get Case Document Order Callback for a requested Case Document Order Callback Id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_document_order_callback import CaseDocumentOrderCallback
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    case_document_order_callback_id = "CBDOp2o7L63f47ce15" # str | Unique Id for the Case Document Order Callback.

    # example passing only required values which don't have defaults set
    try:
        # Get Case Document Order Callback for a requested Case Document Order Callback Id.
        api_response = api_instance.get_case_document_order_callback_by_id(case_document_order_callback_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_document_order_callback_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_document_order_callback_id** | **str**| Unique Id for the Case Document Order Callback. |

### Return type

[**CaseDocumentOrderCallback**](CaseDocumentOrderCallback.md)

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

# **get_case_document_order_callbacks**
> CaseDocumentOrderCallbackListResponse get_case_document_order_callbacks()

Get Case Document Order Callback list for a requested Date.

Get Case Document Order Callback list for a requested Date.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    date = dateutil_parser('2023-03-08T10:17:56+00:00') # datetime | Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date. (optional)
    status = "" # str | Status of Document Order callbacks. Default status will fetch all callbacks. (optional)
    page_number = 1 # int | Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1  (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Case Document Order Callback list for a requested Date.
        api_response = api_instance.get_case_document_order_callbacks(date=date, status=status, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_document_order_callbacks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date. | [optional]
 **status** | **str**| Status of Document Order callbacks. Default status will fetch all callbacks. | [optional]
 **page_number** | **int**| Page to fetch the Case Document Order Callback list.&lt;br&gt;   - Minimum: 1  | [optional] if omitted the server will use the default value of 1

### Return type

[**CaseDocumentOrderCallbackListResponse**](CaseDocumentOrderCallbackListResponse.md)

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

# **get_case_documents**
> CaseDocuments get_case_documents(case_id)

Gets Documents for a requested Case ID.

Gets Documents for a requested Case ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_documents import CaseDocuments
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    case_id = "CASEgua4c06e119ea8" # str | Case ID for which you want the data for.
    in_library = True # bool | Filter all the documents those are added to the UniCourt library. (optional)
    after_first_fetch_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Get all the documents which were added to the case on or after a specific date. (optional)
    library_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Sort all the documents based on the date when the document was added to the UniCourt Library. (optional)
    first_fetch_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Sort all the documents based on the date it was fetched from the source site. (optional)
    sort_by = "latest to oldest" # str | Sort documents with document order. (optional)
    page_number = 1 # int | The page for which the result should be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Documents for a requested Case ID.
        api_response = api_instance.get_case_documents(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Documents for a requested Case ID.
        api_response = api_instance.get_case_documents(case_id, in_library=in_library, after_first_fetch_date=after_first_fetch_date, library_date=library_date, first_fetch_date=first_fetch_date, sort_by=sort_by, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_case_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case ID for which you want the data for. |
 **in_library** | **bool**| Filter all the documents those are added to the UniCourt library. | [optional]
 **after_first_fetch_date** | **datetime, none_type**| Get all the documents which were added to the case on or after a specific date. | [optional]
 **library_date** | **datetime, none_type**| Sort all the documents based on the date when the document was added to the UniCourt Library. | [optional]
 **first_fetch_date** | **datetime, none_type**| Sort all the documents based on the date it was fetched from the source site. | [optional]
 **sort_by** | **str**| Sort documents with document order. | [optional]
 **page_number** | **int**| The page for which the result should be retrieved. | [optional]

### Return type

[**CaseDocuments**](CaseDocuments.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**404** | Resource Not Found |  -  |
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_by_id**
> CaseDocument get_document_by_id(case_document_id)

Gets details for a requested Document ID.

Gets details for a requested Document ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.case_document import CaseDocument
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    case_document_id = "CDOCag3e5eba43b870" # str | Specific Case Dcoument ID for which you want the data for.

    # example passing only required values which don't have defaults set
    try:
        # Gets details for a requested Document ID.
        api_response = api_instance.get_document_by_id(case_document_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->get_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_document_id** | **str**| Specific Case Dcoument ID for which you want the data for. |

### Return type

[**CaseDocument**](CaseDocument.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_case_document**
> CaseDocumentOrderCallback order_case_document()

Add Case Document Order for requested Document Ids.

Add Case Document Order for requested Document Ids. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_documents_api
from openapi_client.model.case_document_order_request import CaseDocumentOrderRequest
from openapi_client.model.exception import Exception
from openapi_client.model.case_document_order_callback import CaseDocumentOrderCallback
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
    api_instance = case_documents_api.CaseDocumentsApi(api_client)
    case_document_order_request = CaseDocumentOrderRequest(
        case_document_id="CDOCcre989d654fa05",
        is_preview_only=True,
        pacer_options=CaseDocumentOrderPacerOptions(
            pacer_user_id="URKYwer3tyh5r56gq2",
            pacer_client_code="Test UniCourt API",
        ),
    ) # CaseDocumentOrderRequest | If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Case Document Order for requested Document Ids.
        api_response = api_instance.order_case_document(case_document_order_request=case_document_order_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocumentsApi->order_case_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_document_order_request** | [**CaseDocumentOrderRequest**](CaseDocumentOrderRequest.md)| If the Case Document Order is for Preview, then the value for &#x60;&#x60;isPreviewOnly&#x60;&#x60; should be &#x60;&#x60;true&#x60;&#x60; else &#x60;&#x60;false&#x60;&#x60;.  | [optional]

### Return type

[**CaseDocumentOrderCallback**](CaseDocumentOrderCallback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**402** | Payment Required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

