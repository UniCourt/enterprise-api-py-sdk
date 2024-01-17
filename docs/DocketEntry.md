# DocketEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_order** | **int** | Order number how the dockets have stored in UniCourt. | 
**docket_entry_date** | **datetime** | Docket Action Date | 
**docket_number** | **int, none_type** | The respective docket entry number which is defined in the court website. | 
**docket_badge** | **str** | Docket Badge helps you to know what type of a docket entry it is. | 
**text** | **str** | Source Docket Entry | 
**text_structured** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**referenced_docket_number_array** | [**[ReferencedDocketNumber]**](ReferencedDocketNumber.md) | Other Docket Numbers that referenced for a particular docket entry. | 
**docket_entry_primary_documents** | [**DocketEntryPrimaryDocuments**](DocketEntryPrimaryDocuments.md) |  | 
**docket_entry_secondary_documents** | [**DocketEntrySecondaryDocuments**](DocketEntrySecondaryDocuments.md) |  | 
**last_fetch_date** | **str** | When this docket entry was last fetched from the source. | 
**boundary** | **str, none_type** | Determines if it is the first docket entry or the last docket entry. This value will be set only for the first and last docket entry. For other docket entries it will be null. However, this will be set as single_docket_entry when the Case contains only one docket entry. | 
**object** | **str** | Name of the object | defaults to "DocketEntry"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


