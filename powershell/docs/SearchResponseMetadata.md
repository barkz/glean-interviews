# SearchResponseMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RewrittenQuery** | **String** | A cleaned up or updated version of the query to be displayed in the query box. Useful for mapping visual facets to search operators. | [optional] 
**SearchedQuery** | **String** | The actual query used to perform search and return results. | [optional] 
**SearchedQueryRanges** | [**TextRange[]**](TextRange.md) | The bolded ranges within the searched query. | [optional] 
**OriginalQuery** | **String** | The query text sent by the client in the request. | [optional] 
**QuerySuggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**AdditionalQuerySuggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**NegatedTerms** | **String[]** | A list of terms that were negated when processing the query. | [optional] 
**ModifiedQueryWasUsed** | **Boolean** | A different query was performed than the one requested. | [optional] 
**OriginalQueryHadNoResults** | **Boolean** | No results were found for the original query. The usage of this bit in conjunction with modifiedQueryWasUsed will dictate whether the full page replacement is 0-result or few-result based. | [optional] 
**SearchWarning** | [**SearchWarning**](SearchWarning.md) |  | [optional] 
**TriggeredExpertDetection** | **Boolean** | Whether the query triggered expert detection results in the People tab. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchResponseMetadata = Initialize-PSOpenAPIToolsSearchResponseMetadata  -RewrittenQuery null `
 -SearchedQuery null `
 -SearchedQueryRanges null `
 -OriginalQuery null `
 -QuerySuggestion null `
 -AdditionalQuerySuggestions null `
 -NegatedTerms null `
 -ModifiedQueryWasUsed null `
 -OriginalQueryHadNoResults null `
 -SearchWarning null `
 -TriggeredExpertDetection null
```

- Convert the resource to JSON
```powershell
$SearchResponseMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

