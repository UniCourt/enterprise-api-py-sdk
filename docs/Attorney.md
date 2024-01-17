# Attorney


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attorney_id** | **str** | ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**name** | **str** | Name of the attorney as provided by Court. | 
**name_prefix** | **str, none_type** |  | 
**first_name** | **str, none_type** | First name of the attorney. This is normalized by UniCourt. | 
**middle_name** | **str, none_type** | Middle name of the attorney. This is normalized by UniCourt. | 
**last_name** | **str, none_type** | Last name of the attorney. This is normalized by UniCourt. | 
**name_suffix** | **str, none_type** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**attorney_law_firm_array** | [**[AttorneyLawFirm]**](AttorneyLawFirm.md) |  | 
**bar_number** | **str, none_type** | The bar enrollment number of an attorney. | 
**attorney_type** | [**AttorneyType**](AttorneyType.md) |  | 
**source_attorney_type** | **str** | Attorney Type as provided by Court. | 
**is_visible** | **bool** | Signifies if the attorney as this attorney type is currently isVisible or not for the case. | 
**first_fetch_date** | **datetime** | When was the attorney first fetched from the court site. | 
**last_fetch_date** | **datetime** | When was the attorney last fetched from the court site. | 
**party_attorney_associations** | [**PartyAttorneyAssociations**](PartyAttorneyAssociations.md) |  | 
**possible_norm_attorney_array** | [**[PossibleNormAttorney]**](PossibleNormAttorney.md) |  | 
**possible_norm_law_firm_array** | [**[PossibleNormLawFirm]**](PossibleNormLawFirm.md) | Possible Norm Lawfirm array for a Attorney. | 
**party_role_group_id_array** | **[str]** | Party Role Group Id for a Attorney. | 
**party_role_id_array** | **[str]** | Party Role Id for a Attorney. | 
**object** | **str** | Name of the object | defaults to "Attorney"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


