# RelatedQuestion
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Question** | **String** | The text of the related question | [optional] 
**Answer** | **String** | The answer for the related question | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | Subsections of the answer string to which some special formatting should be applied (eg. bold) | [optional] 

## Examples

- Prepare the resource
```powershell
$RelatedQuestion = Initialize-PSOpenAPIToolsRelatedQuestion  -Question null `
 -Answer null `
 -Ranges null
```

- Convert the resource to JSON
```powershell
$RelatedQuestion | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

