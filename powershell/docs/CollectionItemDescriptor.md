# CollectionItemDescriptor
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **String** | The URL of the item being added. | [optional] 
**DocumentId** | **String** | The Glean Document ID of the item being added if it&#39;s an indexed document. | [optional] 
**NewNextItemId** | **String** | The (optional) ItemId of the next CollectionItem in sequence. If omitted, will be added to the end of the Collection | [optional] 
**ItemType** | **String** |  | [optional] 
**Name** | **String** | The optional name of the Collection item. | [optional] 
**Description** | **String** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**Icon** | **String** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Examples

- Prepare the resource
```powershell
$CollectionItemDescriptor = Initialize-PSOpenAPIToolsCollectionItemDescriptor  -Url null `
 -DocumentId null `
 -NewNextItemId null `
 -ItemType null `
 -Name null `
 -Description null `
 -Icon null
```

- Convert the resource to JSON
```powershell
$CollectionItemDescriptor | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

