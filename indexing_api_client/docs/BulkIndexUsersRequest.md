# BulkIndexUsersRequest

Describes the request body for the /bulkindexusers API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload\_id** | **str** | Unique id that must be used for this instance of datasource users upload | 
**datasource** | **str** | datasource of the users | 
**users** | [**[DatasourceUserDefinition]**](DatasourceUserDefinition.md) | batch of users for the datasource | 
**is\_first\_page** | **bool** | true if this is the first page of the upload. Defaults to false | [optional] 
**is\_last\_page** | **bool** | true if this is the last page of the upload. Defaults to false | [optional] 
**force\_restart\_upload** | **bool** | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage&#x3D;true | [optional] 
**disable\_stale\_data\_deletion\_check** | **bool** | True if older user data needs to be force deleted after the upload completes. Defaults to older data being deleted only if the percentage of data being deleted is less than a reasonable threshold. This must only be set when &#x60;isLastPage &#x3D; true&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


