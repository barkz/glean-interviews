# ExtractedQnA
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Heading** | **String** | Heading text that was matched to produce this result. | [optional] 
**Question** | **String** | Question text that was matched to produce this result. | [optional] 
**QuestionResult** | [**SearchResult**](SearchResult.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ExtractedQnA = Initialize-PSOpenAPIToolsExtractedQnA  -Heading null `
 -Question null `
 -QuestionResult null
```

- Convert the resource to JSON
```powershell
$ExtractedQnA | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

