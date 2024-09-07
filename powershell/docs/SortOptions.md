# SortOptions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OrderBy** | **String** |  | [optional] 
**SortBy** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$SortOptions = Initialize-PSOpenAPIToolsSortOptions  -OrderBy null `
 -SortBy null
```

- Convert the resource to JSON
```powershell
$SortOptions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

