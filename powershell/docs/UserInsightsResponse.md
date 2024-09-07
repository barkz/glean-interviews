# UserInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**ActivityInsights** | [**UserActivityInsight[]**](UserActivityInsight.md) | Insights for all active users with respect to set of actions. | [optional] 
**InactiveInsights** | [**UserActivityInsight[]**](UserActivityInsight.md) | Insights for all in inactive users with respect to set of actions and time period. Activity count will be set to 0. | [optional] 
**TotalTeammates** | **Int32** | Total number of teammates that have logged in to the product, that are still valid teammates. | [optional] 
**TotalActiveUsers** | **Int32** | Total number of active users in the requested period. | [optional] 
**Departments** | **String[]** | list of departments applicable for users tab. | [optional] 

## Examples

- Prepare the resource
```powershell
$UserInsightsResponse = Initialize-PSOpenAPIToolsUserInsightsResponse  -LastLogTimestamp null `
 -ActivityInsights null `
 -InactiveInsights null `
 -TotalTeammates null `
 -TotalActiveUsers null `
 -Departments null
```

- Convert the resource to JSON
```powershell
$UserInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

