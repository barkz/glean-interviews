# CollectionBaseMutableProperties
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The unique name of the Collection. | 
**Description** | **String** | A brief summary of the Collection&#39;s contents. | [optional] 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 

## Examples

- Prepare the resource
```powershell
$CollectionBaseMutableProperties = Initialize-PSOpenAPIToolsCollectionBaseMutableProperties  -Name null `
 -Description null `
 -AddedRoles null `
 -RemovedRoles null `
 -AudienceFilters null
```

- Convert the resource to JSON
```powershell
$CollectionBaseMutableProperties | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

