# InsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Timeseries** | [**LabeledCountInfo[]**](LabeledCountInfo.md) | List of timeseries to make charts (if applicable). | [optional] 
**Users** | [**UserInsightsResponse**](UserInsightsResponse.md) |  | [optional] 
**Content** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**Queries** | [**QueryInsightsResponse**](QueryInsightsResponse.md) |  | [optional] 
**Collections** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**CollectionsV2** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**Shortcuts** | [**ShortcutInsightsResponse**](ShortcutInsightsResponse.md) |  | [optional] 
**Announcements** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**Answers** | [**ContentInsightsResponse**](ContentInsightsResponse.md) |  | [optional] 
**Ai** | [**AiInsightsResponse**](AiInsightsResponse.md) |  | [optional] 
**AiApps** | [**AiAppsInsightsResponse**](AiAppsInsightsResponse.md) |  | [optional] 
**Departments** | **String[]** | list of all departments. | [optional] 

## Examples

- Prepare the resource
```powershell
$InsightsResponse = Initialize-PSOpenAPIToolsInsightsResponse  -Timeseries null `
 -Users null `
 -Content null `
 -Queries null `
 -Collections null `
 -CollectionsV2 null `
 -Shortcuts null `
 -Announcements null `
 -Answers null `
 -Ai null `
 -AiApps null `
 -Departments null
```

- Convert the resource to JSON
```powershell
$InsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

