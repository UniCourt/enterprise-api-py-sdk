# openapi_client.JudgeAnalyticsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_norm_attorneys_associated_with_norm_judge**](JudgeAnalyticsApi.md#get_norm_attorneys_associated_with_norm_judge) | **GET** /normJudge/{normJudgeId}/associatedNormAttorneys | Attorneys Associated with the Judge.
[**get_norm_judge_by_id**](JudgeAnalyticsApi.md#get_norm_judge_by_id) | **GET** /normJudge/{normJudgeId} | Norm Judge Details.
[**get_norm_law_firms_associated_with_norm_judge**](JudgeAnalyticsApi.md#get_norm_law_firms_associated_with_norm_judge) | **GET** /normJudge/{normJudgeId}/associatedNormLawFirms | Law Firms Associated With the Judge.
[**get_norm_parties_associated_with_norm_judge**](JudgeAnalyticsApi.md#get_norm_parties_associated_with_norm_judge) | **GET** /normJudge/{normJudgeId}/associatedNormParties | Parties Associated with the Judge.
[**search_normalized_judges**](JudgeAnalyticsApi.md#search_normalized_judges) | **GET** /normJudgeSearch | Judge search.
[**search_normalized_judges_by_id**](JudgeAnalyticsApi.md#search_normalized_judges_by_id) | **GET** /normJudgeSearch/{normJudgeSearchId} | Norm judge search results for a given normJudgeSearchId.


# **get_norm_attorneys_associated_with_norm_judge**
> AssociatedNormAttorneyResponse get_norm_attorneys_associated_with_norm_judge(norm_judge_id)

Attorneys Associated with the Judge.

Search for attorneys who have appeared before the specified judge using a keyword expression. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN (\"COLODj4BBVTho3pKpz\",\"COLOPUfJRhw5yPxgRi\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all attorneys associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPGkaW3aGJyKGyfn and case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
from openapi_client.model.associated_norm_attorney_response import AssociatedNormAttorneyResponse
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    norm_judge_id = "NJUDT7jCZyFNeLGpRq" # str | The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired attorneys. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attorneys Associated with the Judge.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_judge(norm_judge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_attorneys_associated_with_norm_judge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorneys Associated with the Judge.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_judge(norm_judge_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_attorneys_associated_with_norm_judge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_judge_id** | **str**| The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired attorneys. | [optional]
 **page_number** | **int**| The page number of the desired page of results. - minimum: 1  | [optional]

### Return type

[**AssociatedNormAttorneyResponse**](AssociatedNormAttorneyResponse.md)

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

# **get_norm_judge_by_id**
> NormJudge get_norm_judge_by_id(norm_judge_id)

Norm Judge Details.

Retrieve the specified judge. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
from openapi_client.model.norm_judge import NormJudge
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    norm_judge_id = "NJUDT7jCZyFNeLGpRq" # str | The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18 

    # example passing only required values which don't have defaults set
    try:
        # Norm Judge Details.
        api_response = api_instance.get_norm_judge_by_id(norm_judge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_judge_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_judge_id** | **str**| The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18  |

### Return type

[**NormJudge**](NormJudge.md)

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

# **get_norm_law_firms_associated_with_norm_judge**
> AssociatedNormLawFirmResponse get_norm_law_firms_associated_with_norm_judge(norm_judge_id)

Law Firms Associated With the Judge.

Search for law firms that have appeared before the specified judge using a keyword expression. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLOPUfJRhw5yPxgRi\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN (\"COLODj4BBVTho3pKpz\",\"COLOPUfJRhw5yPxgRi\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all Law Firms associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPGkaW3aGJyKGyfn and case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    norm_judge_id = "NJUDT7jCZyFNeLGpRq" # str | The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired law firms. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Law Firms Associated With the Judge.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_judge(norm_judge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_law_firms_associated_with_norm_judge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Law Firms Associated With the Judge.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_judge(norm_judge_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_law_firms_associated_with_norm_judge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_judge_id** | **str**| The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired law firms. | [optional]
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

# **get_norm_parties_associated_with_norm_judge**
> AssociatedNormPartyResponse get_norm_parties_associated_with_norm_judge(norm_judge_id)

Parties Associated with the Judge.

Search for parties that have appeared before the specified judge using a keyword expression. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN (\"COLODj4BBVTho3pKpz\",\"COLOPUfJRhw5yPxgRi\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all Parties associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPGkaW3aGJyKGyfn and case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    norm_judge_id = "NJUDT7jCZyFNeLGpRq" # str | The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired parties. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Parties Associated with the Judge.
        api_response = api_instance.get_norm_parties_associated_with_norm_judge(norm_judge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_parties_associated_with_norm_judge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Parties Associated with the Judge.
        api_response = api_instance.get_norm_parties_associated_with_norm_judge(norm_judge_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->get_norm_parties_associated_with_norm_judge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_judge_id** | **str**| The normJudgeId value of the desired judge.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired parties. | [optional]
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

# **search_normalized_judges**
> NormJudgeSearchResponse search_normalized_judges()

Judge search.

### Search for a judge using a keyword expression. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_judge_search_response import NormJudgeSearchResponse
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    q = "normJudgeId:"NJUDFAJDwRVLYPoPjk"" # str | The keyword expression targeting the desired judge.</a>  (optional)
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Judge search.
        api_response = api_instance.search_normalized_judges(q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->search_normalized_judges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired judge.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormJudgeSearchResponse**](NormJudgeSearchResponse.md)

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

# **search_normalized_judges_by_id**
> NormJudgeSearchResponse search_normalized_judges_by_id(norm_judge_search_id)

Norm judge search results for a given normJudgeSearchId.

### Retrieve the desired search for a judge. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import judge_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_judge_search_response import NormJudgeSearchResponse
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
    api_instance = judge_analytics_api.JudgeAnalyticsApi(api_client)
    norm_judge_search_id = "JSRCi9NPpS2X4QNAt5" # str | The normJudgeSearchId value of the desired search.
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Norm judge search results for a given normJudgeSearchId.
        api_response = api_instance.search_normalized_judges_by_id(norm_judge_search_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->search_normalized_judges_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Norm judge search results for a given normJudgeSearchId.
        api_response = api_instance.search_normalized_judges_by_id(norm_judge_search_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JudgeAnalyticsApi->search_normalized_judges_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_judge_search_id** | **str**| The normJudgeSearchId value of the desired search. |
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormJudgeSearchResponse**](NormJudgeSearchResponse.md)

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

