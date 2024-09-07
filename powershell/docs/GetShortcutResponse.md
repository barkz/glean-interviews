# GetShortcutResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**VarError** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetShortcutResponse = Initialize-PSOpenAPIToolsGetShortcutResponse  -Shortcut null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$GetShortcutResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

