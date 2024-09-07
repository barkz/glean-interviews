# AddCollectionItemsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CollectionId** | **Decimal** | The ID of the Collection to add items to. | 
**AddedCollectionItemDescriptors** | [**CollectionItemDescriptor[]**](CollectionItemDescriptor.md) | The CollectionItemDescriptors of the items being added. | [optional] 

## Examples

- Prepare the resource
```powershell
$AddCollectionItemsRequest = Initialize-PSOpenAPIToolsAddCollectionItemsRequest  -CollectionId null `
 -AddedCollectionItemDescriptors null
```

- Convert the resource to JSON
```powershell
$AddCollectionItemsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

