# DeleteCollectionItemRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CollectionId** | **Decimal** | The ID of the Collection to remove an item in. | 
**ItemId** | **String** | The item ID of the CollectionItem to remove from this Collection. | 
**DocumentId** | **String** | The (optional) Glean Document ID of the CollectionItem to remove from this Collection if this is an indexed document. | [optional] 

## Examples

- Prepare the resource
```powershell
$DeleteCollectionItemRequest = Initialize-PSOpenAPIToolsDeleteCollectionItemRequest  -CollectionId null `
 -ItemId null `
 -DocumentId null
```

- Convert the resource to JSON
```powershell
$DeleteCollectionItemRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

