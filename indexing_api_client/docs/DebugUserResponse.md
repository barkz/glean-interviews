# DebugUserResponse

Describes the response body of the /debug/{datasource}/user API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **UserStatusResponse** |  | [optional] 
**uploaded\_groups** | [**[DatasourceGroupDefinition]**](DatasourceGroupDefinition.md) | List of groups the user is a member of, as uploaded via permissions API. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


