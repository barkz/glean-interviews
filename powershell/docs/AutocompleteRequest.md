# AutocompleteRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackingToken** | **String** |  | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**Query** | **String** | Partially typed query. | [optional] 
**DatasourcesFilter** | **String[]** | Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). Results are unfiltered if missing. | [optional] 
**Datasource** | **String** | Filter to only return results relevant to the given datasource. | [optional] 
**ResultTypes** | **String[]** | Filter to only return results of the given type(s). All types may be returned if omitted. | [optional] 
**ResultSize** | **Int32** | Maximum number of results to be returned. If no value is provided, the backend will cap at 200.  | [optional] 
**AuthTokens** | [**AuthToken[]**](AuthToken.md) | Auth tokens which may be used for federated results. | [optional] 

## Examples

- Prepare the resource
```powershell
$AutocompleteRequest = Initialize-PSOpenAPIToolsAutocompleteRequest  -TrackingToken null `
 -SessionInfo null `
 -Query San Fra `
 -DatasourcesFilter null `
 -Datasource null `
 -ResultTypes null `
 -ResultSize 10 `
 -AuthTokens null
```

- Convert the resource to JSON
```powershell
$AutocompleteRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

