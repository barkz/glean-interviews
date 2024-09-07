# AnswerDocId
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocId** | **String** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnswerDocId = Initialize-PSOpenAPIToolsAnswerDocId  -DocId ANSWERS_answer_3
```

- Convert the resource to JSON
```powershell
$AnswerDocId | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

