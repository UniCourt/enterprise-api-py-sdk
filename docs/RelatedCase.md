# RelatedCase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str, none_type** | Case ID of the related Case. This can be null if this case in not found in our database. However the meta information of the related case will be present. | 
**case_number** | **str** | Case Number of the related Case. | 
**case_name** | **str, none_type** | Case Name of the related Case. | 
**case_relationship_type** | [**CaseRelationshipType**](CaseRelationshipType.md) |  | 
**source_case_relationship_type** | **str** | Case Relationship Type provided by court. | 
**is_visible** | **bool** | This specifies if the related cases is still related to the parent case or not. | 
**additional_source_data** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**case_api** | **str, none_type** | Link to the Case API of the current related case. | 
**object** | **str** | Name of the object | defaults to "RelatedCase"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


