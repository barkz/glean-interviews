# EditCollectionItemRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CollectionId** | **Int32** | The ID of the Collection to edit CollectionItems in. | 
**ItemId** | **String** | The ID of the CollectionItem to edit. | 
**Name** | **String** | The optional name of the Collection item. | [optional] 
**Description** | **String** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**Icon** | **String** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Examples

- Prepare the resource
```powershell
$EditCollectionItemRequest = Initialize-PSOpenAPIToolsEditCollectionItemRequest  -CollectionId null `
 -ItemId null `
 -Name null `
 -Description null `
 -Icon null
```

- Convert the resource to JSON
```powershell
$EditCollectionItemRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

