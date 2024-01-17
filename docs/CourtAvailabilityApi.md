# openapi_client.CourtAvailabilityApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_court_coverage**](CourtAvailabilityApi.md#get_court_coverage) | **GET** /courtCoverage/{courtId} | Gets Court Coverage of all courts of specific type.


# **get_court_coverage**
> CourtCoverage get_court_coverage(court_id)

Gets Court Coverage of all courts of specific type.

Determine whether the specified court is covered by UniCourt.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_availability_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_coverage import CourtCoverage
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
    api_instance = court_availability_api.CourtAvailabilityApi(api_client)
    court_id = "CORTV4vCEaKrhystBz" # str | The courtId value of the target court.

    # example passing only required values which don't have defaults set
    try:
        # Gets Court Coverage of all courts of specific type.
        api_response = api_instance.get_court_coverage(court_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtAvailabilityApi->get_court_coverage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_id** | **str**| The courtId value of the target court. |

### Return type

[**CourtCoverage**](CourtCoverage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is received. |  -  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

