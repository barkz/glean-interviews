# WritePermission
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ScopeType** | [**ScopeType**](ScopeType.md) |  | [optional] 
**Create** | **Boolean** | True if user has create permission for this feature and scope | [optional] 
**Update** | **Boolean** | True if user has update permission for this feature and scope | [optional] 
**Delete** | **Boolean** | True if user has delete permission for this feature and scope | [optional] 

## Examples

- Prepare the resource
```powershell
$WritePermission = Initialize-PSOpenAPIToolsWritePermission  -ScopeType null `
 -Create null `
 -Update null `
 -Delete null
```

- Convert the resource to JSON
```powershell
$WritePermission | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

