# PermissionedObject
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PermissionedObject = Initialize-PSOpenAPIToolsPermissionedObject  -Permissions null
```

- Convert the resource to JSON
```powershell
$PermissionedObject | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

