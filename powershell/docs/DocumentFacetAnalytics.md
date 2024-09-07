# DocumentFacetAnalytics
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Facet** | [**FacetFilter**](FacetFilter.md) |  | [optional] 
**Analytics** | [**DocumentAnalytics**](DocumentAnalytics.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentFacetAnalytics = Initialize-PSOpenAPIToolsDocumentFacetAnalytics  -Facet null `
 -Analytics null
```

- Convert the resource to JSON
```powershell
$DocumentFacetAnalytics | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

