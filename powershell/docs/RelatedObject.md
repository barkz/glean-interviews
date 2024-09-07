# RelatedObject
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | The ID of the related object | 
**Metadata** | [**RelatedObjectMetadata**](RelatedObjectMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$RelatedObject = Initialize-PSOpenAPIToolsRelatedObject  -Id null `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$RelatedObject | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

