# ListAnswerBoardsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WithAudience** | **Boolean** | Whether to include the audience filters with the listed Answer Boards. | [optional] 
**WithRoles** | **Boolean** | Whether to include the editor roles with the listed Answer Boards. | [optional] 

## Examples

- Prepare the resource
```powershell
$ListAnswerBoardsRequest = Initialize-PSOpenAPIToolsListAnswerBoardsRequest  -WithAudience null `
 -WithRoles null
```

- Convert the resource to JSON
```powershell
$ListAnswerBoardsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

