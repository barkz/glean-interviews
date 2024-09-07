# ShortcutsPaginationMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cursor** | **String** | Cursor indicates the start of the next page of results | [optional] 
**HasNextPage** | **Boolean** |  | [optional] 
**TotalItemCount** | **Int32** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutsPaginationMetadata = Initialize-PSOpenAPIToolsShortcutsPaginationMetadata  -Cursor null `
 -HasNextPage null `
 -TotalItemCount null
```

- Convert the resource to JSON
```powershell
$ShortcutsPaginationMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

