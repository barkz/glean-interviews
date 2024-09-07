# DocumentSpecOneOf2
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UgcType** | **String** | The type of the user generated content (UGC datasource). | [optional] 
**ContentId** | **Int32** | The id for user generated content. | [optional] 
**DocType** | **String** | The specific type of the user generated content type. | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentSpecOneOf2 = Initialize-PSOpenAPIToolsDocumentSpecOneOf2  -UgcType null `
 -ContentId null `
 -DocType null
```

- Convert the resource to JSON
```powershell
$DocumentSpecOneOf2 | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

