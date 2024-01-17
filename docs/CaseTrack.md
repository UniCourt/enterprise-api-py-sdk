# CaseTrack


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** | Unique Id for a Case in UniCourt. | 
**pacer_options** | [**CaseUpdatePacerOptionsResponse**](CaseUpdatePacerOptionsResponse.md) |  | 
**schedule** | [**Schedule**](Schedule.md) |  | 
**last_tracked_details** | [**LastTrackedDetails**](LastTrackedDetails.md) |  | 
**last_fetch_date** | **datetime, none_type** | The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist. | 
**last_fetch_date_with_updates** | **datetime, none_type** | The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, | 
**case_api** | **str** |  | 
**case** | [**Case**](Case.md) |  | 
**object** | **str** | Name of the object. | defaults to "CaseTrack"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


