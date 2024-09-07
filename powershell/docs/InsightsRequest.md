# InsightsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Categories** | **String[]** | Categories of data requested. Request can include single or multiple types. | 
**Departments** | **String[]** | Departments that the data is requested for. If the empty, corresponds to whole company. | [optional] 
**AssistantActivityTypes** | **String[]** | Types of activity that should count in the definition of an Assistant Active User. Affects only insights for AI category. | [optional] 
**DayRange** | [**Period**](Period.md) |  | [optional] 
**AiAppRequestOptions** | [**InsightsAiAppRequestOptions**](InsightsAiAppRequestOptions.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$InsightsRequest = Initialize-PSOpenAPIToolsInsightsRequest  -Categories null `
 -Departments null `
 -AssistantActivityTypes null `
 -DayRange null `
 -AiAppRequestOptions null
```

- Convert the resource to JSON
```powershell
$InsightsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

