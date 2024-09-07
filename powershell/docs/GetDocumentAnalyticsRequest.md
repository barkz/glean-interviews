# GetDocumentAnalyticsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentSpecs** | [**DocumentSpec[]**](DocumentSpec.md) | The specification for the documents for which analytics will be retrieved. | 
**DayRange** | [**Period**](Period.md) |  | 
**WithClickerCounts** | **Boolean** | Whether response should include click information or not. Default is to not include click information. | [optional] 
**WithImpressionCounts** | **Boolean** | Whether response should include impression information or not. Default is to not include impression information. | [optional] 
**WithFacetAggregations** | **Boolean** | Whether the results will include aggregate counts/info for facets like location, department, etc. | [optional] 
**WithVisitCounts** | **Boolean** | Whether response should include visit counts or not. Default is to return only visitor counts. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDocumentAnalyticsRequest = Initialize-PSOpenAPIToolsGetDocumentAnalyticsRequest  -DocumentSpecs null `
 -DayRange null `
 -WithClickerCounts null `
 -WithImpressionCounts null `
 -WithFacetAggregations null `
 -WithVisitCounts null
```

- Convert the resource to JSON
```powershell
$GetDocumentAnalyticsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

