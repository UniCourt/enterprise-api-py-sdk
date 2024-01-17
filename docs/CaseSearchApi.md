# openapi_client.CaseSearchApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_cases**](CaseSearchApi.md#search_cases) | **GET** /caseSearch | Case search.
[**search_cases_by_id**](CaseSearchApi.md#search_cases_by_id) | **GET** /caseSearch/{caseSearchId} | Case search results for a given caseSearchId.


# **search_cases**
> CaseSearchResponse search_cases(q)

Case search.

This endpoint retrieves cases according to keyword expressions you provide. <br> Keyword expressions are constructed according to the rules described below. <br><br> This API supports multiple use cases:    - Search for multiple keywords  `Google OR Facebook`.   - Search within particular attributes.   - Relational search using terms and connectors.   - And much more. ----  ## Allowed Connectors in Keyword Expressions | Connector | Description  | Example | | ------| ------|------| | **AND** |Find cases containing each of the terms joined by AND connectors.|**personal AND injury**| | **OR**  |Find cases containing any of the terms joined by OR connectors.|**order OR decision**| | **NOT** |Find cases that do not contain the specified term.|**personal AND NOT injury**.  Find cases with the word “personal” and not “injury”.| | **“[phrase]”** |Find the exact phrase placed between the quotation marks.|**\"personal injury”**| | **~**  |Find cases in which the specified words appear near each other. For example, \"personal injury\" ~ 5 targets cases in which the word \"personal\" appears within 5 words of the word \"injury\".|**“personal injury” ~ 5** - Find cases with “personal” within five words of “injury”. | | **( … )** |Specifies the order in which connectors are to be appliied in a keyword expression.| **personal AND (injury OR fall)** - Find cases with the word personal injury or personal fall.|  <br><br> ## Fields and Connectors Searching | Filed | Description  | Example | | ------| ------|------| |**caseNumber** |Find cases with the specified case number (i.e., docket number).| **caseNumber:\"2020-L-007212\"** - Find cases whose case number matches given case number number.| |**caseName** |Find cases with the specified case title.| **caseName:\"THOMAS P. CARNEY, INC. VS BEHLER JAMES Et Al\"** - Find cases whose case name matches given terms.| |**Court**|Find cases in the specified court.|**(Court:(name:(New York)))** - Find cases in New York state.<br>| |**CaseStatus**|Find cases witih the specified case status.|**(CaseStatus:(name:Disposed))** - All disposed cases.<br>| |**CaseType**|Find cases of the specified case type. | **(CaseType:(name:Property))** - Cases with case type “property”.| |**Party** | Find cases involving the specified party.| **(Party:(name:Apple))** - Find cases involving Apple. | |**partyId**|Find cases involving a party with the specified partyId value.|**(Party:(partyId:\"PRTYgu1ffe866484c2\"))**| |**PartyRole** | Find cases in which at least one party has the specified party role. | **(Party:((PartyRole:(name:\"plaintiff\"))))** - Find cases with party role “plaintiff”.<br><br> **(Party:((PartyRole:(name:defendant)) AND (AttorneyRepresentationType:(name:(Attorney represented)))))** - Find cases where a party is acting as defendant and represented by an attorney.| |**AttorneyRepresentationType**| Find cases in which at least one party has the specified attorney representation type.|**(Party:(AttorneyRepresentationType:(name:\"attorney represented\")))** - Find cases where a party is represented by an attorney. | |**Attorney** | Find cases involving the specified attorney. | **(Attorney:(name:\"David Boies\"))** - Find cases involving the attorney David Boies. | |**AttorneyType**|Find cases involving at least one attorney of the specified attorney type.|**(Attorney:((AttorneyType:(name:\"Lead Attorney\"))))**| |**Judge** |Find cases involving the specified judge. | **(Judge:(name:\"Posner\"))** - Find cases involving Judge Posner.| |**JudgeType**|Find cases involving at least one judge of the specified judge type.|**(Judge:((JudgeType:(name:\"Magistrate\"))))**| |**CaseStats**|Find cases with the specified case statistics.|**(CaseStats:(partyCount:[10 TO 100]))** - Find cases involving 10 to 100 parties.<br>**(CaseStats:(attorneyCount:[2 TO 40]))** - Find cases involving 2 to 40 attorneys.<br>**(CaseStats:(judgeCount:[\\* TO 2]))** - Find cases involving up to 2 judges. <br>**(CaseStats:(docketEntryCount:[10 TO 100]))** - Find cases having 10 to 100 docket_entries. <br>**(CaseStats:(allCaseDocumentCount:[10 TO 100]))** - Find cases having 10 to 100 documents. | |**filedDate** | Find cases that were filed on the specified date or within the specified date range. | **filedDate:[2020-03-15 TO 2021-12-01]** - Find the most recently filed cases between March 15, 2020 and December 1, 2021 (inclusive). | |**lastFetchDate**| Find cases in which UniCourt last checked for updates on the specified date or within the specified date range. |**(lastFetchDate:[now-60d TO \\*\\])** - Find cases that were updated by UniCourt in the last 60 days. | |**lastFetchDateWithUpdates**|Find cases in which UniCourt last detected an update on the specified date or within the specified date range.|**(lastFetchDateWithUpdates:[now-6d TO \\*\\])** - Find cases for the changes found on court site in last 6 days.| |**participantsLastFetchDate**|Find cases in which information cocnerning participants was last updated on the specified date or within the specified date range.|**(participantsLastFetchDate:[now-6d TO \\*\\])** - Find cases where the participant's information was updated in last 6 days.| |**DocketEntry**|Find cases in which at least one docket entry contains the specified text.|**(DocketEntry:(text:(Motion to Compel Responses) AND docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00]))** - Find cases with docket text “Motion to Compel Responses” and action date between 2020-01-01 and 2020-05-01.| |**docketEntryDate**|Find cases in which at least one docket entry was made on the specified date or within the specified date range.|**(DocketEntry:(docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00])) AND (CaseStats:(allCaseDocumentCount:[0 TO 10]))** - Find cases with docket action date between 2020-01-01 and 2020-05-01 having up to 10 documents associated with it.| |**HearingDate**| Find cases with at least one hearing scheduled for the specified date or within the specified date range.|**(Hearing:(hearingDate:[now TO now+10d]))** - Find cases where hearing is scheduled in next 10 days.| |**HearingDate**| Search for cases where hearing is going to happen in 10 to 20days.|**(Hearing:(hearingDate:[now+10d TO now+20d]))** - Find cases where hearing is scheduled in next 10 to 20 days.| |**JurisdictionGeo**|Find cases in which the law of the specified state governs.|**(JurisdictionGeo:(state:\"New York\"))**- Find cases where Jurisdiction is New York state.| |**Party Address Exists**|Find cases with Party addresses.|**(Party:(Contact:(Address:(stateName:\\*))))**- Returns only those cases that have addresses for parties.| |**Document**|Find cases with specific document name and preview is available for the document.|**(CaseDocument:(name:\"civil case cover sheet\" AND isPreviewAvailable:true))**- Returns cases with document civil case cover sheet and preview is available.|  <br><br> --- ## Party Sub Filter Examples |Example |Explanation | |---|---| |**(Party:(name:google AND (PartyRole:(name:\"plaintiff\"))))**|Find cases involving at least one plaintiff whose name contains the term \"Google\".| |**(Party:(name:\"OTELIA PEREIDA\" AND (AttorneyRepresentationType:(name:\"Attorney represented\")))) AND (Attorney:(name:\"Law Offices of Todd M Friedman\"))**|Find cases where the Party is *OTELIA PEREIDA* and is represented by the attorney *Law Offices of Todd M Friedman*.|  --- ### All query parameters supported for this API can be found in below schema section. Schema -->  CaseSearchQueryObject 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_search_api
from openapi_client.model.case_search_response import CaseSearchResponse
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
    api_instance = case_search_api.CaseSearchApi(api_client)
    q = "caseNumber:"JP07-22-DC00026818"" # str | Query parameter for keyword expressions.</a> 
    sort = "filedDate" # str | Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy. (optional) if omitted the server will use the default value of "filedDate"
    order = "desc" # str | Query parameter specifying whether search result are sorted in ascending or descending order. (optional) if omitted the server will use the default value of "desc"
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Case search.
        api_response = api_instance.search_cases(q)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseSearchApi->search_cases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case search.
        api_response = api_instance.search_cases(q, sort=sort, order=order, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseSearchApi->search_cases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query parameter for keyword expressions.&lt;/a&gt;  |
 **sort** | **str**| Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy. | [optional] if omitted the server will use the default value of "filedDate"
 **order** | **str**| Query parameter specifying whether search result are sorted in ascending or descending order. | [optional] if omitted the server will use the default value of "desc"
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**CaseSearchResponse**](CaseSearchResponse.md)

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

# **search_cases_by_id**
> CaseSearchResponse search_cases_by_id(case_search_id)

Case search results for a given caseSearchId.

Retrieve the search results corresponding to the specified caseSearchId value. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import case_search_api
from openapi_client.model.case_search_response import CaseSearchResponse
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
    api_instance = case_search_api.CaseSearchApi(api_client)
    case_search_id = "CSRCU3qFUH8BjLnba5" # str | Case Search information for the given caseSearchId.
    page_number = 1 # int | The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Case search results for a given caseSearchId.
        api_response = api_instance.search_cases_by_id(case_search_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseSearchApi->search_cases_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Case search results for a given caseSearchId.
        api_response = api_instance.search_cases_by_id(case_search_id, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CaseSearchApi->search_cases_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_search_id** | **str**| Case Search information for the given caseSearchId. |
 **page_number** | **int**| The page number of the desired page of results. - Minimum: 1 - Maximum: 1000  | [optional]

### Return type

[**CaseSearchResponse**](CaseSearchResponse.md)

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

