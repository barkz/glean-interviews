# GetDocumentsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Documents** | [**System.Collections.Hashtable**](DocumentOrError.md) | The document details or the error if document is not found. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDocumentsResponse = Initialize-PSOpenAPIToolsGetDocumentsResponse  -Documents null
```

- Convert the resource to JSON
```powershell
$GetDocumentsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

