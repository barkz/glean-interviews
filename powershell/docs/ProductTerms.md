# ProductTerms
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assistant** | [**ProductTerm**](ProductTerm.md) |  | [optional] 
**GleanAssistant** | [**ProductTerm**](ProductTerm.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ProductTerms = Initialize-PSOpenAPIToolsProductTerms  -Assistant null `
 -GleanAssistant null
```

- Convert the resource to JSON
```powershell
$ProductTerms | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

