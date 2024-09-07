# ShortcutInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**ShortcutInsights** | [**ShortcutInsight[]**](ShortcutInsight.md) | Insights for shortcuts. | [optional] 
**Departments** | **String[]** | list of departments applicable for shortcuts tab. | [optional] 
**MinVisitorThreshold** | **Int32** | Min threshold in number of visitors while populating results, otherwise 0. | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutInsightsResponse = Initialize-PSOpenAPIToolsShortcutInsightsResponse  -LastLogTimestamp null `
 -ShortcutInsights null `
 -Departments null `
 -MinVisitorThreshold null
```

- Convert the resource to JSON
```powershell
$ShortcutInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

