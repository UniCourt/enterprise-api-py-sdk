# openapi_client.PartyAnalyticsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_norm_attorneys_associated_with_norm_party**](PartyAnalyticsApi.md#get_norm_attorneys_associated_with_norm_party) | **GET** /normParty/{normPartyId}/associatedNormAttorneys | Attorneys that represented the Party.
[**get_norm_judges_associated_with_norm_party**](PartyAnalyticsApi.md#get_norm_judges_associated_with_norm_party) | **GET** /normParty/{normPartyId}/associatedNormJudges | Judges Faced By the Party.
[**get_norm_law_firms_associated_with_norm_party**](PartyAnalyticsApi.md#get_norm_law_firms_associated_with_norm_party) | **GET** /normParty/{normPartyId}/associatedNormLawFirms | Law Firms that represented the Party.
[**get_norm_party_by_id**](PartyAnalyticsApi.md#get_norm_party_by_id) | **GET** /normParty/{normPartyId} | Norm Party Details.
[**search_normalized_parties**](PartyAnalyticsApi.md#search_normalized_parties) | **GET** /normPartySearch | Party search.
[**search_normalized_parties_by_id**](PartyAnalyticsApi.md#search_normalized_parties_by_id) | **GET** /normPartySearch/{normPartySearchId} | Norm party search results for a given normPartySearchId.


# **get_norm_attorneys_associated_with_norm_party**
> AssociatedNormAttorneyResponse get_norm_attorneys_associated_with_norm_party(norm_party_id)

Attorneys that represented the Party.

Search for attorneys who have represented a given party using a keyword expression. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\",\"CORTYsomR6GiiiPovp\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all attorneys associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    norm_party_id = "NORGrPmQyLdx9NGHcT" # str | The normPartyID value of the desired party.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired attorneys. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attorneys that represented the Party.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_party(norm_party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_attorneys_associated_with_norm_party: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorneys that represented the Party.
        api_response = api_instance.get_norm_attorneys_associated_with_norm_party(norm_party_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_attorneys_associated_with_norm_party: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_party_id** | **str**| The normPartyID value of the desired party.   - minimum: 18   - maximum: 18  |
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

# **get_norm_judges_associated_with_norm_party**
> AssociatedNormJudgeResponse get_norm_judges_associated_with_norm_party(norm_party_id)

Judges Faced By the Party.

Search for judges before whom a party has appeared using a keyword expression. <br><br> ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\",\"CORTYsomR6GiiiPovp\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all judges associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] <br><br> 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    norm_party_id = "NORGrPmQyLdx9NGHcT" # str | The normPartyId value of the desired party.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired judges. Keywords should be constructed according to the guidelines given above. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Judges Faced By the Party.
        api_response = api_instance.get_norm_judges_associated_with_norm_party(norm_party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_judges_associated_with_norm_party: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Judges Faced By the Party.
        api_response = api_instance.get_norm_judges_associated_with_norm_party(norm_party_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_judges_associated_with_norm_party: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_party_id** | **str**| The normPartyId value of the desired party.   - minimum: 18   - maximum: 18  |
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

# **get_norm_law_firms_associated_with_norm_party**
> AssociatedNormLawFirmResponse get_norm_law_firms_associated_with_norm_party(norm_party_id)

Law Firms that represented the Party.

Search for law firms that have represented the specified party using a keyword expression. ## Terms and Connectors | Connector | Schema   | Description  | Example | | ------| ------| ------|------| | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:\"CORTV4vCEaKrhystBz\" AND courtLocationId:\"COLO6b82CkRqS846hx\"**| | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN (\"CORTV4vCEaKrhystBz\",\"CORTYsomR6GiiiPovp\")**| | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:\"CORTV4vCEaKrhystBz\"** | | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:\"COSYACHBdMewtaG5DY\"** | | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:\"COTPm8jjc2PAydpFhq\"** | | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:\"COLO6b82CkRqS846hx\"** | | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:\"CTYPGkaW3aGJyKGyfn\"** | | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:\"CTYGBDwLfbbNBPBn5e\"** | | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:\"AOFL2UxEWfVmTPMyqf\"** | | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:\"CSCLNjbKTN7Yfo2wdb\"** | | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:\"PTYRiP8nMgPxBsPc5i\"** | | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:\"PTYGBnjxbx6tKNfVEP\"** | | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** | | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:\"California\"))** | | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.3 TO \\*]** | | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** | <br> ## Example Query Query to get all lawfirms associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPGkaW3aGJyKGyfn and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br> q=caseTypeId:\"CTYPGkaW3aGJyKGyfn\" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00] 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    norm_party_id = "NORGrPmQyLdx9NGHcT" # str | The normPartyId value of the desired party.   - minimum: 18   - maximum: 18 
    q = "caseTypeId:"CTYPGkaW3aGJyKGyfn" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]" # str | The keyword expression targeting the desired law firms. (optional)
    page_number = 1 # int | The page number of the desired page of results. - minimum: 1  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Law Firms that represented the Party.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_party(norm_party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_law_firms_associated_with_norm_party: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Law Firms that represented the Party.
        api_response = api_instance.get_norm_law_firms_associated_with_norm_party(norm_party_id, q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_law_firms_associated_with_norm_party: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_party_id** | **str**| The normPartyId value of the desired party.   - minimum: 18   - maximum: 18  |
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

# **get_norm_party_by_id**
> NormParty get_norm_party_by_id(norm_party_id)

Norm Party Details.

Retrieve the specified party. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
from openapi_client.model.norm_party import NormParty
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    norm_party_id = "NORGrPmQyLdx9NGHcT" # str | The normPartyId value of the desired party.   - minimum: 18   - maximum: 18 

    # example passing only required values which don't have defaults set
    try:
        # Norm Party Details.
        api_response = api_instance.get_norm_party_by_id(norm_party_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->get_norm_party_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_party_id** | **str**| The normPartyId value of the desired party.   - minimum: 18   - maximum: 18  |

### Return type

[**NormParty**](NormParty.md)

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

# **search_normalized_parties**
> NormPartySearchResponse search_normalized_parties()

Party search.

### Search for a party using a keyword expression. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_party_search_response import NormPartySearchResponse
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    q = "normPartyId:"NORGJWPpNLekV7dKTm"" # str | The keyword expression targeting the desired party.</a>  (optional)
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Party search.
        api_response = api_instance.search_normalized_parties(q=q, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->search_normalized_parties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired party.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormPartySearchResponse**](NormPartySearchResponse.md)

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

# **search_normalized_parties_by_id**
> NormPartySearchResponse search_normalized_parties_by_id(norm_party_search_id)

Norm party search results for a given normPartySearchId.

### Retrieve a search for a party. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import party_analytics_api
from openapi_client.model.exception import Exception
from openapi_client.model.norm_party_search_response import NormPartySearchResponse
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
    api_instance = party_analytics_api.PartyAnalyticsApi(api_client)
    norm_party_search_id = "PSRCUoacNCGj9ezvqf" # str | The normPartySearchId value of the search to be retrieved.
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Norm party search results for a given normPartySearchId.
        api_response = api_instance.search_normalized_parties_by_id(norm_party_search_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->search_normalized_parties_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Norm party search results for a given normPartySearchId.
        api_response = api_instance.search_normalized_parties_by_id(norm_party_search_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartyAnalyticsApi->search_normalized_parties_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **norm_party_search_id** | **str**| The normPartySearchId value of the search to be retrieved. |
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**NormPartySearchResponse**](NormPartySearchResponse.md)

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

