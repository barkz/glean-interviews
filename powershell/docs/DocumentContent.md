# DocumentContent
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FullTextList** | **String[]** | The plaintext content of the document. | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentContent = Initialize-PSOpenAPIToolsDocumentContent  -FullTextList null
```

- Convert the resource to JSON
```powershell
$DocumentContent | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

