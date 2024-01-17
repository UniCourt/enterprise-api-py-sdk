# CaseUpdatePacerOptionsAdditionalPageArrayInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **str** |  | [optional] 
**fetch_if_older_than_days** | **int** | You can limit how often this page information is fetched to reduce your PACER fees.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that this page is fetched from PACER for this case update irrespective of when the page was last fetched. 2.  Specifying a value of 30 ensures that this page is fetched from PACER for this case update only if the last fetch was older than 30 days.  | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


