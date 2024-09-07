# SeenFeedbackInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsExplicit** | **Boolean** | The confidence of the user seeing the object is high because they explicitly interacted with it e.g. answer impression in SERP with additional user interaction. | [optional] 

## Examples

- Prepare the resource
```powershell
$SeenFeedbackInfo = Initialize-PSOpenAPIToolsSeenFeedbackInfo  -IsExplicit null
```

- Convert the resource to JSON
```powershell
$SeenFeedbackInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

