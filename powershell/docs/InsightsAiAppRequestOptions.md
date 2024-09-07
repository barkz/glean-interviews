# InsightsAiAppRequestOptions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AiAppIds** | **String[]** | IDs of the AI Apps for which Insights should be returned. An empty array signifies all. | [optional] 

## Examples

- Prepare the resource
```powershell
$InsightsAiAppRequestOptions = Initialize-PSOpenAPIToolsInsightsAiAppRequestOptions  -AiAppIds null
```

- Convert the resource to JSON
```powershell
$InsightsAiAppRequestOptions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

