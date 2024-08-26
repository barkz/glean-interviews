# DatasourceProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | The datasource the profile is of. | 
**handle** | **str** | The display name of the entity in the given datasource. | 
**url** | **str** | URL to view the entity&#39;s profile. | [optional] 
**native\_app\_url** | **str** | A deep link, if available, into the datasource&#39;s native application for the entity&#39;s platform (i.e. slack://...). | [optional] 
**is\_user\_generated** | **bool** | For internal use only. True iff the data source profile was manually added by a user from within Glean (aka not from the original data source) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


