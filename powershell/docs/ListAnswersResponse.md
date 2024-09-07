# ListAnswersResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AnswerResults** | [**AnswerResult[]**](AnswerResult.md) | List of answers with tracking tokens. | 

## Examples

- Prepare the resource
```powershell
$ListAnswersResponse = Initialize-PSOpenAPIToolsListAnswersResponse  -AnswerResults null
```

- Convert the resource to JSON
```powershell
$ListAnswersResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

