# User
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserID** | **String** | An opaque user ID for the claimed authority (i.e., the actas param, or the origid if actas is not specified). | [optional] 
**OrigID** | **String** | An opaque user ID for the authenticated user (ignores actas). | [optional] 

## Examples

- Prepare the resource
```powershell
$User = Initialize-PSOpenAPIToolsUser  -UserID null `
 -OrigID null
```

- Convert the resource to JSON
```powershell
$User | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

