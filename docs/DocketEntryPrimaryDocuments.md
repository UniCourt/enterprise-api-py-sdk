# DocketEntryPrimaryDocuments

Primary Documents refers to documents that are directly related to a docket entry. Primary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the primary document is one which is attached to the docket number. Because in district for a primary document it can have many attachments associatated to it. PACER Appeal Courts - Here the attachments for a docket entry are the primary documents. Because in appeal for those attachments there is no primary documents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Page number for which results where obtained. | 
**case_document_array** | [**[CaseDocument]**](CaseDocument.md) |  | 
**next_page_api** | **str, none_type** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case. entity in a Case. | 
**object** | **str** | Name of the object | defaults to "DocketEntryPrimaryDocuments"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


