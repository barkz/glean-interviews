# DisplayableListConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Format** | **String** | defines how to render this particular displayable list card | [optional] 
**Title** | **String** | Primary title for the list. | [optional] 
**Enabled** | **Boolean** | Whether the list should be shown to the user | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should should see displayable list | [optional] 
**ItemUIConfig** | [**DisplayableListItemUIConfig**](DisplayableListItemUIConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DisplayableListConfig = Initialize-PSOpenAPIToolsDisplayableListConfig  -Format null `
 -Title null `
 -Enabled null `
 -AudienceFilters null `
 -ItemUIConfig null
```

- Convert the resource to JSON
```powershell
$DisplayableListConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

