# MigrateShortcutsRequest

Describes the request body of the /migrateshortcuts API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload\_id** | **str** | Unique id that must be used for this bulk upload instance | 
**shortcuts** | [**[Shortcut]**](Shortcut.md) | Batch of shortcuts information | 
**is\_first\_page** | **bool** | true if this is the first page of the upload. Defaults to false | [optional] 
**is\_last\_page** | **bool** | true if this is the last page of the upload. Defaults to false | [optional] 
**force\_restart\_upload** | **bool** | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage&#x3D;true | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


