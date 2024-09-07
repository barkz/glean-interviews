# PreviewStructuredTextResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StructuredText** | [**StructuredText**](StructuredText.md) |  | 
**DocsInaccessibleToUser** | **String[]** | A list of links the user doesn&#39;t have access to. | [optional] 
**CombinedAnswerText** | [**StructuredText**](StructuredText.md) |  | 

## Examples

- Prepare the resource
```powershell
$PreviewStructuredTextResponse = Initialize-PSOpenAPIToolsPreviewStructuredTextResponse  -StructuredText null `
 -DocsInaccessibleToUser null `
 -CombinedAnswerText null
```

- Convert the resource to JSON
```powershell
$PreviewStructuredTextResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

