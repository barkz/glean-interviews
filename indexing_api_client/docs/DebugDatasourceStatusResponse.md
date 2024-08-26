# DebugDatasourceStatusResponse

Describes the response body of the /debug/{datasource}/status API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**DebugDatasourceStatusResponseDocuments**](DebugDatasourceStatusResponseDocuments.md) |  | [optional] 
**identity** | [**DebugDatasourceStatusResponseIdentity**](DebugDatasourceStatusResponseIdentity.md) |  | [optional] 
**datasource\_visibility** | **str** | The visibility of the datasource, an enum of VISIBLE\_TO\_ALL, VISIBLE\_TO\_TEST\_GROUP, NOT\_VISIBLE | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


