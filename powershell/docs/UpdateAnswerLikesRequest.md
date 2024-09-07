# UpdateAnswerLikesRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AnswerId** | **Int32** | The opaque id of the answer to like. | 
**AnswerDocId** | **String** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID is unavailable. If both are available, using the Answer ID is preferred. | [optional] 
**Action** | **String** |  | 

## Examples

- Prepare the resource
```powershell
$UpdateAnswerLikesRequest = Initialize-PSOpenAPIToolsUpdateAnswerLikesRequest  -AnswerId 3 `
 -AnswerDocId ANSWERS_answer_3 `
 -Action null
```

- Convert the resource to JSON
```powershell
$UpdateAnswerLikesRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

