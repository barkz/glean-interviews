# CustomEntity
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**Id** | **String** | Unique identifier. | [optional] 
**Title** | **String** | Title or name of the custom entity. | [optional] 
**Datasource** | **String** | The datasource the custom entity is from. | [optional] 
**ObjectType** | **String** | The type of the entity. Interpretation is specific to each datasource | [optional] 
**Metadata** | [**CustomEntityMetadata**](CustomEntityMetadata.md) |  | [optional] 
**Roles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the custom entity explicitly granted by the owner. | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomEntity = Initialize-PSOpenAPIToolsCustomEntity  -Permissions null `
 -Id null `
 -Title null `
 -Datasource null `
 -ObjectType null `
 -Metadata null `
 -Roles null
```

- Convert the resource to JSON
```powershell
$CustomEntity | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

