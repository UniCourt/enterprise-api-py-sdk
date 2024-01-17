# DocketEntrySecondaryDocuments

Secondary Documents refers to documents that are attached to a docket entry. Secondary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the secondary document is one which is attached in the docket entry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Page number for which results where obtained. | 
**case_document_array** | [**[CaseDocument]**](CaseDocument.md) |  | 
**next_page_api** | **str, none_type** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case. entity in a Case. | 
**object** | **str** | Name of the object | defaults to "DocketEntrySecondaryDocuments"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


