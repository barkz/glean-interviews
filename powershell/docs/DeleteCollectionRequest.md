# DeleteCollectionRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **Int32[]** | The IDs of the Collections to delete. | 
**AllowedDatasource** | **String** | The datasource allowed in the Collection to be deleted. | [optional] 

## Examples

- Prepare the resource
```powershell
$DeleteCollectionRequest = Initialize-PSOpenAPIToolsDeleteCollectionRequest  -Ids null `
 -AllowedDatasource null
```

- Convert the resource to JSON
```powershell
$DeleteCollectionRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

