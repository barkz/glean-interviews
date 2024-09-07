# ShortcutsConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShortcutsPrefix** | **String** | Deployment&#39;s prefix for shortcuts. | [optional] 
**UseExternalShortcuts** | **Boolean** | Whether the deployment uses external shortcuts. | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutsConfig = Initialize-PSOpenAPIToolsShortcutsConfig  -ShortcutsPrefix null `
 -UseExternalShortcuts null
```

- Convert the resource to JSON
```powershell
$ShortcutsConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

