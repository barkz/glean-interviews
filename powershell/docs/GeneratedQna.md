# GeneratedQna
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Question** | **String** | Search query rephrased into a question. | [optional] 
**Answer** | **String** | Answer generated for the given query or the generated question. | [optional] 
**FollowUpPrompts** | **String[]** | List of all follow-up prompts generated for the given query or the generated question. | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | Answer subsections to mark with special formatting (citations, bolding etc) | [optional] 
**Status** | **String** | Status of backend generating the answer | [optional] 
**Cursor** | **String** | An opaque cursor representing the search request | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$GeneratedQna = Initialize-PSOpenAPIToolsGeneratedQna  -Question null `
 -Answer null `
 -FollowUpPrompts null `
 -Ranges null `
 -Status null `
 -Cursor null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$GeneratedQna | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

