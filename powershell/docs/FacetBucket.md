# FacetBucket
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Count** | **Int32** | Estimated number of results in this facet. | [optional] 
**Datasource** | **String** | The datasource the value belongs to. This will be used by the all tab to show types across all datasources. | [optional] 
**Percentage** | **Int32** | Estimated percentage of results in this facet. | [optional] 
**Value** | [**FacetValue**](FacetValue.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetBucket = Initialize-PSOpenAPIToolsFacetBucket  -Count 1 `
 -Datasource jira `
 -Percentage 5 `
 -Value null
```

- Convert the resource to JSON
```powershell
$FacetBucket | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

