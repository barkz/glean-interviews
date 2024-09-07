# AnswerBoardResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Board** | [**AnswerBoard**](AnswerBoard.md) |  | 
**TrackingToken** | **String** | An opaque token that represents this particular Answer Board. To be used for /feedback reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnswerBoardResult = Initialize-PSOpenAPIToolsAnswerBoardResult  -Board null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$AnswerBoardResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

