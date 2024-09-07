# RecommendationsRequestOptions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasourceFilter** | **String** | Filter results to a single datasource name (e.g. gmail, slack). All results are returned if missing. | [optional] 
**DatasourcesFilter** | **String[]** | Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). All results are returned if missing. | [optional] 
**FacetFilterSets** | [**FacetFilterSet[]**](FacetFilterSet.md) | A list of facet filter sets that will be OR&#39;ed together. | [optional] 
**Context** | [**Document**](Document.md) |  | [optional] 
**ResultProminence** | [**SearchResultProminenceEnum[]**](SearchResultProminenceEnum.md) | The types of prominence wanted in results returned. Default is any type. | [optional] 

## Examples

- Prepare the resource
```powershell
$RecommendationsRequestOptions = Initialize-PSOpenAPIToolsRecommendationsRequestOptions  -DatasourceFilter null `
 -DatasourcesFilter null `
 -FacetFilterSets null `
 -Context null `
 -ResultProminence null
```

- Convert the resource to JSON
```powershell
$RecommendationsRequestOptions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

