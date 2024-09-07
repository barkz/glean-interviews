# GetCollectionRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The ID of the Collection to be retrieved. | 
**WithItems** | **Boolean** | Whether or not to include the Collection Items in this Collection. Only request if absolutely required, as this is expensive. | [optional] 
**WithHierarchy** | **Boolean** | Whether or not to include the top level Collection in this Collection&#39;s hierarchy. | [optional] 
**AllowedDatasource** | **String** | The datasource allowed in the Collection returned. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetCollectionRequest = Initialize-PSOpenAPIToolsGetCollectionRequest  -Id null `
 -WithItems null `
 -WithHierarchy null `
 -AllowedDatasource null
```

- Convert the resource to JSON
```powershell
$GetCollectionRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

