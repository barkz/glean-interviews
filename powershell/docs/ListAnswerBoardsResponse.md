# ListAnswerBoardsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BoardResults** | [**AnswerBoardResult[]**](AnswerBoardResult.md) | List of all Answer Boards, no Answers are included. | 

## Examples

- Prepare the resource
```powershell
$ListAnswerBoardsResponse = Initialize-PSOpenAPIToolsListAnswerBoardsResponse  -BoardResults null
```

- Convert the resource to JSON
```powershell
$ListAnswerBoardsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

