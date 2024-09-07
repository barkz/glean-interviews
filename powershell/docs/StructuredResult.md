# StructuredResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Document** | [**Document**](Document.md) |  | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 
**Customer** | [**Customer**](Customer.md) |  | [optional] 
**Team** | [**Team**](Team.md) |  | [optional] 
**CustomEntity** | [**CustomEntity**](CustomEntity.md) |  | [optional] 
**Answer** | [**Answer**](Answer.md) |  | [optional] 
**ExtractedQnA** | [**ExtractedQnA**](ExtractedQnA.md) |  | [optional] 
**App** | [**AppResult**](AppResult.md) |  | [optional] 
**Collection** | [**Collection**](Collection.md) |  | [optional] 
**AnswerBoard** | [**AnswerBoard**](AnswerBoard.md) |  | [optional] 
**Code** | [**Code**](Code.md) |  | [optional] 
**Shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**QuerySuggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**RelatedDocuments** | [**RelatedDocuments[]**](RelatedDocuments.md) | A list of documents related to this structured result. | [optional] 
**RelatedQuestion** | [**RelatedQuestion**](RelatedQuestion.md) |  | [optional] 
**Snippets** | [**SearchResultSnippet[]**](SearchResultSnippet.md) | Any snippets associated to the populated object. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**Prominence** | **String** | The level of visual distinction that should be given to a result. | [optional] 
**Source** | **String** | Source context for this result. Possible values depend on the result type. | [optional] 

## Examples

- Prepare the resource
```powershell
$StructuredResult = Initialize-PSOpenAPIToolsStructuredResult  -Document null `
 -Person null `
 -Customer null `
 -Team null `
 -CustomEntity null `
 -Answer null `
 -ExtractedQnA null `
 -App null `
 -Collection null `
 -AnswerBoard null `
 -Code null `
 -Shortcut null `
 -QuerySuggestions null `
 -RelatedDocuments null `
 -RelatedQuestion null `
 -Snippets null `
 -TrackingToken null `
 -Prominence null `
 -Source null
```

- Convert the resource to JSON
```powershell
$StructuredResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

