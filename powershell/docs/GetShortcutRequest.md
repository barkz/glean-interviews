# GetShortcutRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The opaque id of the user generated content. | [optional] 
**Alias** | **String** | The alias for the shortcut, including any arguments for variable shortcuts. | 

## Examples

- Prepare the resource
```powershell
$GetShortcutRequest = Initialize-PSOpenAPIToolsGetShortcutRequest  -Id null `
 -Alias null
```

- Convert the resource to JSON
```powershell
$GetShortcutRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

