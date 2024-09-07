# QuerySuggestion
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MissingTerm** | **String** | A query term missing from the original query on which this suggestion is based | [optional] 
**Query** | **String** | The query being suggested (e.g. enforcing the missing term from the original query) | 
**Label** | **String** | A user-facing description to display for the suggestion | [optional] 
**Datasource** | **String** | The datasource associated with the suggestion | [optional] 
**RequestOptions** | [**SearchRequestOptions**](SearchRequestOptions.md) |  | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | The bolded ranges within the query of the QuerySuggestion. | [optional] 

## Examples

- Prepare the resource
```powershell
$QuerySuggestion = Initialize-PSOpenAPIToolsQuerySuggestion  -MissingTerm null `
 -Query null `
 -Label null `
 -Datasource null `
 -RequestOptions null `
 -Ranges null
```

- Convert the resource to JSON
```powershell
$QuerySuggestion | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

