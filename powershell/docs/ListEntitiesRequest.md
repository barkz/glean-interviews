# ListEntitiesRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VarFilter** | [**FacetFilter[]**](FacetFilter.md) |  | [optional] 
**Sort** | [**SortOptions[]**](SortOptions.md) | Use EntitiesSortOrder enum for SortOptions.sortBy | [optional] 
**EntityType** | **String** |  | [optional] [default to "PEOPLE"]
**Datasource** | **String** | The datasource associated with the entity type, most commonly used with CUSTOM_ENTITIES | [optional] 
**Query** | **String** | A query string to search for entities that each entity in the response must conform to. An empty query does not filter any entities. | [optional] 
**IncludeFields** | **String[]** | List of entity fields to return (that aren&#39;t returned by default) | [optional] 
**PageSize** | **Int32** | Hint to the server about how many results to send back. Server may return less. | [optional] 
**Cursor** | **String** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**Source** | **String** | A string denoting the search surface from which the endpoint is called. | [optional] 

## Examples

- Prepare the resource
```powershell
$ListEntitiesRequest = Initialize-PSOpenAPIToolsListEntitiesRequest  -VarFilter null `
 -Sort null `
 -EntityType null `
 -Datasource null `
 -Query null `
 -IncludeFields null `
 -PageSize 100 `
 -Cursor null `
 -Source null
```

- Convert the resource to JSON
```powershell
$ListEntitiesRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

