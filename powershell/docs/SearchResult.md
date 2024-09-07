# SearchResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StructuredResults** | [**StructuredResult[]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**Title** | **String** |  | [optional] 
**Url** | **String** |  | 
**NativeAppUrl** | **String** | A deep link, if available, into the datasource&#39;s native application for the user&#39;s platform (e.g. slack://...). | [optional] 
**Snippets** | [**SearchResultSnippet[]**](SearchResultSnippet.md) | Text content from the result document which contains search query terms, if available. | [optional] 
**ExpandedSnippets** | **String[]** | The expanded snippets for this result. This is only populated if the query has the expand_snippets parameter set to true. | [optional] 
**FullText** | **String** | The full body text of the result if not already contained in the snippets | [optional] 
**FullTextList** | **String[]** | The full body text of the result if not already contained in the snippets; each item in the array represents a separate line in the original text | [optional] 
**RelatedResults** | [**RelatedDocuments[]**](RelatedDocuments.md) | A list of results related to this search result. Eg. for conversation results it contains individual messages from the conversation document which will be shown on SERP. | [optional] 
**ClusteredResults** | [**SearchResult[]**](SearchResult.md) | A list of results that should be displayed as associated with this result. | [optional] 
**AllClusteredResults** | [**ClusterGroup[]**](ClusterGroup.md) | A list of results that should be displayed as associated with this result. | [optional] 
**AttachmentCount** | **Int32** | The total number of attachments. | [optional] 
**Attachments** | [**SearchResult[]**](SearchResult.md) | A (potentially partial) list of results representing documents attached to the main result document. | [optional] 
**BacklinkResults** | [**SearchResult[]**](SearchResult.md) | A list of results that should be displayed as backlinks of this result in reverse chronological order. | [optional] 
**ClusterType** | [**ClusterTypeEnum**](ClusterTypeEnum.md) |  | [optional] 
**MustIncludeSuggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**QuerySuggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**Prominence** | [**SearchResultProminenceEnum**](SearchResultProminenceEnum.md) |  | [optional] 
**AttachmentContext** | **String** | Additional context for the relationship between the result and the document it&#39;s attached to. | [optional] 
**Pins** | [**PinDocument[]**](PinDocument.md) | A list of pins associated with this search result. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchResult = Initialize-PSOpenAPIToolsSearchResult  -StructuredResults null `
 -TrackingToken null `
 -Document null `
 -Title null `
 -Url null `
 -NativeAppUrl null `
 -Snippets null `
 -ExpandedSnippets null `
 -FullText null `
 -FullTextList null `
 -RelatedResults null `
 -ClusteredResults null `
 -AllClusteredResults null `
 -AttachmentCount null `
 -Attachments null `
 -BacklinkResults null `
 -ClusterType null `
 -MustIncludeSuggestions null `
 -QuerySuggestion null `
 -Prominence null `
 -AttachmentContext null `
 -Pins null
```

- Convert the resource to JSON
```powershell
$SearchResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

