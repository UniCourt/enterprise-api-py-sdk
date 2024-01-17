# SourceCharge

Source charge data from the source site.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_charge_raw** | **str** | Raw charge data from the source site. | 
**source_charge** | **str, none_type** | Charge data from the source site. | 
**is_visible** | **bool** | Signifies if the charge is currently isVisible or not for the case. | 
**source_statute** | **str, none_type** | Statute of a charge. | 
**source_charge_degree** | **str, none_type** | Charge degree data from the source site. | 
**source_charge_severity** | **str, none_type** | Charge severity data from the source site. | 
**source_charge_additional_data_array** | [**[SourceChargeAdditionalData]**](SourceChargeAdditionalData.md) | Additional data related to the charge which is available in the source site. | 
**first_fetch_date** | **str** | When this charge was first fetched from the court site. | 
**last_fetch_date** | **str** | When this charge was last fetched from the court site. | 
**object** | **str** | Name of the object | defaults to "SourceCharge"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


