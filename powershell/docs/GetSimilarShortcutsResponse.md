# GetSimilarShortcutsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shortcuts** | [**Shortcut[]**](Shortcut.md) | Shortcuts with similar aliases to the given. Includes shortcut with the exact alias if it exists. | 

## Examples

- Prepare the resource
```powershell
$GetSimilarShortcutsResponse = Initialize-PSOpenAPIToolsGetSimilarShortcutsResponse  -Shortcuts null
```

- Convert the resource to JSON
```powershell
$GetSimilarShortcutsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

