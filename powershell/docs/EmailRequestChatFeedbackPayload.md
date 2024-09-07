# EmailRequestChatFeedbackPayload
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rating** | **String** | Rating given to the conversation (currently either &quot;&quot;upvoted&quot;&quot; or &quot;&quot;downvoted&quot;&quot;). | [optional] 
**Comments** | **String** | Additional freeform comments provided by the reporter. | [optional] 
**PreviousMessages** | **String[]** | Previous messages in this conversation. | [optional] 

## Examples

- Prepare the resource
```powershell
$EmailRequestChatFeedbackPayload = Initialize-PSOpenAPIToolsEmailRequestChatFeedbackPayload  -Rating null `
 -Comments null `
 -PreviousMessages null
```

- Convert the resource to JSON
```powershell
$EmailRequestChatFeedbackPayload | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

