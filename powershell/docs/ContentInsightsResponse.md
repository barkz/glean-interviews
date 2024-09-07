# ContentInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**DocumentInsights** | [**DocumentInsight[]**](DocumentInsight.md) | Insights for documents. | [optional] 
**Departments** | **String[]** | list of departments applicable for contents tab. | [optional] 
**MinDepartmentSizeThreshold** | **Int32** | Min threshold in size of departments while populating results, otherwise 0. | [optional] 
**MinVisitorThreshold** | **Int32** | Minimum number of visitors to a document required to be included in insights. | [optional] 

## Examples

- Prepare the resource
```powershell
$ContentInsightsResponse = Initialize-PSOpenAPIToolsContentInsightsResponse  -LastLogTimestamp null `
 -DocumentInsights null `
 -Departments null `
 -MinDepartmentSizeThreshold null `
 -MinVisitorThreshold null
```

- Convert the resource to JSON
```powershell
$ContentInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

