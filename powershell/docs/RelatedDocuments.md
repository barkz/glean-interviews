# RelatedDocuments
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Relation** | **String** | How this document relates to the including entity. | [optional] 
**AssociatedEntityId** | **String** | Which entity in the response that this entity relates to. Relevant when there are multiple entities associated with the response (such as merged customers) | [optional] 
**QuerySuggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**Documents** | [**Document[]**](Document.md) | A truncated list of documents with this relation. TO BE DEPRECATED. | [optional] 
**Results** | [**SearchResult[]**](SearchResult.md) | A truncated list of documents associated with this relation. To be used in favor of &#x60;documents&#x60; because it contains a trackingToken. | [optional] 

## Examples

- Prepare the resource
```powershell
$RelatedDocuments = Initialize-PSOpenAPIToolsRelatedDocuments  -Relation null `
 -AssociatedEntityId null `
 -QuerySuggestion null `
 -Documents null `
 -Results null
```

- Convert the resource to JSON
```powershell
$RelatedDocuments | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

