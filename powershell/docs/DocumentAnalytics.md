# DocumentAnalytics
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentSpec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**VisitorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**ClickerCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**UserImpressionCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**VisitCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**FacetAnalytics** | [**DocumentFacetAnalytics[]**](DocumentFacetAnalytics.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentAnalytics = Initialize-PSOpenAPIToolsDocumentAnalytics  -DocumentSpec null `
 -VisitorCount null `
 -ClickerCount null `
 -UserImpressionCount null `
 -VisitCount null `
 -FacetAnalytics null
```

- Convert the resource to JSON
```powershell
$DocumentAnalytics | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

