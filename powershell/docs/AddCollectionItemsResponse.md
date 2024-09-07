# AddCollectionItemsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Collection** | [**Collection**](Collection.md) |  | [optional] 
**VarError** | [**AddCollectionItemsError**](AddCollectionItemsError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$AddCollectionItemsResponse = Initialize-PSOpenAPIToolsAddCollectionItemsResponse  -Collection null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$AddCollectionItemsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

