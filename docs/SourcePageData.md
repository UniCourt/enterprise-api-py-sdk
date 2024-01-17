# SourcePageData

Source data from different pages in the court website.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_name** | **str** | Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases. | 
**additional_source_data** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**first_fetch_date** | **str** | When was the page first fetched from the court site. | 
**last_fetch_date** | **str** | When was the page last fetched from the court site. | 
**object** | **str** | Name of the object | defaults to "SourcePageData"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


