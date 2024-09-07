# ResolutionStep
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepText** | **String** | text for what step to take | [optional] 
**Link** | **String** | optional link url for instructions | [optional] 

## Examples

- Prepare the resource
```powershell
$ResolutionStep = Initialize-PSOpenAPIToolsResolutionStep  -StepText null `
 -Link null
```

- Convert the resource to JSON
```powershell
$ResolutionStep | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

