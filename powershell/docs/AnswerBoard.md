# AnswerBoard
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The unique name of the Collection. | 
**Description** | **String** | A brief summary of the Collection&#39;s contents. | 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**Id** | **Int32** | The unique ID of the Answer Board. | 
**CreateTime** | **System.DateTime** |  | [optional] 
**UpdateTime** | **System.DateTime** |  | [optional] 
**Creator** | [**Person**](Person.md) |  | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**ItemCount** | **Int32** | The number of items currently in the Answer Board. Separated from the actual items so we can grab the count without items. | [optional] 
**Roles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the Answer Board. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnswerBoard = Initialize-PSOpenAPIToolsAnswerBoard  -Name null `
 -Description null `
 -AddedRoles null `
 -RemovedRoles null `
 -AudienceFilters null `
 -Permissions null `
 -Id null `
 -CreateTime null `
 -UpdateTime null `
 -Creator null `
 -UpdatedBy null `
 -ItemCount null `
 -Roles null
```

- Convert the resource to JSON
```powershell
$AnswerBoard | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

