# Address

Address object Data Schema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_address1** | **str, none_type** | 1st part of the street address. | 
**street_address2** | **str, none_type** | 2nd part of the street address. | 
**city** | **str, none_type** | City | 
**state_code** | **str, none_type** | State Code if the state is a US state else contains null. | 
**country_code** | **str, none_type** | ISO 3166-1 alpha-3 (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements). Code of the country if country name is present. | 
**zip** | **str, none_type** | Zip code of the address. | 
**zip4** | **str, none_type** | 4 digit extension of the zip code if the address is a US address. | 
**is_visible** | **bool** | Boolean indicating if the address is visible or not. | 
**first_fetch_date** | **datetime** | Date at which this record is created in UniCourt. | 
**last_fetch_date** | **datetime** | Date at which this record was updated in UniCourt. | 
**latitude** | **float, none_type** | Coordinates at geographic coordinate system. | 
**longitude** | **float, none_type** | Coordinates at geographic coordinate system. | 
**object** | **str** |  | defaults to "Address"
**state_name** | **str** | State Name if present else default value. | defaults to "UNKNOWN"
**country_name** | **str** | Country Name if present else default value. | defaults to "UNKNOWN"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


