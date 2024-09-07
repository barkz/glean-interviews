# GetAnswerResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AnswerResult** | [**AnswerResult**](AnswerResult.md) |  | [optional] 
**VarError** | [**GetAnswerError**](GetAnswerError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetAnswerResponse = Initialize-PSOpenAPIToolsGetAnswerResponse  -AnswerResult null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$GetAnswerResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

