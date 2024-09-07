# ListEntitiesResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**Person[]**](Person.md) |  | [optional] 
**TeamResults** | [**Team[]**](Team.md) |  | [optional] 
**CustomEntityResults** | [**CustomEntity[]**](CustomEntity.md) |  | [optional] 
**FacetResults** | [**FacetResult[]**](FacetResult.md) |  | [optional] 
**Cursor** | **String** | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start. | [optional] 
**TotalCount** | **Int32** | The total number of entities available | [optional] 
**HasMoreResults** | **Boolean** | Whether or not more entities can be fetched. | [optional] 
**SortOptions** | [**EntitiesSortOrder[]**](EntitiesSortOrder.md) | Sort options from EntitiesSortOrder supported for this response. Default is empty list. | [optional] 
**CustomFacetNames** | **String[]** | list of Person attributes that are custom setup by deployment | [optional] 

## Examples

- Prepare the resource
```powershell
$ListEntitiesResponse = Initialize-PSOpenAPIToolsListEntitiesResponse  -Results null `
 -TeamResults null `
 -CustomEntityResults null `
 -FacetResults null `
 -Cursor null `
 -TotalCount null `
 -HasMoreResults null `
 -SortOptions null `
 -CustomFacetNames null
```

- Convert the resource to JSON
```powershell
$ListEntitiesResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

