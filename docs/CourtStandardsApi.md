# openapi_client.CourtStandardsApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_appeal_courts_for_court**](CourtStandardsApi.md#get_appeal_courts_for_court) | **GET** /masterData/court/{courtId}/appealCourts | Appeal Court Objects for given courtId.
[**get_area_of_law**](CourtStandardsApi.md#get_area_of_law) | **GET** /masterData/areaOfLaw/{areaOfLawId} | AreaOfLaw Object for the given AreaOfLaw Id.
[**get_areas_of_law**](CourtStandardsApi.md#get_areas_of_law) | **GET** /masterData/areaOfLaw | AreaOfLaw Object.
[**get_attorney_representation_type**](CourtStandardsApi.md#get_attorney_representation_type) | **GET** /masterData/attorneyRepresentationType/{attorneyRepresentationTypeId} | Attorney Representation Type Object for the given attorneyRepresentationTypeId.
[**get_attorney_representation_types**](CourtStandardsApi.md#get_attorney_representation_types) | **GET** /masterData/attorneyRepresentationType | Attorney Representation Type Object.
[**get_attorney_type**](CourtStandardsApi.md#get_attorney_type) | **GET** /masterData/attorneyType/{attorneyTypeId} | Attorney Type Object for given Attorney Type Id.
[**get_attorney_types**](CourtStandardsApi.md#get_attorney_types) | **GET** /masterData/attorneyType | Attorney Type Object.
[**get_case_class**](CourtStandardsApi.md#get_case_class) | **GET** /masterData/caseClass/{caseClassId} | Case Class Object for the given Case Class Id.
[**get_case_relationship_type**](CourtStandardsApi.md#get_case_relationship_type) | **GET** /masterData/caseRelationshipType/{caseRelationshipTypeId} | Case Relationship Type Object for the given caseRelationshipTypeId.
[**get_case_relationship_types**](CourtStandardsApi.md#get_case_relationship_types) | **GET** /masterData/caseRelationshipType | Case Relationship Type Object.
[**get_case_status**](CourtStandardsApi.md#get_case_status) | **GET** /masterData/caseStatus/{caseStatusId} | Returns the caseStatus information for the given caseStatusId.
[**get_case_status_group**](CourtStandardsApi.md#get_case_status_group) | **GET** /masterData/caseStatusGroup/{caseStatusGroupId} | Returns the caseStatusGroup information for the given caseStatusGroupId.
[**get_case_status_groups**](CourtStandardsApi.md#get_case_status_groups) | **GET** /masterData/caseStatusGroup | Case Status Group Object.
[**get_case_type**](CourtStandardsApi.md#get_case_type) | **GET** /masterData/caseType/{caseTypeId} | CaseType Object for given Case Type Id.
[**get_case_type_group**](CourtStandardsApi.md#get_case_type_group) | **GET** /masterData/caseTypeGroup/{caseTypeGroupId} | CaseType Group for the given CaseType Group Id.
[**get_case_type_groups**](CourtStandardsApi.md#get_case_type_groups) | **GET** /masterData/caseTypeGroup | CaseTypeGroup Object.
[**get_case_types**](CourtStandardsApi.md#get_case_types) | **GET** /masterData/caseType | Case Type Object.
[**get_cases_class**](CourtStandardsApi.md#get_cases_class) | **GET** /masterData/caseClass | Case Class Object.
[**get_cases_status**](CourtStandardsApi.md#get_cases_status) | **GET** /masterData/caseStatus | Case Status Object.
[**get_cause_of_action**](CourtStandardsApi.md#get_cause_of_action) | **GET** /masterData/causeOfAction/{causeOfActionId} | CauseOfAction Object for the given causeOfActionId.
[**get_cause_of_action_additional_data**](CourtStandardsApi.md#get_cause_of_action_additional_data) | **GET** /masterData/causeOfActionAdditionalData/{causeOfActionAdditionalDataId} | CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.
[**get_cause_of_action_group**](CourtStandardsApi.md#get_cause_of_action_group) | **GET** /masterData/causeOfActionGroup/{causeOfActionGroupId} | CauseOfActionGroup Object for the given causeOfActionGroupId.
[**get_causes_of_action**](CourtStandardsApi.md#get_causes_of_action) | **GET** /masterData/causeOfAction | CauseOfAction Object.
[**get_causes_of_action_additional_data**](CourtStandardsApi.md#get_causes_of_action_additional_data) | **GET** /masterData/causeOfActionAdditionalData | CauseOfActionAdditionaData Object.
[**get_causes_of_action_group**](CourtStandardsApi.md#get_causes_of_action_group) | **GET** /masterData/causeOfActionGroup | CauseOfActionGroup Object.
[**get_charge**](CourtStandardsApi.md#get_charge) | **GET** /masterData/charge/{chargeId} | Charge Object for the given chargeId.
[**get_charge_additional_data**](CourtStandardsApi.md#get_charge_additional_data) | **GET** /masterData/chargeAdditionalData/{chargeAdditionalDataId} | Charge Additional Data Object for the given chargeAdditionalDataId.
[**get_charge_degree**](CourtStandardsApi.md#get_charge_degree) | **GET** /masterData/chargeDegree/{chargeDegreeId} | ChargeDegree Object for the given chargeDegreeId.
[**get_charge_group**](CourtStandardsApi.md#get_charge_group) | **GET** /masterData/chargeGroup/{chargeGroupId} | Charge Group Object for the given chargeGroupId.
[**get_charge_groups**](CourtStandardsApi.md#get_charge_groups) | **GET** /masterData/chargeGroup | Charge Group Object.
[**get_charge_severity**](CourtStandardsApi.md#get_charge_severity) | **GET** /masterData/chargeSeverity/{chargeSeverityId} | ChargeSeverity Object for the given chargeSeverityId.
[**get_charges**](CourtStandardsApi.md#get_charges) | **GET** /masterData/charge | Charge Object.
[**get_charges_additional_data**](CourtStandardsApi.md#get_charges_additional_data) | **GET** /masterData/chargeAdditionalData | Charge Additional Data Object.
[**get_charges_degree**](CourtStandardsApi.md#get_charges_degree) | **GET** /masterData/chargeDegree | ChargeDegree Object.
[**get_charges_severity**](CourtStandardsApi.md#get_charges_severity) | **GET** /masterData/chargeSeverity | ChargeSeverity Object.
[**get_court**](CourtStandardsApi.md#get_court) | **GET** /masterData/court/{courtId} | Court Object for given courtId.
[**get_court_location**](CourtStandardsApi.md#get_court_location) | **GET** /masterData/courtLocation/{courtLocationId} | Courthouse Object for given Court Location Id.
[**get_court_locations**](CourtStandardsApi.md#get_court_locations) | **GET** /masterData/courtLocation | Courthouse Object.
[**get_court_locations_for_court**](CourtStandardsApi.md#get_court_locations_for_court) | **GET** /masterData/court/{courtId}/courtLocations | Associated Court Location for given courtId.
[**get_court_service_status**](CourtStandardsApi.md#get_court_service_status) | **GET** /masterData/courtServiceStatus/{courtServiceStatusId} | Court Service Status Object for the given courtServiceStatusId.
[**get_court_system**](CourtStandardsApi.md#get_court_system) | **GET** /masterData/courtSystem/{courtSystemId} | Court System Object for given courtSystemId.
[**get_court_systems**](CourtStandardsApi.md#get_court_systems) | **GET** /masterData/courtSystem | Court System Objects.
[**get_court_type**](CourtStandardsApi.md#get_court_type) | **GET** /masterData/courtType/{courtTypeId} | Court Type Object for given courtTypeId.
[**get_court_types**](CourtStandardsApi.md#get_court_types) | **GET** /masterData/courtType | Court Type Objects.
[**get_courts**](CourtStandardsApi.md#get_courts) | **GET** /masterData/court | Court Objects.
[**get_courts_for_court_location**](CourtStandardsApi.md#get_courts_for_court_location) | **GET** /masterData/courtLocation/{courtLocationId}/courts | Associated Court for given Court Location.
[**get_courts_for_jurisdiction_geo**](CourtStandardsApi.md#get_courts_for_jurisdiction_geo) | **GET** /masterData/jurisdictionGeo/{jurisdictionGeoId}/courts | Associated Court for given Jurisdiction Geo.
[**get_courts_service_status**](CourtStandardsApi.md#get_courts_service_status) | **GET** /masterData/courtServiceStatus | Court Service Status Object.
[**get_judge_type**](CourtStandardsApi.md#get_judge_type) | **GET** /masterData/judgeType/{judgeTypeId} | Judge Type Object for the given judgeTypeId.
[**get_judge_types**](CourtStandardsApi.md#get_judge_types) | **GET** /masterData/judgeType | Judge Type Object.
[**get_jurisdiction_geo**](CourtStandardsApi.md#get_jurisdiction_geo) | **GET** /masterData/jurisdictionGeo/{jurisdictionGeoId} | Jurisdiction Geo Object for given Jurisdiction Geo Id.
[**get_jurisdiction_geo_for_court**](CourtStandardsApi.md#get_jurisdiction_geo_for_court) | **GET** /masterData/court/{courtId}/jurisdictionGeo | Jurisdiction Geo Objects for given courtId.
[**get_jurisdictions_geo**](CourtStandardsApi.md#get_jurisdictions_geo) | **GET** /masterData/jurisdictionGeo | Jurisdiction Geo Object.
[**get_party_role**](CourtStandardsApi.md#get_party_role) | **GET** /masterData/partyRole/{partyRoleId} | Party Role Object.
[**get_party_role_group**](CourtStandardsApi.md#get_party_role_group) | **GET** /masterData/partyRoleGroup/{partyRoleGroupId} | Party Role Group Object.
[**get_party_role_groups**](CourtStandardsApi.md#get_party_role_groups) | **GET** /masterData/partyRoleGroup | Party Role Group Object.
[**get_party_roles**](CourtStandardsApi.md#get_party_roles) | **GET** /masterData/partyRole | Party Role Object.


# **get_appeal_courts_for_court**
> CourtResponse get_appeal_courts_for_court(court_id)

Appeal Court Objects for given courtId.

Retrieve the appeals courts associated with the specified court. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_response import CourtResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_id = "CORThSxcef8eGUSkuC" # str | The courtId value of the target court.
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Appeal Court Objects for given courtId.
        api_response = api_instance.get_appeal_courts_for_court(court_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_appeal_courts_for_court: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Appeal Court Objects for given courtId.
        api_response = api_instance.get_appeal_courts_for_court(court_id, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_appeal_courts_for_court: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_id** | **str**| The courtId value of the target court. |
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtResponse**](CourtResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_area_of_law**
> AreaOfLaw get_area_of_law(area_of_law_id)

AreaOfLaw Object for the given AreaOfLaw Id.

Retrieve the specified area of law. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.area_of_law import AreaOfLaw
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    area_of_law_id = "AOFLGAd9Ah5qkTRNw9" # str | The areaOfLawId value of the desired area of law.

    # example passing only required values which don't have defaults set
    try:
        # AreaOfLaw Object for the given AreaOfLaw Id.
        api_response = api_instance.get_area_of_law(area_of_law_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_area_of_law: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_of_law_id** | **str**| The areaOfLawId value of the desired area of law. |

### Return type

[**AreaOfLaw**](AreaOfLaw.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_areas_of_law**
> AreaOfLawResponse get_areas_of_law()

AreaOfLaw Object.

The keyword expression targeting the desired area of law.   ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.area_of_law_response import AreaOfLawResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "areaOfLawId: "AOFLGAd9Ah5qkTRNw9"" # str | Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # AreaOfLaw Object.
        api_response = api_instance.get_areas_of_law(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_areas_of_law: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**AreaOfLawResponse**](AreaOfLawResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attorney_representation_type**
> AttorneyRepresentationType get_attorney_representation_type(attorney_representation_type_id)

Attorney Representation Type Object for the given attorneyRepresentationTypeId.

Retrieve the specified attorney representation type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.attorney_representation_type import AttorneyRepresentationType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    attorney_representation_type_id = "ATRPYgPMGJufoCsR6Q" # str | The attorneyRepresentationTypeId value of the desired attorney representation type.

    # example passing only required values which don't have defaults set
    try:
        # Attorney Representation Type Object for the given attorneyRepresentationTypeId.
        api_response = api_instance.get_attorney_representation_type(attorney_representation_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_attorney_representation_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_representation_type_id** | **str**| The attorneyRepresentationTypeId value of the desired attorney representation type. |

### Return type

[**AttorneyRepresentationType**](AttorneyRepresentationType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attorney_representation_types**
> AttorneyRepresentationTypeResponse get_attorney_representation_types()

Attorney Representation Type Object.

Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above. ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.attorney_representation_type_response import AttorneyRepresentationTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "attorneyRepresentationTypeId: "ATRPYgPMGJufoCsR6Q"" # str | The keyword expression targeting the attorney representation type.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorney Representation Type Object.
        api_response = api_instance.get_attorney_representation_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_attorney_representation_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the attorney representation type.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**AttorneyRepresentationTypeResponse**](AttorneyRepresentationTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attorney_type**
> AttorneyType get_attorney_type(attorney_type_id)

Attorney Type Object for given Attorney Type Id.

Retrieve a specified attorney type object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.attorney_type import AttorneyType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    attorney_type_id = "ATYPWXtARwvzu5HLcf" # str | The attorneyTypeId value of the desired attorney type.

    # example passing only required values which don't have defaults set
    try:
        # Attorney Type Object for given Attorney Type Id.
        api_response = api_instance.get_attorney_type(attorney_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_attorney_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_type_id** | **str**| The attorneyTypeId value of the desired attorney type. |

### Return type

[**AttorneyType**](AttorneyType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attorney_types**
> AttorneyTypeResponse get_attorney_types()

Attorney Type Object.

Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.attorney_type_response import AttorneyTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "attorneyTypeId:"ATYPWXtARwvzu5HLcf"" # str | The keyword expression targeting the attorney type.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attorney Type Object.
        api_response = api_instance.get_attorney_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_attorney_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the attorney type.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**AttorneyTypeResponse**](AttorneyTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_class**
> CaseClass get_case_class(case_class_id)

Case Class Object for the given Case Class Id.

Retrieve the specified case class. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_class import CaseClass
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_class_id = "CSCLNjbKTN7Yfo2wdb" # str | The caseClassId value of the desired case class.

    # example passing only required values which don't have defaults set
    try:
        # Case Class Object for the given Case Class Id.
        api_response = api_instance.get_case_class(case_class_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_class_id** | **str**| The caseClassId value of the desired case class. |

### Return type

[**CaseClass**](CaseClass.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_relationship_type**
> CaseRelationshipType get_case_relationship_type(case_relationship_type_id)

Case Relationship Type Object for the given caseRelationshipTypeId.

Retrieve the specified case relationship type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_relationship_type import CaseRelationshipType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_relationship_type_id = "CRTPgkmnzpiBXstT3s" # str | The caseRelationshipTypeId value of the desired case relationship type.

    # example passing only required values which don't have defaults set
    try:
        # Case Relationship Type Object for the given caseRelationshipTypeId.
        api_response = api_instance.get_case_relationship_type(case_relationship_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_relationship_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_relationship_type_id** | **str**| The caseRelationshipTypeId value of the desired case relationship type. |

### Return type

[**CaseRelationshipType**](CaseRelationshipType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_relationship_types**
> CaseRelationshipTypeResponse get_case_relationship_types()

Case Relationship Type Object.

Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_relationship_type_response import CaseRelationshipTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseRelationshipTypeId: "CRTPgkmnzpiBXstT3s"" # str | The keyword expression targeting the case relationship type.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case Relationship Type Object.
        api_response = api_instance.get_case_relationship_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_relationship_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the case relationship type.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseRelationshipTypeResponse**](CaseRelationshipTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_status**
> CaseStatus get_case_status(case_status_id)

Returns the caseStatus information for the given caseStatusId.

Retrieve the specified case status. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_status import CaseStatus
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_status_id = "CSSTBtqf3R2LYFt4j4" # str | The caseStatusId value of the desired case status.

    # example passing only required values which don't have defaults set
    try:
        # Returns the caseStatus information for the given caseStatusId.
        api_response = api_instance.get_case_status(case_status_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_status_id** | **str**| The caseStatusId value of the desired case status. |

### Return type

[**CaseStatus**](CaseStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_status_group**
> CaseStatusGroup get_case_status_group(case_status_group_id)

Returns the caseStatusGroup information for the given caseStatusGroupId.

Retrieve the specified case status group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_status_group import CaseStatusGroup
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_status_group_id = "CSSG6ERqyFdydo52WK" # str | The caseStatusGroupId value of the desired case status group.

    # example passing only required values which don't have defaults set
    try:
        # Returns the caseStatusGroup information for the given caseStatusGroupId.
        api_response = api_instance.get_case_status_group(case_status_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_status_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_status_group_id** | **str**| The caseStatusGroupId value of the desired case status group. |

### Return type

[**CaseStatusGroup**](CaseStatusGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_status_groups**
> CaseStatusGroupResponse get_case_status_groups()

Case Status Group Object.

Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_status_group_response import CaseStatusGroupResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseStatusGroupId:"CSSG6ERqyFdydo52WK"" # str | The keyword expression targeting the desired case status group.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case Status Group Object.
        api_response = api_instance.get_case_status_groups(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_status_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired case status group.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseStatusGroupResponse**](CaseStatusGroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_type**
> CaseType get_case_type(case_type_id)

CaseType Object for given Case Type Id.

Retrieve the specified case type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_type import CaseType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_type_id = "CTYPoLU7sWaGjWtkBx" # str | The caseTypeId value of the desired case type.

    # example passing only required values which don't have defaults set
    try:
        # CaseType Object for given Case Type Id.
        api_response = api_instance.get_case_type(case_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_type_id** | **str**| The caseTypeId value of the desired case type. |

### Return type

[**CaseType**](CaseType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_type_group**
> CaseTypeGroup get_case_type_group(case_type_group_id)

CaseType Group for the given CaseType Group Id.

Retrieve the specified case type group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_type_group import CaseTypeGroup
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    case_type_group_id = "CTYGSpWaVityBQndsv" # str | caseTypeGroupId

    # example passing only required values which don't have defaults set
    try:
        # CaseType Group for the given CaseType Group Id.
        api_response = api_instance.get_case_type_group(case_type_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_type_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_type_group_id** | **str**| caseTypeGroupId |

### Return type

[**CaseTypeGroup**](CaseTypeGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_type_groups**
> CaseTypeGroupResponse get_case_type_groups()

CaseTypeGroup Object.

Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_type_group_response import CaseTypeGroupResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseTypeGroupId: "CTYGSpWaVityBQndsv"" # str | Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CaseTypeGroup Object.
        api_response = api_instance.get_case_type_groups(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_type_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseTypeGroupResponse**](CaseTypeGroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_types**
> CaseTypeResponse get_case_types()

Case Type Object.

Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.case_type_response import CaseTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseTypeId: "CTYPoLU7sWaGjWtkBx"" # str | Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case Type Object.
        api_response = api_instance.get_case_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_case_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseTypeResponse**](CaseTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cases_class**
> CaseClassResponse get_cases_class()

Case Class Object.

Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_class_response import CaseClassResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseClassId:"CSCLNjbKTN7Yfo2wdb"" # str | The keyword expression targeting the desired case class.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case Class Object.
        api_response = api_instance.get_cases_class(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_cases_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired case class.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseClassResponse**](CaseClassResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cases_status**
> CaseStatusResponse get_cases_status()

Case Status Object.

Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.case_status_response import CaseStatusResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "caseStatusId: "CSSTBtqf3R2LYFt4j4"" # str | The keyword expression targeting the desired case status.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case Status Object.
        api_response = api_instance.get_cases_status(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_cases_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired case status.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CaseStatusResponse**](CaseStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cause_of_action**
> CauseOfAction get_cause_of_action(cause_of_action_id)

CauseOfAction Object for the given causeOfActionId.

Retrieve the specified cause of action. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.cause_of_action import CauseOfAction
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    cause_of_action_id = "CATNoLU7sWaGjWtkBx" # str | The causeOfActionId value of the desired cause of action.

    # example passing only required values which don't have defaults set
    try:
        # CauseOfAction Object for the given causeOfActionId.
        api_response = api_instance.get_cause_of_action(cause_of_action_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_cause_of_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause_of_action_id** | **str**| The causeOfActionId value of the desired cause of action. |

### Return type

[**CauseOfAction**](CauseOfAction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cause_of_action_additional_data**
> CauseOfActionAdditionalData get_cause_of_action_additional_data(cause_of_action_additional_data_id)

CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.

Retrieve the specified cause of action additional data. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.cause_of_action_additional_data import CauseOfActionAdditionalData
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    cause_of_action_additional_data_id = "CAADoLU7sWaGjWtkBx" # str | The causeOfActionAdditionalDataId value of the desired cause of action additional data.

    # example passing only required values which don't have defaults set
    try:
        # CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.
        api_response = api_instance.get_cause_of_action_additional_data(cause_of_action_additional_data_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_cause_of_action_additional_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause_of_action_additional_data_id** | **str**| The causeOfActionAdditionalDataId value of the desired cause of action additional data. |

### Return type

[**CauseOfActionAdditionalData**](CauseOfActionAdditionalData.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cause_of_action_group**
> CauseOfActionGroup get_cause_of_action_group(cause_of_action_group_id)

CauseOfActionGroup Object for the given causeOfActionGroupId.

Retrieve the specified cause of action group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.cause_of_action_group import CauseOfActionGroup
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    cause_of_action_group_id = "CAGPoLU7sWaGjWtkBx" # str | causeOfActionGroupId

    # example passing only required values which don't have defaults set
    try:
        # CauseOfActionGroup Object for the given causeOfActionGroupId.
        api_response = api_instance.get_cause_of_action_group(cause_of_action_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_cause_of_action_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause_of_action_group_id** | **str**| causeOfActionGroupId |

### Return type

[**CauseOfActionGroup**](CauseOfActionGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_causes_of_action**
> CauseOfActionResponse get_causes_of_action()

CauseOfAction Object.

Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.cause_of_action_response import CauseOfActionResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "causeOfActionId:"CATNiHoKn66p3bkcNs"" # str | The keyword expression targeting the desired cause of action.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CauseOfAction Object.
        api_response = api_instance.get_causes_of_action(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_causes_of_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired cause of action.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CauseOfActionResponse**](CauseOfActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_causes_of_action_additional_data**
> CauseOfActionAdditionalDataResponse get_causes_of_action_additional_data()

CauseOfActionAdditionaData Object.

Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.cause_of_action_additional_data_response import CauseOfActionAdditionalDataResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "causeOfActionAdditionalDataId:"CAADiHoKn66p3bkcNs"" # str | The keyword expression targeting the desired cause of action additional data.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CauseOfActionAdditionaData Object.
        api_response = api_instance.get_causes_of_action_additional_data(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_causes_of_action_additional_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired cause of action additional data.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CauseOfActionAdditionalDataResponse**](CauseOfActionAdditionalDataResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_causes_of_action_group**
> CauseOfActionGroupResponse get_causes_of_action_group()

CauseOfActionGroup Object.

Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.cause_of_action_group_response import CauseOfActionGroupResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "causeOfActionGroupId:"CAGPiHoKn66p3bkcNs"" # str | The keyword expression targeting the desired cause of action group.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CauseOfActionGroup Object.
        api_response = api_instance.get_causes_of_action_group(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_causes_of_action_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired cause of action group.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CauseOfActionGroupResponse**](CauseOfActionGroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge**
> Charge get_charge(charge_id)

Charge Object for the given chargeId.

Retrieve the specified charge. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge import Charge
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    charge_id = "CHRGiHoKn66p3bkcNs" # str | The chargeId value of the desired charge.

    # example passing only required values which don't have defaults set
    try:
        # Charge Object for the given chargeId.
        api_response = api_instance.get_charge(charge_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| The chargeId value of the desired charge. |

### Return type

[**Charge**](Charge.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge_additional_data**
> ChargeAdditionalData get_charge_additional_data(charge_additional_data_id)

Charge Additional Data Object for the given chargeAdditionalDataId.

Retrieve the specified charge additional data. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_additional_data import ChargeAdditionalData
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    charge_additional_data_id = "CHADiHoKn66p3bkcNs" # str | The chargeAdditionalDataId value of the desired charge additional data.

    # example passing only required values which don't have defaults set
    try:
        # Charge Additional Data Object for the given chargeAdditionalDataId.
        api_response = api_instance.get_charge_additional_data(charge_additional_data_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge_additional_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_additional_data_id** | **str**| The chargeAdditionalDataId value of the desired charge additional data. |

### Return type

[**ChargeAdditionalData**](ChargeAdditionalData.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge_degree**
> ChargeDegree get_charge_degree(charge_degree_id)

ChargeDegree Object for the given chargeDegreeId.

Retrieve the specified charge degree. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_degree import ChargeDegree
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    charge_degree_id = "CHDGiHoKn66p3bkcNs" # str | The chargeDegreeId value of the desired charge degree.

    # example passing only required values which don't have defaults set
    try:
        # ChargeDegree Object for the given chargeDegreeId.
        api_response = api_instance.get_charge_degree(charge_degree_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge_degree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_degree_id** | **str**| The chargeDegreeId value of the desired charge degree. |

### Return type

[**ChargeDegree**](ChargeDegree.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge_group**
> ChargeGroup get_charge_group(charge_group_id)

Charge Group Object for the given chargeGroupId.

Retrieve the specified charge group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_group import ChargeGroup
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    charge_group_id = "CHGPiHoKn66p3bkcNs" # str | The chargeGroupId value of the desired charge group.

    # example passing only required values which don't have defaults set
    try:
        # Charge Group Object for the given chargeGroupId.
        api_response = api_instance.get_charge_group(charge_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_group_id** | **str**| The chargeGroupId value of the desired charge group. |

### Return type

[**ChargeGroup**](ChargeGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge_groups**
> ChargeGroupResponse get_charge_groups()

Charge Group Object.

Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_group_response import ChargeGroupResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "chargeGroupId:"CHRGoLU7sWaGjWtkBx"" # str | The keyword expression targeting the desired charge group.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Charge Group Object.
        api_response = api_instance.get_charge_groups(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired charge group.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**ChargeGroupResponse**](ChargeGroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charge_severity**
> ChargeSeverity get_charge_severity(charge_severity_id)

ChargeSeverity Object for the given chargeSeverityId.

Retrieve the specified charge severity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_severity import ChargeSeverity
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    charge_severity_id = "CHSEiHoKn66p3bkcNs" # str | The chargeSeverityId value of the desired charge severity.

    # example passing only required values which don't have defaults set
    try:
        # ChargeSeverity Object for the given chargeSeverityId.
        api_response = api_instance.get_charge_severity(charge_severity_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charge_severity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_severity_id** | **str**| The chargeSeverityId value of the desired charge severity. |

### Return type

[**ChargeSeverity**](ChargeSeverity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges**
> ChargeResponse get_charges()

Charge Object.

Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.charge_response import ChargeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "chargeId:"CHRGoLU7sWaGjWtkBx"" # str | The keyword expression targeting the desired charge.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Charge Object.
        api_response = api_instance.get_charges(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired charge.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_additional_data**
> ChargeAdditionalDataResponse get_charges_additional_data()

Charge Additional Data Object.

Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.charge_additional_data_response import ChargeAdditionalDataResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "chargeAdditionalDataId:"CHADoLU7sWaGjWtkBx"" # str | The keyword expression targeting the desired charge additional data.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Charge Additional Data Object.
        api_response = api_instance.get_charges_additional_data(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charges_additional_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired charge additional data.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**ChargeAdditionalDataResponse**](ChargeAdditionalDataResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_degree**
> ChargeDegreeResponse get_charges_degree()

ChargeDegree Object.

Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_degree_response import ChargeDegreeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "chargeDegreeId:"CHDGiHoKn66p3bkcNs"" # str | The keyword expression targeting the desired charge degree.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ChargeDegree Object.
        api_response = api_instance.get_charges_degree(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charges_degree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired charge degree.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**ChargeDegreeResponse**](ChargeDegreeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_severity**
> ChargeSeverityResponse get_charges_severity()

ChargeSeverity Object.

Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.charge_severity_response import ChargeSeverityResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "chargeSeverityId:"CHSEiHoKn66p3bkcNs"" # str | The keyword expression targeting the desired charge severity.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ChargeSeverity Object.
        api_response = api_instance.get_charges_severity(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_charges_severity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired charge severity.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**ChargeSeverityResponse**](ChargeSeverityResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court**
> Court get_court(court_id)

Court Object for given courtId.

Retrieve information about a specified court. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court import Court
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_id = "CORThSxcef8eGUSkuC" # str | The courtId value of the target court.

    # example passing only required values which don't have defaults set
    try:
        # Court Object for given courtId.
        api_response = api_instance.get_court(court_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_id** | **str**| The courtId value of the target court. |

### Return type

[**Court**](Court.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_location**
> CourtLocation get_court_location(court_location_id)

Courthouse Object for given Court Location Id.

Contains the Court Location Object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.court_location import CourtLocation
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_location_id = "COLOV75AKgqMqnfVhM" # str | courtLocationId

    # example passing only required values which don't have defaults set
    try:
        # Courthouse Object for given Court Location Id.
        api_response = api_instance.get_court_location(court_location_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_location_id** | **str**| courtLocationId |

### Return type

[**CourtLocation**](CourtLocation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_locations**
> CourtLocationResponse get_court_locations()

Courthouse Object.

Retrieve the specified court location or court locations.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_location_response import CourtLocationResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "courtLocationId:"COLO9g3fhYM4bmxveA"" # str | The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Courthouse Object.
        api_response = api_instance.get_court_locations(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtLocationResponse**](CourtLocationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_locations_for_court**
> CourtLocationResponse get_court_locations_for_court(court_id)

Associated Court Location for given courtId.

Retrieve the court locations associated with the specified court. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_location_response import CourtLocationResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_id = "CORThSxcef8eGUSkuC" # str | The courtId value of the target court.
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Associated Court Location for given courtId.
        api_response = api_instance.get_court_locations_for_court(court_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_locations_for_court: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associated Court Location for given courtId.
        api_response = api_instance.get_court_locations_for_court(court_id, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_locations_for_court: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_id** | **str**| The courtId value of the target court. |
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtLocationResponse**](CourtLocationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_service_status**
> CourtServiceStatus get_court_service_status(court_service_status_id)

Court Service Status Object for the given courtServiceStatusId.

Retrieve the court status of the specified court. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_service_status import CourtServiceStatus
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_service_status_id = "CTSSf45fd1bd792e97" # str | The courtServiceStatusId value of the desired court.

    # example passing only required values which don't have defaults set
    try:
        # Court Service Status Object for the given courtServiceStatusId.
        api_response = api_instance.get_court_service_status(court_service_status_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_service_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_service_status_id** | **str**| The courtServiceStatusId value of the desired court. |

### Return type

[**CourtServiceStatus**](CourtServiceStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_system**
> CourtSystem get_court_system(court_system_id)

Court System Object for given courtSystemId.

Retrieve the specified court system. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.court_system import CourtSystem
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_system_id = "COSY4vuCtGQeAmdDdN" # str | The courtSystemId value of the court system to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Court System Object for given courtSystemId.
        api_response = api_instance.get_court_system(court_system_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_system_id** | **str**| The courtSystemId value of the court system to be retrieved. |

### Return type

[**CourtSystem**](CourtSystem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_systems**
> CourtSystemResponse get_court_systems()

Court System Objects.

Retrieve information about the specified court system or court systems.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_system_response import CourtSystemResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "courtSystemId:"COSY4vuCtGQeAmdDdN"" # str | The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Court System Objects.
        api_response = api_instance.get_court_systems(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_systems: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtSystemResponse**](CourtSystemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_type**
> CourtType get_court_type(court_type_id)

Court Type Object for given courtTypeId.

Retrieve the information concerning the specific court type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.court_type import CourtType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_type_id = "COTPm8jjc2PAydpFhq" # str | The courtTypeId value of the court type to be retrieved.

    # example passing only required values which don't have defaults set
    try:
        # Court Type Object for given courtTypeId.
        api_response = api_instance.get_court_type(court_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type_id** | **str**| The courtTypeId value of the court type to be retrieved. |

### Return type

[**CourtType**](CourtType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_court_types**
> CourtTypeResponse get_court_types()

Court Type Objects.

Retrieve court types recognized by UniCourt.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_type_response import CourtTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "courtTypeId:"COTPm8jjc2PAydpFhq"" # str | The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Court Type Objects.
        api_response = api_instance.get_court_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_court_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtTypeResponse**](CourtTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courts**
> CourtResponse get_courts()

Court Objects.

Retrieve information about a specified court or courts.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_response import CourtResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "courtId:"CORThSxcef8eGUSkuC"" # str | The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Court Objects.
        api_response = api_instance.get_courts(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtResponse**](CourtResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courts_for_court_location**
> CourtResponse get_courts_for_court_location(court_location_id)

Associated Court for given Court Location.

Retrieve the courts associated with the specified court location. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_response import CourtResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_location_id = "COLOV75AKgqMqnfVhM" # str | The courtLocationId value of the court location for which courts are to be retrieved.
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Associated Court for given Court Location.
        api_response = api_instance.get_courts_for_court_location(court_location_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts_for_court_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associated Court for given Court Location.
        api_response = api_instance.get_courts_for_court_location(court_location_id, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts_for_court_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_location_id** | **str**| The courtLocationId value of the court location for which courts are to be retrieved. |
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtResponse**](CourtResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courts_for_jurisdiction_geo**
> CourtResponse get_courts_for_jurisdiction_geo(jurisdiction_geo_id)

Associated Court for given Jurisdiction Geo.

Returns Associated Court for given Jurisdiction Geo. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_response import CourtResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    jurisdiction_geo_id = "JUGO8s7HvM84dLvVMu" # str | jurisdictionGeoId
    page_number = 1 # int | Page number. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | Sort field. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Sort order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Associated Court for given Jurisdiction Geo.
        api_response = api_instance.get_courts_for_jurisdiction_geo(jurisdiction_geo_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts_for_jurisdiction_geo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associated Court for given Jurisdiction Geo.
        api_response = api_instance.get_courts_for_jurisdiction_geo(jurisdiction_geo_id, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts_for_jurisdiction_geo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jurisdiction_geo_id** | **str**| jurisdictionGeoId |
 **page_number** | **int**| Page number. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| Sort field. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Sort order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtResponse**](CourtResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courts_service_status**
> CourtServiceStatusResponse get_courts_service_status()

Court Service Status Object.

Retrieve the status of one or more courts using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.court_service_status_response import CourtServiceStatusResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "courtServiceStatusId: "CTSSf45fd1bd792e97"" # str | The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Court Service Status Object.
        api_response = api_instance.get_courts_service_status(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_courts_service_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**CourtServiceStatusResponse**](CourtServiceStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_judge_type**
> JudgeType get_judge_type(judge_type_id)

Judge Type Object for the given judgeTypeId.

Retrieve the specified judge type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.judge_type import JudgeType
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    judge_type_id = "JGTPkwrfzkDJUvxpN9" # str | The judgeTypeId of the desired judge type.

    # example passing only required values which don't have defaults set
    try:
        # Judge Type Object for the given judgeTypeId.
        api_response = api_instance.get_judge_type(judge_type_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_judge_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **judge_type_id** | **str**| The judgeTypeId of the desired judge type. |

### Return type

[**JudgeType**](JudgeType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_judge_types**
> JudgeTypeResponse get_judge_types()

Judge Type Object.

Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.judge_type_response import JudgeTypeResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "judgeTypeId: "JGTPkwrfzkDJUvxpN9"" # str | The keyword expression targeting the judge type.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Judge Type Object.
        api_response = api_instance.get_judge_types(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_judge_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the judge type.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**JudgeTypeResponse**](JudgeTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jurisdiction_geo**
> JurisdictionGeo get_jurisdiction_geo(jurisdiction_geo_id)

Jurisdiction Geo Object for given Jurisdiction Geo Id.

Retrieve the specified jurisdiction geography. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.jurisdiction_geo import JurisdictionGeo
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    jurisdiction_geo_id = "JUGO8s7HvM84dLvVMu" # str | The jurisdictionGeoId value of the desired jurisdiction geography.

    # example passing only required values which don't have defaults set
    try:
        # Jurisdiction Geo Object for given Jurisdiction Geo Id.
        api_response = api_instance.get_jurisdiction_geo(jurisdiction_geo_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_jurisdiction_geo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jurisdiction_geo_id** | **str**| The jurisdictionGeoId value of the desired jurisdiction geography. |

### Return type

[**JurisdictionGeo**](JurisdictionGeo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jurisdiction_geo_for_court**
> JurisdictionGeoResponse get_jurisdiction_geo_for_court(court_id)

Jurisdiction Geo Objects for given courtId.

Retrieve the jurisdiction geography object for the specified court. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.jurisdiction_geo_response import JurisdictionGeoResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    court_id = "CORThSxcef8eGUSkuC" # str | The courtId value of the target court.
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "state" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "state"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Jurisdiction Geo Objects for given courtId.
        api_response = api_instance.get_jurisdiction_geo_for_court(court_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_jurisdiction_geo_for_court: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Jurisdiction Geo Objects for given courtId.
        api_response = api_instance.get_jurisdiction_geo_for_court(court_id, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_jurisdiction_geo_for_court: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_id** | **str**| The courtId value of the target court. |
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "state"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**JurisdictionGeoResponse**](JurisdictionGeoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jurisdictions_geo**
> JurisdictionGeoResponse get_jurisdictions_geo()

Jurisdiction Geo Object.

Retrieve one or more jurisdiction geographies using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.jurisdiction_geo_response import JurisdictionGeoResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "jurisdictionGeoId:"JUGO8s7HvM84dLvVMu"" # str | The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "state" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "state"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Jurisdiction Geo Object.
        api_response = api_instance.get_jurisdictions_geo(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_jurisdictions_geo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "state"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**JurisdictionGeoResponse**](JurisdictionGeoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_role**
> PartyRole get_party_role(party_role_id)

Party Role Object.

Retrieve the specified party role. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.party_role import PartyRole
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    party_role_id = "PTYRVRgMKueGmhnxRN" # str | The partyRoleId value of the desired party role.

    # example passing only required values which don't have defaults set
    try:
        # Party Role Object.
        api_response = api_instance.get_party_role(party_role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_party_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_role_id** | **str**| The partyRoleId value of the desired party role. |

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_role_group**
> PartyRoleGroup get_party_role_group(party_role_group_id)

Party Role Group Object.

Retrieve the specified party role group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.party_role_group import PartyRoleGroup
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    party_role_group_id = "PTYGBnjxbx6tKNfVEP" # str | The partyRoleGroupId value of the desired party role group.

    # example passing only required values which don't have defaults set
    try:
        # Party Role Group Object.
        api_response = api_instance.get_party_role_group(party_role_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_party_role_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_role_group_id** | **str**| The partyRoleGroupId value of the desired party role group. |

### Return type

[**PartyRoleGroup**](PartyRoleGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Returned if the resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_role_groups**
> PartyRoleGroupResponse get_party_role_groups()

Party Role Group Object.

Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.party_role_group_response import PartyRoleGroupResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "partyRoleGroupId: "PTYGBnjxbx6tKNfVEP"" # str | The keyword expression targeting the desired party role group.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Party Role Group Object.
        api_response = api_instance.get_party_role_groups(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_party_role_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired party role group.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**PartyRoleGroupResponse**](PartyRoleGroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_roles**
> PartyRoleResponse get_party_roles()

Party Role Object.

Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import court_standards_api
from openapi_client.model.exception import Exception
from openapi_client.model.party_role_response import PartyRoleResponse
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
    api_instance = court_standards_api.CourtStandardsApi(api_client)
    q = "partyRoleId: "PTYRVRgMKueGmhnxRN"" # str | The keyword expression targeting the desired party role.</a>  (optional)
    page_number = 1 # int | The page number of the results to be retrieved. - minimum: 1 - maximum: 100  (optional)
    sort = "name" # str | The field according to which search results are to be sorted. (optional) if omitted the server will use the default value of "name"
    order = "asc" # str | Whether search results are to be shown in ascending or descending order. (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Party Role Object.
        api_response = api_instance.get_party_roles(q=q, page_number=page_number, sort=sort, order=order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CourtStandardsApi->get_party_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The keyword expression targeting the desired party role.&lt;/a&gt;  | [optional]
 **page_number** | **int**| The page number of the results to be retrieved. - minimum: 1 - maximum: 100  | [optional]
 **sort** | **str**| The field according to which search results are to be sorted. | [optional] if omitted the server will use the default value of "name"
 **order** | **str**| Whether search results are to be shown in ascending or descending order. | [optional] if omitted the server will use the default value of "asc"

### Return type

[**PartyRoleResponse**](PartyRoleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Returned if the request is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

