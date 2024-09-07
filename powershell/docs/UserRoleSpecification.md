# UserRoleSpecification
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceDocumentSpec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 
**Group** | [**Group**](Group.md) |  | [optional] 
**Role** | [**UserRole**](UserRole.md) |  | 

## Examples

- Prepare the resource
```powershell
$UserRoleSpecification = Initialize-PSOpenAPIToolsUserRoleSpecification  -SourceDocumentSpec null `
 -Person null `
 -Group null `
 -Role null
```

- Convert the resource to JSON
```powershell
$UserRoleSpecification | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

