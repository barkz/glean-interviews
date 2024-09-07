# GetDocumentsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentSpecs** | [**DocumentSpec[]**](DocumentSpec.md) | The specification for the documents to be retrieved. | 
**IncludeFields** | **String[]** | List of Document fields to return (that aren&#39;t returned by default) | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDocumentsRequest = Initialize-PSOpenAPIToolsGetDocumentsRequest  -DocumentSpecs null `
 -IncludeFields null
```

- Convert the resource to JSON
```powershell
$GetDocumentsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

