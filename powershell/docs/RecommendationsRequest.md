# RecommendationsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Timestamp** | **System.DateTime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**TrackingToken** | **String** | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs. | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**SourceDocument** | [**Document**](Document.md) |  | [optional] 
**PageSize** | **Int32** | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don&#39;t count towards pageSize. | [optional] 
**MaxSnippetSize** | **Int32** | Hint to the server about how many characters long a snippet may be. Server may return less or more. | [optional] 
**RecommendationDocumentSpec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**RequestOptions** | [**RecommendationsRequestOptions**](RecommendationsRequestOptions.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$RecommendationsRequest = Initialize-PSOpenAPIToolsRecommendationsRequest  -Timestamp null `
 -TrackingToken null `
 -SessionInfo null `
 -SourceDocument null `
 -PageSize 100 `
 -MaxSnippetSize 400 `
 -RecommendationDocumentSpec null `
 -RequestOptions null
```

- Convert the resource to JSON
```powershell
$RecommendationsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

