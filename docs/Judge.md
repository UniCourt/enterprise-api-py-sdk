# Judge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judge_id** | **str** | ID for the judge in this case. This ID is unique within a case and NOT across cases. If the same Judge were to appear in another case this ID would be different. | 
**name** | **str** | Name of the judge as provided by Court. | 
**name_prefix** | **str, none_type** |  | 
**first_name** | **str, none_type** | First name of the judge. This is normalized by UniCourt. | 
**middle_name** | **str, none_type** | Middle name of the judge. This is normalized by UniCourt. | 
**last_name** | **str, none_type** | Last name of the judge. This is normalized by UniCourt. | 
**name_suffix** | **str, none_type** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**judge_type** | [**JudgeType**](JudgeType.md) |  | 
**source_judge_type** | **str** |  | 
**is_visible** | **bool** | Signifies if the judge as this judge type is currently isVisible or not for the case. | 
**first_fetch_date** | **datetime** | When was the judge first fetched from the court site. | 
**last_fetch_date** | **datetime** | When was the judge last fetched from the court site. | 
**possible_norm_judge_array** | [**[PossibleNormJudge]**](PossibleNormJudge.md) |  | 
**object** | **str** | Name of the object | defaults to "Judge"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


