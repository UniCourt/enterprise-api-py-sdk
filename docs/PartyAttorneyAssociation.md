# PartyAttorneyAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_attorney_association_id** | **str** | ID of the association | 
**attorney_id** | **str** | ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**party_id** | **str** | ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**is_visible** | **bool** | Signifies if this party attorney relationship is currently isVisible or not for the case. | 
**object** | **str** | Name of the object | defaults to "PartyAttorneyAssociation"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


