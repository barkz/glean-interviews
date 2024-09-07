# GetAnswerError
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ErrorType** | **String** |  | [optional] 
**AnswerAuthor** | [**Person**](Person.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetAnswerError = Initialize-PSOpenAPIToolsGetAnswerError  -ErrorType null `
 -AnswerAuthor null
```

- Convert the resource to JSON
```powershell
$GetAnswerError | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

