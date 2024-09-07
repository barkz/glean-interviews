# SearchResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackingToken** | **String** | A token that should be passed for additional requests related to this request (such as more results requests). | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**Results** | [**SearchResult[]**](SearchResult.md) |  | [optional] 
**StructuredResults** | [**StructuredResult[]**](StructuredResult.md) |  | [optional] 
**GeneratedQnaResult** | [**GeneratedQna**](GeneratedQna.md) |  | [optional] 
**ErrorInfo** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**RequestID** | **String** | A platform-generated request ID to correlate backend logs. | [optional] 
**BackendTimeMillis** | **Int64** | Time in milliseconds the backend took to respond to the request. | [optional] 
**ExperimentIds** | **Int64[]** | List of experiment ids for the corresponding request. | [optional] 
**Metadata** | [**SearchResponseMetadata**](SearchResponseMetadata.md) |  | [optional] 
**FacetResults** | [**FacetResult[]**](FacetResult.md) |  | [optional] 
**ResultTabs** | [**ResultTab[]**](ResultTab.md) | All result tabs available for the current query. Populated if QUERY_METADATA is specified in the request. | [optional] 
**ResultTabIds** | **String[]** | The unique IDs of the result tabs to which this response belongs. | [optional] 
**ResultsDescription** | [**ResultsDescription**](ResultsDescription.md) |  | [optional] 
**RewrittenFacetFilters** | [**FacetFilter[]**](FacetFilter.md) | The actual applied facet filters based on the operators and facetFilters in the query. Useful for mapping typed operators to visual facets. | [optional] 
**Cursor** | **String** | Cursor that indicates the start of the next page of results. To be passed in &quot;&quot;more&quot;&quot; requests for this query. | [optional] 
**HasMoreResults** | **Boolean** | Whether more results are available. Use cursor to retrieve them. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchResponse = Initialize-PSOpenAPIToolsSearchResponse  -TrackingToken null `
 -SessionInfo null `
 -Results null `
 -StructuredResults null `
 -GeneratedQnaResult null `
 -ErrorInfo null `
 -RequestID null `
 -BackendTimeMillis 1100 `
 -ExperimentIds null `
 -Metadata null `
 -FacetResults null `
 -ResultTabs null `
 -ResultTabIds null `
 -ResultsDescription null `
 -RewrittenFacetFilters null `
 -Cursor null `
 -HasMoreResults null
```

- Convert the resource to JSON
```powershell
$SearchResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

