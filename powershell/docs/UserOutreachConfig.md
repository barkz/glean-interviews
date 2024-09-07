# UserOutreachConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WeeklyFeedEmailEnabled** | **Boolean** | Whether the weekly feed email is enabled | [optional] 
**OnboardingCampaignEnabled** | **Boolean** | Whether the onboarding email campaign is enabled | [optional] 

## Examples

- Prepare the resource
```powershell
$UserOutreachConfig = Initialize-PSOpenAPIToolsUserOutreachConfig  -WeeklyFeedEmailEnabled null `
 -OnboardingCampaignEnabled null
```

- Convert the resource to JSON
```powershell
$UserOutreachConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

