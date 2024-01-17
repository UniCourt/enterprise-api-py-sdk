# DailyUsageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_start_time** | **datetime** | Start time of the usage. | 
**usage_end_time** | **datetime** | End time of the usage. | 
**api_usage** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Api Usage made in real time. | 
**api_calls_made** | [**BillingCycleUsageResponseApiCallsMade**](BillingCycleUsageResponseApiCallsMade.md) |  | 
**api_calls_credited** | [**BillingCycleUsageResponseApiCallsCredited**](BillingCycleUsageResponseApiCallsCredited.md) |  | 
**api_calls_billable** | [**BillingCycleUsageResponseApiCallsBillable**](BillingCycleUsageResponseApiCallsBillable.md) |  | 
**object** | **str** | Name of the object. | defaults to "DailyUsageResponse"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


