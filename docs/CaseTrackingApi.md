# openapi_client.CaseTrackingApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case_track_by_id**](CaseTrackingApi.md#get_case_track_by_id) | **GET** /caseTrack/{caseId} | Get Case Track for a requested Case Id.
[**get_case_tracks**](CaseTrackingApi.md#get_case_tracks) | **GET** /caseTracks | Get Case Track list.
[**remove_case_track_by_id**](CaseTrackingApi.md#remove_case_track_by_id) | **DELETE** /caseTrack/{caseId} | Remove Case Track for a specific Case Id.
[**track_case**](CaseTrackingApi.md#track_case) | **PUT** /caseTrack | Add Case Track for the requested Case Id.


# **get_case_track_by_id**
> CaseTrack get_case_track_by_id(case_id)

Get Case Track for a requested Case Id.

Retrieve case tracking information for the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_tracking_api
from openapi_client.model.case_track import CaseTrack
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
    api_instance = case_tracking_api.CaseTrackingApi(api_client)
    case_id = "CASEak99a698ea5413" # str | The caseId value for which case tracking information is to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Get Case Track for a requested Case Id.
        api_response = api_instance.get_case_track_by_id(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseTrackingApi->get_case_track_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value for which case tracking information is to be retrieved. |

### Return type

[**CaseTrack**](CaseTrack.md)

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

# **get_case_tracks**
> CaseTrackListResponse get_case_tracks()

Get Case Track list.

Retrieve a list of all tracked cases.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_tracking_api
from openapi_client.model.case_track_list_response import CaseTrackListResponse
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
    api_instance = case_tracking_api.CaseTrackingApi(api_client)
    last_fetch_date = dateutil_parser('2023-03-08T10:17:56+00:00') # datetime | The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.  (optional)
    last_fetch_date_with_updates = dateutil_parser('2023-03-08T10:17:56+00:00') # datetime | The date on which changes were last found in the case information.  (optional)
    page_number = 1 # int | The page number of the results to be retrieved.<br>   - Minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Case Track list.
        api_response = api_instance.get_case_tracks(last_fetch_date=last_fetch_date, last_fetch_date_with_updates=last_fetch_date_with_updates, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseTrackingApi->get_case_tracks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_fetch_date** | **datetime**| The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.  | [optional]
 **last_fetch_date_with_updates** | **datetime**| The date on which changes were last found in the case information.  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional]

### Return type

[**CaseTrackListResponse**](CaseTrackListResponse.md)

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

# **remove_case_track_by_id**
> Success remove_case_track_by_id(case_id)

Remove Case Track for a specific Case Id.

Remove Case Track for a specific Case Id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_tracking_api
from openapi_client.model.exception import Exception
from openapi_client.model.success import Success
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
    api_instance = case_tracking_api.CaseTrackingApi(api_client)
    case_id = "CASEak99a698ea5413" # str | The caseId value for which case tracking information is to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Remove Case Track for a specific Case Id.
        api_response = api_instance.remove_case_track_by_id(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseTrackingApi->remove_case_track_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value for which case tracking information is to be retrieved. |

### Return type

[**Success**](Success.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_case**
> Success track_case()

Add Case Track for the requested Case Id.

Track the specified case.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_tracking_api
from openapi_client.model.case_track_request import CaseTrackRequest
from openapi_client.model.exception import Exception
from openapi_client.model.success import Success
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
    api_instance = case_tracking_api.CaseTrackingApi(api_client)
    case_track_request = CaseTrackRequest(
        case_track_params=CaseUpdateRequest(
            case_id="CASEhq9d8b72d0800c",
            pacer_options=CaseUpdatePacerOptions(
                pacer_user_id="URKYwer3tyh5r56gq2",
                pacer_client_code="Test UniCourt API",
                fetch_participants_if_older_than_days=30,
                refresh_type="fetchNewDocketEntries",
                additional_page_array=[
                    CaseUpdatePacerOptionsAdditionalPageArrayInner(
                        page="caseSummary",
                        fetch_if_older_than_days=30,
                    ),
                ],
            ),
        ),
        schedule=CaseTrackSchedule(
            type="weekly",
            days=[1,3,5],
        ),
    ) # CaseTrackRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Case Track for the requested Case Id.
        api_response = api_instance.track_case(case_track_request=case_track_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseTrackingApi->track_case: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_track_request** | [**CaseTrackRequest**](CaseTrackRequest.md)|  | [optional]

### Return type

[**Success**](Success.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

