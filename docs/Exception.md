# Exception

Exception object contains specific error code and its message related to the API request validation error or error occurred during API request processing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Indicates the type of error occured. | 
**message** | **str** | Indicates the error message that describes the error code. | 
**details** | **str** | Describes what went wrong. | 
**object** | **str** |  | defaults to "Exception"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


