# ObjectPermissions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Write** | [**WritePermission**](WritePermission.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ObjectPermissions = Initialize-PSOpenAPIToolsObjectPermissions  -Write null
```

- Convert the resource to JSON
```powershell
$ObjectPermissions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

