# GeneratedAttachmentContent
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DisplayHeader** | **String** | The header describing the generated content. | [optional] 
**Text** | **String** | The content that has been generated. | [optional] 

## Examples

- Prepare the resource
```powershell
$GeneratedAttachmentContent = Initialize-PSOpenAPIToolsGeneratedAttachmentContent  -DisplayHeader null `
 -Text null
```

- Convert the resource to JSON
```powershell
$GeneratedAttachmentContent | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

