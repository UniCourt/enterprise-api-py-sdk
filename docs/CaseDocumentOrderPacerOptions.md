# CaseDocumentOrderPacerOptions

**Applicable for PACER cases.**

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pacer_user_id** | **str** | Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too. | 
**pacer_client_code** | **str, none_type** | PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


