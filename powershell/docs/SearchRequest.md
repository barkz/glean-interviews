# SearchRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Timestamp** | **System.DateTime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**TrackingToken** | **String** | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs. | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**SourceDocument** | [**Document**](Document.md) |  | [optional] 
**PageSize** | **Int32** | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don&#39;t count towards pageSize. | [optional] 
**MaxSnippetSize** | **Int32** | Hint to the server about how many characters long a snippet may be. Server may return less or more. | [optional] 
**Query** | **String** | The search terms. | 
**Cursor** | **String** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**ResultTabIds** | **String[]** | The unique IDs of the result tabs for which to fetch results. This will have precedence over datasource filters if both are specified and in conflict. | [optional] 
**InputDetails** | [**SearchRequestInputDetails**](SearchRequestInputDetails.md) |  | [optional] 
**RequestOptions** | [**SearchRequestOptions**](SearchRequestOptions.md) |  | [optional] 
**TimeoutMillis** | **Int32** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**People** | [**Person[]**](Person.md) | People associated with the search request. Hints to the server to fetch additional information for these people. Note that in this request, an email may be used as a person&#39;s obfuscatedId value. | [optional] 
**DisableSpellcheck** | **Boolean** | Whether or not to disable spellcheck. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchRequest = Initialize-PSOpenAPIToolsSearchRequest  -Timestamp null `
 -TrackingToken null `
 -SessionInfo null `
 -SourceDocument null `
 -PageSize 100 `
 -MaxSnippetSize 400 `
 -Query vacation policy `
 -Cursor null `
 -ResultTabIds null `
 -InputDetails null `
 -RequestOptions null `
 -TimeoutMillis 5000 `
 -People null `
 -DisableSpellcheck null
```

- Convert the resource to JSON
```powershell
$SearchRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

