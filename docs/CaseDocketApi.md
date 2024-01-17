# openapi_client.CaseDocketApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attorney_associated_parties**](CaseDocketApi.md#get_attorney_associated_parties) | **GET** /attorney/{attorneyId}/associatedParties | Gets Associated Party details for a requested Attorney ID.
[**get_attorney_by_id**](CaseDocketApi.md#get_attorney_by_id) | **GET** /attorney/{attorneyId} | Gets details for a requested Attorney ID.
[**get_case**](CaseDocketApi.md#get_case) | **GET** /case/{caseId} | Gets case information for a requested Case ID.
[**get_case_attorneys**](CaseDocketApi.md#get_case_attorneys) | **GET** /case/{caseId}/attorneys | Gets Attorneys for a requested Case ID.
[**get_case_docket_entries**](CaseDocketApi.md#get_case_docket_entries) | **GET** /case/{caseId}/docketEntries | Gets Docket Entries for a requested Case ID.
[**get_case_hearings**](CaseDocketApi.md#get_case_hearings) | **GET** /case/{caseId}/hearings | Gets Hearings for a requested Case ID.
[**get_case_judges**](CaseDocketApi.md#get_case_judges) | **GET** /case/{caseId}/judges | Gets Judges for a requested Case ID.
[**get_case_parties**](CaseDocketApi.md#get_case_parties) | **GET** /case/{caseId}/parties | Gets Parties for a requested Case ID.
[**get_case_related_cases**](CaseDocketApi.md#get_case_related_cases) | **GET** /case/{caseId}/relatedCases | Gets Related Cases for a requested Case ID.
[**get_judge_by_id**](CaseDocketApi.md#get_judge_by_id) | **GET** /judge/{judgeId} | Gets details for a requested Judge ID.
[**get_party_associated_attorneys**](CaseDocketApi.md#get_party_associated_attorneys) | **GET** /party/{partyId}/associatedAttorneys | Gets Associated Attorney details for a requested Party ID.
[**get_party_by_id**](CaseDocketApi.md#get_party_by_id) | **GET** /party/{partyId} | Gets details for a requested Party ID.
[**get_primary_documents_for_docket_entries**](CaseDocketApi.md#get_primary_documents_for_docket_entries) | **GET** /case/{caseId}/docketEntries/primaryDocuments | Gets Primary Documents of Docket Entries.
[**get_secondary_documents_for_docket_entries**](CaseDocketApi.md#get_secondary_documents_for_docket_entries) | **GET** /case/{caseId}/docketEntries/secondaryDocuments | Gets Secondary Documents of Docket Entries.


# **get_attorney_associated_parties**
> PartyAttorneyAssociations get_attorney_associated_parties(attorney_id)

Gets Associated Party details for a requested Attorney ID.

Retrieve the parties represented by the attorney with the specified attorneyId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.party_attorney_associations import PartyAttorneyAssociations
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    attorney_id = "ATTYgr3ae043d84ebc" # str | Retrieve the parties represented by the attorney with the specified attorneyId value.
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Associated Party details for a requested Attorney ID.
        api_response = api_instance.get_attorney_associated_parties(attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_attorney_associated_parties: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Associated Party details for a requested Attorney ID.
        api_response = api_instance.get_attorney_associated_parties(attorney_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_attorney_associated_parties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_id** | **str**| Retrieve the parties represented by the attorney with the specified attorneyId value. |
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**PartyAttorneyAssociations**](PartyAttorneyAssociations.md)

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

# **get_attorney_by_id**
> Attorney get_attorney_by_id(attorney_id)

Gets details for a requested Attorney ID.

Retrieve the attorney with the specified attorneyId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.attorney import Attorney
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    attorney_id = "ATTYgu01be2e4de654" # str | Retrieve the attorney with the specified attorneyId value.

    # example passing only required values which don't have defaults set
    try:
        # Gets details for a requested Attorney ID.
        api_response = api_instance.get_attorney_by_id(attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_attorney_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_id** | **str**| Retrieve the attorney with the specified attorneyId value. |

### Return type

[**Attorney**](Attorney.md)

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
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case**
> Case get_case(case_id)

Gets case information for a requested Case ID.

Retrieve the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.case import Case
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgr45196c84f3ff" # str | Retrieve the case with the specified caseId value.

    # example passing only required values which don't have defaults set
    try:
        # Gets case information for a requested Case ID.
        api_response = api_instance.get_case(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |

### Return type

[**Case**](Case.md)

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
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_attorneys**
> Attorneys get_case_attorneys(case_id)

Gets Attorneys for a requested Case ID.

Retrieve the attorneys in the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.attorneys import Attorneys
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgq5943bd47a6d2" # str | Retrieve the case with the specified caseId value.
    is_visible = True # bool | Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Attorneys for a requested Case ID.
        api_response = api_instance.get_case_attorneys(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_attorneys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Attorneys for a requested Case ID.
        api_response = api_instance.get_case_attorneys(case_id, is_visible=is_visible, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_attorneys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **is_visible** | **bool**| Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**Attorneys**](Attorneys.md)

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

# **get_case_docket_entries**
> DocketEntries get_case_docket_entries(case_id)

Gets Docket Entries for a requested Case ID.

Retrieve the docket entries in the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.docket_entries import DocketEntries
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgle0bf14b74a96" # str | Retrieve the case with the specified caseId value.
    docket_number = 1 # int | Retrieve the docket entry witih the specified docket number in the case with the specified caseId value. (optional)
    sort_by = "latest to oldest" # str | Sort the retrieved docket entries in ascending order or descending order of date. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Docket Entries for a requested Case ID.
        api_response = api_instance.get_case_docket_entries(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_docket_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Docket Entries for a requested Case ID.
        api_response = api_instance.get_case_docket_entries(case_id, docket_number=docket_number, sort_by=sort_by, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_docket_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **docket_number** | **int**| Retrieve the docket entry witih the specified docket number in the case with the specified caseId value. | [optional]
 **sort_by** | **str**| Sort the retrieved docket entries in ascending order or descending order of date. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**DocketEntries**](DocketEntries.md)

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

# **get_case_hearings**
> Hearings get_case_hearings(case_id)

Gets Hearings for a requested Case ID.

Gets Hearings for a requested Case ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.hearings import Hearings
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEar3c45901ef267" # str | Retrieve the case with the specified caseId value.
    sort_by = "latest to oldest" # str | Specify the sort order of hearings in the case with the specified caseId. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Hearings for a requested Case ID.
        api_response = api_instance.get_case_hearings(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_hearings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Hearings for a requested Case ID.
        api_response = api_instance.get_case_hearings(case_id, sort_by=sort_by, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_hearings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **sort_by** | **str**| Specify the sort order of hearings in the case with the specified caseId. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**Hearings**](Hearings.md)

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

# **get_case_judges**
> Judges get_case_judges(case_id)

Gets Judges for a requested Case ID.

Retrieve the judges involved in the specified case.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.judges import Judges
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgq6e6ea66cd91d" # str | Retrieve the case with the specified caseId value.
    is_visible = True # bool | Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Judges for a requested Case ID.
        api_response = api_instance.get_case_judges(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_judges: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Judges for a requested Case ID.
        api_response = api_instance.get_case_judges(case_id, is_visible=is_visible, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_judges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **is_visible** | **bool**| Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**Judges**](Judges.md)

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

# **get_case_parties**
> Parties get_case_parties(case_id)

Gets Parties for a requested Case ID.

Retrieve the parties involved in the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.parties import Parties
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgq8f4cea2d8e1a" # str | Retrieve the case with the specified caseId value.
    is_visible = True # bool | Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)
    party_role_id = "partyRoleId_example" # str | Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value. (optional)
    party_role_group_id = "partyRoleGroupId_example" # str | Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value. (optional)
    attorney_representation_type_id = "attorneyRepresentationTypeId_example" # str | Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value. (optional)
    party_classification_type = "INDIVIDUAL" # str | Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Parties for a requested Case ID.
        api_response = api_instance.get_case_parties(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_parties: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Parties for a requested Case ID.
        api_response = api_instance.get_case_parties(case_id, is_visible=is_visible, page_number=page_number, party_role_id=party_role_id, party_role_group_id=party_role_group_id, attorney_representation_type_id=attorney_representation_type_id, party_classification_type=party_classification_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_parties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **is_visible** | **bool**| Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]
 **party_role_id** | **str**| Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value. | [optional]
 **party_role_group_id** | **str**| Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value. | [optional]
 **attorney_representation_type_id** | **str**| Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value. | [optional]
 **party_classification_type** | **str**| Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value. | [optional]

### Return type

[**Parties**](Parties.md)

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

# **get_case_related_cases**
> RelatedCases get_case_related_cases(case_id)

Gets Related Cases for a requested Case ID.

Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.related_cases import RelatedCases
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEba328623913f9f" # str | Retrieve the case with the specified caseId value.
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Related Cases for a requested Case ID.
        api_response = api_instance.get_case_related_cases(case_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_related_cases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Related Cases for a requested Case ID.
        api_response = api_instance.get_case_related_cases(case_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_case_related_cases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**RelatedCases**](RelatedCases.md)

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

# **get_judge_by_id**
> Judge get_judge_by_id(judge_id)

Gets details for a requested Judge ID.

Retrieve the judge with the specified judgeId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.judge import Judge
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    judge_id = "JUDGbaf564ec55624a" # str | Retrieve the judge with the specified judgeId value.

    # example passing only required values which don't have defaults set
    try:
        # Gets details for a requested Judge ID.
        api_response = api_instance.get_judge_by_id(judge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_judge_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **judge_id** | **str**| Retrieve the judge with the specified judgeId value. |

### Return type

[**Judge**](Judge.md)

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
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_associated_attorneys**
> PartyAttorneyAssociations get_party_associated_attorneys(party_id)

Gets Associated Attorney details for a requested Party ID.

Retrieve the attorneys in the case with the specified partyId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.party_attorney_associations import PartyAttorneyAssociations
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    party_id = "PRTYgu537f3901f406" # str | Retrieve the party with the specified partyId value.
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Associated Attorney details for a requested Party ID.
        api_response = api_instance.get_party_associated_attorneys(party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_party_associated_attorneys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Associated Attorney details for a requested Party ID.
        api_response = api_instance.get_party_associated_attorneys(party_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_party_associated_attorneys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_id** | **str**| Retrieve the party with the specified partyId value. |
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**PartyAttorneyAssociations**](PartyAttorneyAssociations.md)

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

# **get_party_by_id**
> Party get_party_by_id(party_id)

Gets details for a requested Party ID.

Retrieve the party with the specified partyId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.party import Party
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    party_id = "PRTYgla171a8952aed" # str | Retrieve the party with the specified partyId value.

    # example passing only required values which don't have defaults set
    try:
        # Gets details for a requested Party ID.
        api_response = api_instance.get_party_by_id(party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_party_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_id** | **str**| Retrieve the party with the specified partyId value. |

### Return type

[**Party**](Party.md)

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
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_primary_documents_for_docket_entries**
> DocketEntryPrimaryDocuments get_primary_documents_for_docket_entries(case_id, docket_number)

Gets Primary Documents of Docket Entries.

Retrieve the primary documents in the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.docket_entry_primary_documents import DocketEntryPrimaryDocuments
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgq5da86597e9a4" # str | Retrieve the case with the specified caseId value.
    docket_number = 1 # int | Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.
    in_library = True # bool | Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value. (optional)
    after_first_fetch_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date. (optional)
    library_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Primary Documents of Docket Entries.
        api_response = api_instance.get_primary_documents_for_docket_entries(case_id, docket_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_primary_documents_for_docket_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Primary Documents of Docket Entries.
        api_response = api_instance.get_primary_documents_for_docket_entries(case_id, docket_number, in_library=in_library, after_first_fetch_date=after_first_fetch_date, library_date=library_date, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_primary_documents_for_docket_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **docket_number** | **int**| Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value. |
 **in_library** | **bool**| Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value. | [optional]
 **after_first_fetch_date** | **datetime, none_type**| Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date. | [optional]
 **library_date** | **datetime, none_type**| Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**DocketEntryPrimaryDocuments**](DocketEntryPrimaryDocuments.md)

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

# **get_secondary_documents_for_docket_entries**
> DocketEntrySecondaryDocuments get_secondary_documents_for_docket_entries(case_id, docket_number)

Gets Secondary Documents of Docket Entries.

Retrieve the secondary documents in the case with the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_docket_api
from openapi_client.model.exception import Exception
from openapi_client.model.docket_entry_secondary_documents import DocketEntrySecondaryDocuments
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
    api_instance = case_docket_api.CaseDocketApi(api_client)
    case_id = "CASEgq5da86597e9a4" # str | Retrieve the case with the specified caseId value.
    docket_number = 1 # int | Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.
    in_library = True # bool | Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value. (optional)
    after_first_fetch_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date. (optional)
    library_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date. (optional)
    page_number = 1 # int | Query parameter specifying the page number of the search results to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Secondary Documents of Docket Entries.
        api_response = api_instance.get_secondary_documents_for_docket_entries(case_id, docket_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_secondary_documents_for_docket_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Secondary Documents of Docket Entries.
        api_response = api_instance.get_secondary_documents_for_docket_entries(case_id, docket_number, in_library=in_library, after_first_fetch_date=after_first_fetch_date, library_date=library_date, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseDocketApi->get_secondary_documents_for_docket_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Retrieve the case with the specified caseId value. |
 **docket_number** | **int**| Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value. |
 **in_library** | **bool**| Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value. | [optional]
 **after_first_fetch_date** | **datetime, none_type**| Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date. | [optional]
 **library_date** | **datetime, none_type**| Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date. | [optional]
 **page_number** | **int**| Query parameter specifying the page number of the search results to be retrieved. | [optional]

### Return type

[**DocketEntrySecondaryDocuments**](DocketEntrySecondaryDocuments.md)

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

