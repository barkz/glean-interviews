# ListCollectionsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IncludeAudience** | **Boolean** | Whether to include the audience filters with the listed Collections. | [optional] 
**IncludeRoles** | **Boolean** | Whether to include the editor roles with the listed Collections. | [optional] 
**AllowedDatasource** | **String** | The datasource type this Collection can hold. ANSWERS - for Collections representing answer boards | [optional] 

## Examples

- Prepare the resource
```powershell
$ListCollectionsRequest = Initialize-PSOpenAPIToolsListCollectionsRequest  -IncludeAudience null `
 -IncludeRoles null `
 -AllowedDatasource null
```

- Convert the resource to JSON
```powershell
$ListCollectionsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

