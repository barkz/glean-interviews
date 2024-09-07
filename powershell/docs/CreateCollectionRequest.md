# CreateCollectionRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The unique name of the Collection. | 
**Description** | **String** | A brief summary of the Collection&#39;s contents. | [optional] 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**Icon** | **String** | The emoji icon of this Collection. | [optional] 
**AdminLocked** | **Boolean** | Indicates whether edits are allowed for everyone or only admins. | [optional] 
**ParentId** | **Int32** | The parent of this Collection, or 0 if it&#39;s a top-level Collection. | [optional] 
**Thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**AllowedDatasource** | **String** | The datasource type this Collection can hold. | [optional] 
**NewNextItemId** | **String** | The (optional) ItemId of the next CollectionItem in sequence. If omitted, will be added to the end of the Collection. Only used if parentId is specified. | [optional] 

## Examples

- Prepare the resource
```powershell
$CreateCollectionRequest = Initialize-PSOpenAPIToolsCreateCollectionRequest  -Name null `
 -Description null `
 -AddedRoles null `
 -RemovedRoles null `
 -AudienceFilters null `
 -Icon null `
 -AdminLocked null `
 -ParentId null `
 -Thumbnail null `
 -AllowedDatasource null `
 -NewNextItemId null
```

- Convert the resource to JSON
```powershell
$CreateCollectionRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

