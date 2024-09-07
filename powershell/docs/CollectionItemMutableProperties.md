# CollectionItemMutableProperties
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The optional name of the Collection item. | [optional] 
**Description** | **String** | A helpful description of why this CollectionItem is in the Collection that it&#39;s in. | [optional] 
**Icon** | **String** | The emoji icon for this CollectionItem. Only used for Text type items. | [optional] 

## Examples

- Prepare the resource
```powershell
$CollectionItemMutableProperties = Initialize-PSOpenAPIToolsCollectionItemMutableProperties  -Name null `
 -Description null `
 -Icon null
```

- Convert the resource to JSON
```powershell
$CollectionItemMutableProperties | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

