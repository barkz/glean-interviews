# AnswerResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Answer** | [**Answer**](Answer.md) |  | 
**TrackingToken** | **String** | An opaque token that represents this particular Answer. To be used for &#x60;/feedback&#x60; reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnswerResult = Initialize-PSOpenAPIToolsAnswerResult  -Answer null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$AnswerResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

