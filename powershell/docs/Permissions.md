# Permissions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CanAdminSearch** | **Boolean** | TODO--deprecate in favor of the read and write properties. True if the user has access to /adminsearch | [optional] 
**CanAdminClientApiGlobalTokens** | **Boolean** | TODO--deprecate in favor of the read and write properties. True if the user can administrate client API tokens with global scope | [optional] 
**CanDlp** | **Boolean** | TODO--deprecate in favor of the read and write properties. True if the user has access to data loss prevention (DLP) features | [optional] 
**Read** | [**System.Collections.Hashtable**](Array.md) | Describes the read permission levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**Write** | [**System.Collections.Hashtable**](Array.md) | Describes the write permissions levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**Grant** | [**System.Collections.Hashtable**](Array.md) | Describes the grant permission levels that a user has for permissioned features. Key must be PermissionedFeatureOrObject | [optional] 
**Role** | **String** | The roleId of the canonical role a user has. The displayName is equal to the roleId. | [optional] 
**Roles** | **String[]** | The roleIds of the roles a user has. | [optional] 

## Examples

- Prepare the resource
```powershell
$Permissions = Initialize-PSOpenAPIToolsPermissions  -CanAdminSearch null `
 -CanAdminClientApiGlobalTokens null `
 -CanDlp null `
 -Read null `
 -Write null `
 -Grant null `
 -Role null `
 -Roles null
```

- Convert the resource to JSON
```powershell
$Permissions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

