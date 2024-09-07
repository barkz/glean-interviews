# ResultsDescription
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Text** | **String** | Textual description of the results. Can be shown at the top of SERP, e.g. &#39;People who write about this topic&#39; for experts in people tab. | [optional] 
**IconConfig** | [**IconConfig**](IconConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ResultsDescription = Initialize-PSOpenAPIToolsResultsDescription  -Text null `
 -IconConfig null
```

- Convert the resource to JSON
```powershell
$ResultsDescription | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

