# ChatResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Messages** | [**ChatMessage[]**](ChatMessage.md) |  | [optional] 
**ChatId** | **String** | The id of the associated Chat the messages belong to, if one exists. | [optional] 
**FollowUpPrompts** | **String[]** | Follow-up prompts for the user to potentially use | [optional] 
**BackendTimeMillis** | **Int64** | Time in milliseconds the backend took to respond to the request. | [optional] 
**ChatSessionTrackingToken** | **String** | A token that is used to track the session. | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatResponse = Initialize-PSOpenAPIToolsChatResponse  -Messages null `
 -ChatId null `
 -FollowUpPrompts null `
 -BackendTimeMillis 1100 `
 -ChatSessionTrackingToken null
```

- Convert the resource to JSON
```powershell
$ChatResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

