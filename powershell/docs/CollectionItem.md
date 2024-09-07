# CollectionItem
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The optional name of the Collection item. | [optional] 
**Description** | **String** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**Icon** | **String** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 
**CollectionId** | **Int32** | The Collection ID of the Collection that this CollectionItem belongs in. | 
**DocumentId** | **String** | If this CollectionItem is indexed, the Glean Document ID of that document. | [optional] 
**Url** | **String** | The URL of this CollectionItem. | [optional] 
**ItemId** | **String** | Unique identifier for the item within the Collection it belongs to. | [optional] 
**CreatedBy** | [**Person**](Person.md) |  | [optional] 
**CreatedAt** | **System.DateTime** | Unix timestamp for when the item was first added (in seconds since epoch UTC). | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**Shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**Collection** | [**Collection**](Collection.md) |  | [optional] 
**ItemType** | **String** |  | 

## Examples

- Prepare the resource
```powershell
$CollectionItem = Initialize-PSOpenAPIToolsCollectionItem  -Name null `
 -Description null `
 -Icon null `
 -CollectionId null `
 -DocumentId null `
 -Url null `
 -ItemId null `
 -CreatedBy null `
 -CreatedAt null `
 -Document null `
 -Shortcut null `
 -Collection null `
 -ItemType null
```

- Convert the resource to JSON
```powershell
$CollectionItem | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

