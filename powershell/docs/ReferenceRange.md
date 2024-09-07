# ReferenceRange
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TextRange** | [**TextRange**](TextRange.md) |  | 
**Snippets** | [**SearchResultSnippet[]**](SearchResultSnippet.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ReferenceRange = Initialize-PSOpenAPIToolsReferenceRange  -TextRange null `
 -Snippets null
```

- Convert the resource to JSON
```powershell
$ReferenceRange | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

