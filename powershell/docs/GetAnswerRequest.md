# GetAnswerRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The opaque ID of the Answer. | [optional] 
**DocId** | **String** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetAnswerRequest = Initialize-PSOpenAPIToolsGetAnswerRequest  -Id 3 `
 -DocId ANSWERS_answer_3
```

- Convert the resource to JSON
```powershell
$GetAnswerRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

