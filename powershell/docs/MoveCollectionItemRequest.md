# MoveCollectionItemRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CollectionId** | **Int32** | The ID of the Collection to move items in. | 
**ItemId** | **String** | The item ID of the item being moved. | 
**NewNextItemId** | **String** | The (optional) item ID of the item that is the new next of itemId, or empty if this is now the last item. This item does not move, it&#39;s used as a reference position to put the itemId in the right position. | [optional] 

## Examples

- Prepare the resource
```powershell
$MoveCollectionItemRequest = Initialize-PSOpenAPIToolsMoveCollectionItemRequest  -CollectionId null `
 -ItemId null `
 -NewNextItemId null
```

- Convert the resource to JSON
```powershell
$MoveCollectionItemRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

