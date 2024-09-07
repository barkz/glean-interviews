# AnswerLike
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**User** | [**Person**](Person.md) |  | [optional] 
**CreateTime** | **System.DateTime** | The time the user liked the answer in ISO format (ISO 8601). | [optional] 

## Examples

- Prepare the resource
```powershell
$AnswerLike = Initialize-PSOpenAPIToolsAnswerLike  -User null `
 -CreateTime null
```

- Convert the resource to JSON
```powershell
$AnswerLike | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

