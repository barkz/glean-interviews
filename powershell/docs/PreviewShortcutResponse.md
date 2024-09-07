# PreviewShortcutResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shortcut** | [**Shortcut**](Shortcut.md) |  | [optional] 
**ExistingUrlShortcuts** | [**Shortcut[]**](Shortcut.md) | Exising shortcuts that have a similar destination URL. | [optional] 
**VarError** | [**ShortcutError**](ShortcutError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PreviewShortcutResponse = Initialize-PSOpenAPIToolsPreviewShortcutResponse  -Shortcut null `
 -ExistingUrlShortcuts null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$PreviewShortcutResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

