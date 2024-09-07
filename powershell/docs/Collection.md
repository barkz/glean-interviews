# Collection
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The unique name of the Collection. | 
**Description** | **String** | A brief summary of the Collection&#39;s contents. | 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of added user roles for the Collection. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of removed user roles for the Collection. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. | [optional] 
**Icon** | **String** | The emoji icon of this Collection. | [optional] 
**AdminLocked** | **Boolean** | Indicates whether edits are allowed for everyone or only admins. | [optional] 
**ParentId** | **Int32** | The parent of this Collection, or 0 if it&#39;s a top-level Collection. | [optional] 
**Thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**AllowedDatasource** | **String** | The datasource type this Collection can hold. | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**Id** | **Int32** | The unique ID of the Collection. | 
**CreateTime** | **System.DateTime** |  | [optional] 
**UpdateTime** | **System.DateTime** |  | [optional] 
**Creator** | [**Person**](Person.md) |  | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**ItemCount** | **Int32** | The number of items currently in the Collection. Separated from the actual items so we can grab the count without items. | [optional] 
**ChildCount** | **Int32** | The number of children Collections. Separated from the actual children so we can grab the count without children. | [optional] 
**Items** | [**CollectionItem[]**](CollectionItem.md) | The items in this Collection. | [optional] 
**PinMetadata** | [**CollectionPinnedMetadata**](CollectionPinnedMetadata.md) |  | [optional] 
**Shortcuts** | **String[]** | The names of the shortcuts (Go Links) that point to this Collection. | [optional] 
**Children** | [**Collection[]**](Collection.md) | The children Collections of this Collection. | [optional] 
**Roles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the Collection. | [optional] 

## Examples

- Prepare the resource
```powershell
$Collection = Initialize-PSOpenAPIToolsCollection  -Name null `
 -Description null `
 -AddedRoles null `
 -RemovedRoles null `
 -AudienceFilters null `
 -Icon null `
 -AdminLocked null `
 -ParentId null `
 -Thumbnail null `
 -AllowedDatasource null `
 -Permissions null `
 -Id null `
 -CreateTime null `
 -UpdateTime null `
 -Creator null `
 -UpdatedBy null `
 -ItemCount null `
 -ChildCount null `
 -Items null `
 -PinMetadata null `
 -Shortcuts null `
 -Children null `
 -Roles null
```

- Convert the resource to JSON
```powershell
$Collection | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

