# ServiceStatusDownDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | This field determines the reason behind status being down. Following are the possible reason for the service to be down:   underMaintenance: It means that the site is under scheduled maintenance.   notIntegrated: When an court with specific case type is not integrated in UniCourt.   brokenIntegration: Due to some updates made to the court site our existing Integration has broken and will require a fix to be made to support this court again for a spcific case type category.   sourceMigrated: When a source is migrated from one site to another for a specific case type category. | 
**details** | **str, none_type** | Details of the reason. | 
**eta** | **str, none_type** | Estimated Time this Service could be Up again for the use. | 
**object** | **str** | Name of the object | defaults to "ServiceStatusDownDetails"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


