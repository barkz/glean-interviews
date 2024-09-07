# EditAnswerBoardResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BoardResult** | [**AnswerBoardResult**](AnswerBoardResult.md) |  | [optional] 
**VarError** | [**AnswerBoardError**](AnswerBoardError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$EditAnswerBoardResponse = Initialize-PSOpenAPIToolsEditAnswerBoardResponse  -BoardResult null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$EditAnswerBoardResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

