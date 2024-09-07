# AiAppsInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**AiAppInsights** | [**UserActivityInsight[]**](UserActivityInsight.md) |  | [optional] 
**TotalActiveUsers** | **Int32** | Total number of active users on the Ai App in the requested period. | [optional] 
**ActionCounts** | [**AiAppActionCounts**](AiAppActionCounts.md) |  | [optional] 
**Departments** | **String[]** | list of departments applicable for users tab. | [optional] 

## Examples

- Prepare the resource
```powershell
$AiAppsInsightsResponse = Initialize-PSOpenAPIToolsAiAppsInsightsResponse  -LastLogTimestamp null `
 -AiAppInsights null `
 -TotalActiveUsers null `
 -ActionCounts null `
 -Departments null
```

- Convert the resource to JSON
```powershell
$AiAppsInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

