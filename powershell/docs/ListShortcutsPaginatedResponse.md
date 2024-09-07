# ListShortcutsPaginatedResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shortcuts** | [**Shortcut[]**](Shortcut.md) | List of all shortcuts accessible to the user | 
**FacetResults** | [**FacetResult[]**](FacetResult.md) |  | [optional] 
**Meta** | [**ShortcutsPaginationMetadata**](ShortcutsPaginationMetadata.md) |  | 

## Examples

- Prepare the resource
```powershell
$ListShortcutsPaginatedResponse = Initialize-PSOpenAPIToolsListShortcutsPaginatedResponse  -Shortcuts null `
 -FacetResults null `
 -Meta null
```

- Convert the resource to JSON
```powershell
$ListShortcutsPaginatedResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

