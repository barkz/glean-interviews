# EditPermissionsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserIds** | **String[]** | The ids of the users whose permissions will be edited | [optional] 
**Permissions** | [**Permissions**](Permissions.md) |  | 

## Examples

- Prepare the resource
```powershell
$EditPermissionsRequest = Initialize-PSOpenAPIToolsEditPermissionsRequest  -UserIds null `
 -Permissions null
```

- Convert the resource to JSON
```powershell
$EditPermissionsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

