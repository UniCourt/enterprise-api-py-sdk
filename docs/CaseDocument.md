# CaseDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_document_id** | **str** | UniCourt&#39;s Case Document ID. | 
**sort_order** | **int, none_type** | Order of documents how it is being stored in UniCourt. | 
**name** | **str, none_type** | Document name. | 
**description** | **str, none_type** | Description of the document. | 
**document_filed_date** | **str, none_type** | Document Date when it was filed. The document date will be either explicitly provided byt the court or if the document is associatated to a docket entry then the document date will be of docket entry date. | 
**parent_document_id** | **str, none_type** | Document ID which is the parent document for the current document. This will be null if the current document is a parent document. | 
**child_document_id_array** | **[str, none_type]** | List of child document ID&#39;s if exists or else it will be an empty lsit. | 
**pages** | **int, none_type** | Total number of pages in the document. | 
**is_preview_available** | **bool** | Determines if a preview is available for the case document. | 
**preview_document** | [**PreviewDocument**](PreviewDocument.md) |  | 
**price** | **float, none_type** | Price of the document. | 
**in_library** | **bool** | Determines if the document is present in the UniCourt Library or not. | 
**added_to_library_date** | **str, none_type** | Date and time when the document was downloaded and added to the UniCourt Crowd Source Library. | 
**download_api** | **str, none_type** | Link to either view the document if it is downloaded and already present in the UniCourt CrowdSourced Library. | 
**first_fetch_date** | **str** | Is the date when the document was first fetched from the court site. | 
**source_data_status** | **str, none_type** | The status of source data of document. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Document has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site. | 
**object** | **str** | Name of the object | defaults to "CaseDocument"
**estimated_order_duration** | **str** | Estimated duration of a Order. | defaults to "estimateUnavailable"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


