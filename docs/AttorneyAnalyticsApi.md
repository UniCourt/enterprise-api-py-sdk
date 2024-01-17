# openapi_client.AttorneyAnalyticsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_norm_attorney_by_id**](AttorneyAnalyticsApi.md#get_norm_attorney_by_id) | **GET** /normAttorney/{normAttorneyId} | Norm Attorney Details.
[**get_norm_judges_associated_with_norm_attorney**](AttorneyAnalyticsApi.md#get_norm_judges_associated_with_norm_attorney) | **GET** /normAttorney/{normAttorneyId}/associatedNormJudges | Judges faced by the Attorney.
[**get_norm_law_firms_associated_with_norm_attorney**](AttorneyAnalyticsApi.md#get_norm_law_firms_associated_with_norm_attorney) | **GET** /normAttorney/{normAttorneyId}/associatedNormLawFirms | Law Firms the attorney has worked for.
[**get_norm_parties_associated_with_norm_attorney**](AttorneyAnalyticsApi.md#get_norm_parties_associated_with_norm_attorney) | **GET** /normAttorney/{normAttorneyId}/associatedNormParties | Parties Represented By the Attorney.
[**search_normalized_attorneys**](AttorneyAnalyticsApi.md#search_normalized_attorneys) | **GET** /normAttorneySearch | Attorney search.
[**search_normalized_attorneys_by_id**](AttorneyAnalyticsApi.md#search_normalized_attorneys_by_id) | **GET** /normAttorneySearch/{normAttorneySearchId} | Norm attorney search results for a given normAttorneySearchId.


# **get_norm_attorney_by_id**
> NormAttorney get_norm_attorney_by_id(norm_attorney_id)

Norm Attorney Details.

This endpoint retrieves information on the attorney in our normalized attorney database which matches the normAttorneyId specified in the request.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_attorney import NormAttorney
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    norm_attorney_id = "NATYs4P6kDBkhKL8CF" # str | Norm ID of Attorney.    - minimum: 18   - maximum: 18 

    # example passing only required values which don't have defaults set
    try:
        # Norm Attorney Details.
        api_response = api_instance.get_norm_attorney_by_id(norm_attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_attorney_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_attorney_id** | **str**| Norm ID of Attorney.    - minimum: 18   - maximum: 18  |

### Return type

[**NormAttorney**](NormAttorney.md)

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

# **get_norm_judges_associated_with_norm_attorney**
> AssociatedNormJudgeResponse get_norm_judges_associated_with_norm_attorney(norm_attorney_id)

Judges faced by the Attorney.

This endpoint returns information on all judges which have appeared in cases with the attorney specified by the normAttorneyId. The returned judges are ordered in descending order of number of cases shared with the relevant attorney. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\"  AND  courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\", \"CORTKQiA4LJuv54tEj\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all judges associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.associated_norm_judge_response import AssociatedNormJudgeResponse
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    norm_attorney_id = "NATYfwmXwRHS279WPY" # str | Norm ID of Attorney.    - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Judges faced by the Attorney.
        api_response = api_instance.get_norm_judges_associated_with_norm_attorney(norm_attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_judges_associated_with_norm_attorney: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Judges faced by the Attorney.
        api_response = api_instance.get_norm_judges_associated_with_norm_attorney(norm_attorney_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_judges_associated_with_norm_attorney: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_attorney_id** | **str**| Norm ID of Attorney.    - minimum: 18   - maximum: 18  |
 **q** | **str**| The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above. | [optional]
 **page_number** | **int**| The page number of the desired page of results. - minimum: 1  | [optional]

### Return type

[**AssociatedNormJudgeResponse**](AssociatedNormJudgeResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_norm_law_firms_associated_with_norm_attorney**
> AssociatedNormLawFirmResponse get_norm_law_firms_associated_with_norm_attorney(norm_attorney_id)

Law Firms the attorney has worked for.

Retrieve law firms with which the specified attorney is known to have been associated. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\"  AND  courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\", \"CORTKQiA4LJuv54tEj\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all LawFirms associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.associated_norm_law_firm_response import AssociatedNormLawFirmResponse
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    norm_attorney_id = "NATYfwmXwRHS279WPY" # str | The normAttorneyId value of the desired attorney.    - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired firms. Keyword expressions should be constructed according to the guidelines shown above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Law Firms the attorney has worked for.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_attorney(norm_attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_law_firms_associated_with_norm_attorney: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Law Firms the attorney has worked for.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_attorney(norm_attorney_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_law_firms_associated_with_norm_attorney: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_attorney_id** | **str**| The normAttorneyId value of the desired attorney.    - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired firms. Keyword expressions should be constructed according to the guidelines shown above. | [optional]
 **page_number** | **int**| The page number of the desired page of results. - minimum: 1  | [optional]

### Return type

[**AssociatedNormLawFirmResponse**](AssociatedNormLawFirmResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_norm_parties_associated_with_norm_attorney**
> AssociatedNormPartyResponse get_norm_parties_associated_with_norm_attorney(norm_attorney_id)

Parties Represented By the Attorney.

Retrieve the parties for which an attorney is known to have represented. <br><br> ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\"  AND  courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\", \"CORTKQiA4LJuv54tEj\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object.. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all parties associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.associated_norm_party_response import AssociatedNormPartyResponse
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    norm_attorney_id = "NATYfwmXwRHS279WPY" # str | The normAttorneyId value of the desired attorney.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired parties. Keyword expressions should be constructed according to the guidelines shown above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Parties Represented By the Attorney.
        api_response = api_instance.get_norm_parties_associated_with_norm_attorney(norm_attorney_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_parties_associated_with_norm_attorney: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Parties Represented By the Attorney.
        api_response = api_instance.get_norm_parties_associated_with_norm_attorney(norm_attorney_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->get_norm_parties_associated_with_norm_attorney: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_attorney_id** | **str**| The normAttorneyId value of the desired attorney.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired parties. Keyword expressions should be constructed according to the guidelines shown above. | [optional]
 **page_number** | **int**| The page number of the desired page of results. - minimum: 1  | [optional]

### Return type

[**AssociatedNormPartyResponse**](AssociatedNormPartyResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_normalized_attorneys**
> NormAttorneySearchResponse search_normalized_attorneys()

Attorney search.

### This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.norm_attorney_search_response import NormAttorneySearchResponse
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    q = "normAttorneyId:"NATYhUvNaef3b2iP8D"" # str | The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.</a>  (optional)
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorney search.
        api_response = api_instance.search_normalized_attorneys(q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->search_normalized_attorneys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormAttorneySearchResponse**](NormAttorneySearchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_normalized_attorneys_by_id**
> NormAttorneySearchResponse search_normalized_attorneys_by_id(norm_attorney_search_id)

Norm attorney search results for a given normAttorneySearchId.

### All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import attorney_analytics_api
from openapi_client.model.norm_attorney_search_response import NormAttorneySearchResponse
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
    api_instance = attorney_analytics_api.AttorneyAnalyticsApi(api_client)
    norm_attorney_search_id = "ASRCJxUHYsgddr4Hc5" # str | Norm Attorney Search information for the given normAttorneySearchId.
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Norm attorney search results for a given normAttorneySearchId.
        api_response = api_instance.search_normalized_attorneys_by_id(norm_attorney_search_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->search_normalized_attorneys_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Norm attorney search results for a given normAttorneySearchId.
        api_response = api_instance.search_normalized_attorneys_by_id(norm_attorney_search_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttorneyAnalyticsApi->search_normalized_attorneys_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_attorney_search_id** | **str**| Norm Attorney Search information for the given normAttorneySearchId. |
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormAttorneySearchResponse**](NormAttorneySearchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Error |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

