# DocumentSpec
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **String** | The URL of the document. | [optional] 
**Id** | **String** | The ID of the document. | [optional] 
**UgcType** | **String** | The type of the user generated content (UGC datasource). | [optional] 
**ContentId** | **Int32** | The id for user generated content. | [optional] 
**DocType** | **String** | The specific type of the user generated content type. | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentSpec = Initialize-PSOpenAPIToolsDocumentSpec  -Url null `
 -Id null `
 -UgcType null `
 -ContentId null `
 -DocType null
```

- Convert the resource to JSON
```powershell
$DocumentSpec | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

