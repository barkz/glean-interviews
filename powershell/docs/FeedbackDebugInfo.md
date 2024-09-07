# FeedbackDebugInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DesktopAppVersion** | **String** | The version of the desktop app from which the feedback was sent, if applicable | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedbackDebugInfo = Initialize-PSOpenAPIToolsFeedbackDebugInfo  -DesktopAppVersion null
```

- Convert the resource to JSON
```powershell
$FeedbackDebugInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

