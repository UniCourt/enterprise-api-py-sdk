# openapi_client.LawFirmAnalyticsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_norm_attorneys_associated_with_norm_law_firm**](LawFirmAnalyticsApi.md#get_norm_attorneys_associated_with_norm_law_firm) | **GET** /normLawFirm/{normLawFirmId}/associatedNormAttorneys | Attorneys working for the Law Firm.
[**get_norm_judges_associated_with_norm_law_firm**](LawFirmAnalyticsApi.md#get_norm_judges_associated_with_norm_law_firm) | **GET** /normLawFirm/{normLawFirmId}/associatedNormJudges | Judges Faced By the Law Firm.
[**get_norm_law_firm_by_id**](LawFirmAnalyticsApi.md#get_norm_law_firm_by_id) | **GET** /normLawFirm/{normLawFirmId} | Norm LawFirm Details.
[**get_norm_parties_associated_with_norm_law_firm**](LawFirmAnalyticsApi.md#get_norm_parties_associated_with_norm_law_firm) | **GET** /normLawFirm/{normLawFirmId}/associatedNormParties | Parties Represented by the Law Firm.
[**search_normalized_law_firms**](LawFirmAnalyticsApi.md#search_normalized_law_firms) | **GET** /normLawFirmSearch | Law firm search.
[**search_normalized_law_firms_by_id**](LawFirmAnalyticsApi.md#search_normalized_law_firms_by_id) | **GET** /normLawFirmSearch/{normLawFirmSearchId} | Norm law firm search result for a given normLawFirmSearchId.


# **get_norm_attorneys_associated_with_norm_law_firm**
> AssociatedNormAttorneyResponse get_norm_attorneys_associated_with_norm_law_firm(norm_law_firm_id)

Attorneys working for the Law Firm.

Retrieve the attorneys associated with a given normalized law firm. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTKQiA4LJuv54tEj\",\"CORTV4vCEaKrhystBz\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId**  | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate**  | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br>         ## Example Query Query to get all attorneys associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    norm_law_firm_id = "NORGrPmQyLdx9NGHcT" # str | The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired attorneys. Keywords should be constructed according to the guidelines given above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attorneys working for the Law Firm.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_law_firm(norm_law_firm_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_attorneys_associated_with_norm_law_firm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorneys working for the Law Firm.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_law_firm(norm_law_firm_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_attorneys_associated_with_norm_law_firm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_law_firm_id** | **str**| The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired attorneys. Keywords should be constructed according to the guidelines given above. | [optional]
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

# **get_norm_judges_associated_with_norm_law_firm**
> AssociatedNormJudgeResponse get_norm_judges_associated_with_norm_law_firm(norm_law_firm_id)

Judges Faced By the Law Firm.

Retrieve the judges before which a given normalized law firm has appeared. <br><br> ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTKQiA4LJuv54tEj\",\"CORTV4vCEaKrhystBz\")**| | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all judges associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    norm_law_firm_id = "NORGrPmQyLdx9NGHcT" # str | The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired judges. Keywords should be constructed according to the guidelines given above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Judges Faced By the Law Firm.
        api_response = api_instance.get_norm_judges_associated_with_norm_law_firm(norm_law_firm_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_judges_associated_with_norm_law_firm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Judges Faced By the Law Firm.
        api_response = api_instance.get_norm_judges_associated_with_norm_law_firm(norm_law_firm_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_judges_associated_with_norm_law_firm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_law_firm_id** | **str**| The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired judges. Keywords should be constructed according to the guidelines given above. | [optional]
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

# **get_norm_law_firm_by_id**
> NormLawFirm get_norm_law_firm_by_id(norm_law_firm_id)

Norm LawFirm Details.

Retrieve the specified normalized law firm. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_law_firm import NormLawFirm
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    norm_law_firm_id = "NORGrPmQyLdx9NGHcT" # str | The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18 

    # example passing only required values which don't have defaults set
    try:
        # Norm LawFirm Details.
        api_response = api_instance.get_norm_law_firm_by_id(norm_law_firm_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_law_firm_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_law_firm_id** | **str**| The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18  |

### Return type

[**NormLawFirm**](NormLawFirm.md)

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

# **get_norm_parties_associated_with_norm_law_firm**
> AssociatedNormPartyResponse get_norm_parties_associated_with_norm_law_firm(norm_law_firm_id)

Parties Represented by the Law Firm.

Retrieve the parties that the given normalized law firm has represented. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTKQiA4LJuv54tEj\",\"CORTV4vCEaKrhystBz\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all parties associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    norm_law_firm_id = "NORGrPmQyLdx9NGHcT" # str | The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired parties. Keywords should be constructed according to the guidelines given above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Parties Represented by the Law Firm.
        api_response = api_instance.get_norm_parties_associated_with_norm_law_firm(norm_law_firm_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_parties_associated_with_norm_law_firm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Parties Represented by the Law Firm.
        api_response = api_instance.get_norm_parties_associated_with_norm_law_firm(norm_law_firm_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->get_norm_parties_associated_with_norm_law_firm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_law_firm_id** | **str**| The normLawFirmId value of the desired normalized law firm.   - minimum: 18   - maximum: 18  |
 **q** | **str**| The keyword expression targeting the desired parties. Keywords should be constructed according to the guidelines given above. | [optional]
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

# **search_normalized_law_firms**
> NormLawFirmSearchResponse search_normalized_law_firms()

Law firm search.

### Retrieve a normalized law firm using a keyword expression. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_law_firm_search_response import NormLawFirmSearchResponse
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    q = "normLawFirmId:"NORGDiJQPjeed2mtvx"" # str | The keyword expression targeting the desired law firms.</a>  (optional)
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Law firm search.
        api_response = api_instance.search_normalized_law_firms(q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->search_normalized_law_firms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired law firms.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormLawFirmSearchResponse**](NormLawFirmSearchResponse.md)

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

# **search_normalized_law_firms_by_id**
> NormLawFirmSearchResponse search_normalized_law_firms_by_id(norm_law_firm_search_id)

Norm law firm search result for a given normLawFirmSearchId.

### Retrieve the specified search for a normalized law firm. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import law_firm_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_law_firm_search_response import NormLawFirmSearchResponse
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
    api_instance = law_firm_analytics_api.LawFirmAnalyticsApi(api_client)
    norm_law_firm_search_id = "LSRCeCT9pC3maopkW7" # str | The normLawFirmSearchId value of the search to be retrieved.
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Norm law firm search result for a given normLawFirmSearchId.
        api_response = api_instance.search_normalized_law_firms_by_id(norm_law_firm_search_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->search_normalized_law_firms_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Norm law firm search result for a given normLawFirmSearchId.
        api_response = api_instance.search_normalized_law_firms_by_id(norm_law_firm_search_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawFirmAnalyticsApi->search_normalized_law_firms_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_law_firm_search_id** | **str**| The normLawFirmSearchId value of the search to be retrieved. |
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormLawFirmSearchResponse**](NormLawFirmSearchResponse.md)

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

