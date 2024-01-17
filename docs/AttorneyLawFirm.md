# AttorneyLawFirm

Name of the attorney's law firm as provided by Court. This can be null as some Courts do not provide this as a separate field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attorney_law_firm_id** | **str, none_type** | ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**name** | **str** | Name of the law firm as provided by Court. | 
**is_visible** | **bool** | Signifies if the attorney as this attorney type is currently isVisible or not for the case. | 
**first_fetch_date** | **str** | Is the date when the document was first fetched from the court site. | 
**last_fetch_date** | **str** | Is the date when the document was last fetched from the court site. | 
**object** | **str** | Name of the object | defaults to "AttorneyLawFirm"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


