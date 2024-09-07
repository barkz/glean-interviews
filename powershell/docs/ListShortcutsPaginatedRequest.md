# ListShortcutsPaginatedRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IncludeFields** | **String[]** | Array of fields/data to be included in response that are not included by default | [optional] 
**PageSize** | **Int32** |  | 
**Cursor** | **String** | A token specifying the position in the overall results to start at. Received from the endpoint and iterated back. Currently being used as page no (as we implement offset pagination) | [optional] 
**Filters** | [**FacetFilter[]**](FacetFilter.md) | A list of filters for the query. An AND is assumed between different filters. We support filters on Go Link name, author, department and type. | [optional] 
**Sort** | [**SortOptions**](SortOptions.md) |  | [optional] 
**Query** | **String** | Search query that should be a substring in atleast one of the fields (alias , inputAlias, destinationUrl, description). Empty query does not filter shortcuts. | [optional] 

## Examples

- Prepare the resource
```powershell
$ListShortcutsPaginatedRequest = Initialize-PSOpenAPIToolsListShortcutsPaginatedRequest  -IncludeFields null `
 -PageSize 10 `
 -Cursor null `
 -Filters null `
 -Sort null `
 -Query null
```

- Convert the resource to JSON
```powershell
$ListShortcutsPaginatedRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

