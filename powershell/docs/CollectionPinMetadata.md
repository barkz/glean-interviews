# CollectionPinMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The ID of the Collection. | 
**Target** | [**CollectionPinTarget**](CollectionPinTarget.md) |  | 

## Examples

- Prepare the resource
```powershell
$CollectionPinMetadata = Initialize-PSOpenAPIToolsCollectionPinMetadata  -Id null `
 -Target null
```

- Convert the resource to JSON
```powershell
$CollectionPinMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

