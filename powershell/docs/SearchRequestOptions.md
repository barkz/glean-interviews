# SearchRequestOptions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasourceFilter** | **String** | Filter results to a single datasource name (e.g. gmail, slack). All results are returned if missing. | [optional] 
**DatasourcesFilter** | **String[]** | Filter results to one or more datasources (e.g. gmail, slack). All results are returned if missing. | [optional] 
**QueryOverridesFacetFilters** | **Boolean** | If true, the operators in the query are taken to override any operators in facetFilters in the case of conflict. This is used to correctly set rewrittenFacetFilters and rewrittenQuery. | [optional] 
**FacetFilters** | [**FacetFilter[]**](FacetFilter.md) | A list of filters for the query. An AND is assumed between different facetFilters. For example, owner Sumeet and type Spreadsheet shows documents that are by Sumeet AND are Spreadsheets. | [optional] 
**FacetFilterSets** | [**FacetFilterSet[]**](FacetFilterSet.md) | A list of facet filter sets that will be OR&#39;ed together. SearchRequestOptions where both facetFilterSets and facetFilters set are considered as bad request. Callers should set only one of these fields. | [optional] 
**FacetBucketFilter** | [**FacetBucketFilter**](FacetBucketFilter.md) |  | [optional] 
**FacetBucketSize** | **Int32** | The maximum number of FacetBuckets to return in each FacetResult. | 
**DefaultFacets** | **String[]** | Facets for which FacetResults should be fetched and that don&#39;t apply to a particular datasource. If specified, these values will replace the standard default facets (last_updated_at, from, etc.). The requested facets will be returned alongside datasource-specific facets if searching a single datasource. | [optional] 
**AuthTokens** | [**AuthToken[]**](AuthToken.md) | Auth tokens which may be used for non-indexed, federated results (e.g. Gmail). | [optional] 
**FetchAllDatasourceCounts** | **Boolean** | Hints that the QE should return result counts (via the datasource facet result) for all supported datasources, rather than just those specified in the datasource[s]Filter | [optional] 
**ResponseHints** | **String[]** | Array of hints containing which fields should be populated in the response. | [optional] 
**TimezoneOffset** | **Int32** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**ForceNegation** | **Boolean** | Whether or not to force not ignoring of negation, i.e. force negated terms to be negated. | [optional] 
**DisableSpellcheck** | **Boolean** | Whether or not to disable spellcheck. | [optional] 
**DisableQueryAutocorrect** | **Boolean** | Disables automatic adjustment of the input query for spelling corrections or other reasons. | [optional] 
**ReturnLlmContentOverSnippets** | **Boolean** | [beta] Enables expanded content to be returned for LLM usage. The size of content per result returned should be modified using maxSnippetSize. Server may return less or more than what is specified in maxSnippetSize. For more details, https://docs.google.com/document/d/1CTOLSxWWT9WDEnHVLoCUaxbGYyXYP8kctPRF-RluSQY/edit. Requires sufficient permissions. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchRequestOptions = Initialize-PSOpenAPIToolsSearchRequestOptions  -DatasourceFilter null `
 -DatasourcesFilter null `
 -QueryOverridesFacetFilters null `
 -FacetFilters null `
 -FacetFilterSets null `
 -FacetBucketFilter null `
 -FacetBucketSize null `
 -DefaultFacets null `
 -AuthTokens null `
 -FetchAllDatasourceCounts null `
 -ResponseHints null `
 -TimezoneOffset null `
 -ForceNegation null `
 -DisableSpellcheck null `
 -DisableQueryAutocorrect null `
 -ReturnLlmContentOverSnippets null
```

- Convert the resource to JSON
```powershell
$SearchRequestOptions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

