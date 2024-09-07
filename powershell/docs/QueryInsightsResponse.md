# QueryInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**QueryInsights** | [**QueryInsight[]**](QueryInsight.md) | Insights for queries. | [optional] 
**LowPerformingQueryInsights** | [**QueryInsight[]**](QueryInsight.md) | Insights for low performing queries without good results. | [optional] 
**Departments** | **String[]** | list of departments applicable for queries tab. | [optional] 
**MinVisitorThreshold** | **Int32** | Min threshold in number of visitors while populating results, otherwise 0. | [optional] 

## Examples

- Prepare the resource
```powershell
$QueryInsightsResponse = Initialize-PSOpenAPIToolsQueryInsightsResponse  -LastLogTimestamp null `
 -QueryInsights null `
 -LowPerformingQueryInsights null `
 -Departments null `
 -MinVisitorThreshold null
```

- Convert the resource to JSON
```powershell
$QueryInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

