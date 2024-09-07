# PeopleFilters
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VarFilter** | [**FacetFilter[]**](FacetFilter.md) | Facets used for filtering people search | [optional] 
**Query** | **String** | A query string to search for people that each person in the response must conform to. An empty query does not filter any people. | [optional] 

## Examples

- Prepare the resource
```powershell
$PeopleFilters = Initialize-PSOpenAPIToolsPeopleFilters  -VarFilter null `
 -Query null
```

- Convert the resource to JSON
```powershell
$PeopleFilters | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

