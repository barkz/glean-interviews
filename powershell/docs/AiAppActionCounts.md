# AiAppActionCounts
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TotalSlackbotResponses** | **Int32** | Total number of Slackbot responses, both proactive and reactive. | [optional] 
**TotalSlackbotResponsesShared** | **Int32** | Total number of Slackbot responses shared publicly (upvoted). | [optional] 
**TotalSlackbotResponsesNotHelpful** | **Int32** | Total number of Slackbot responses rejected as not helpful (downvoted). | [optional] 
**TotalChatMessages** | **Int32** | Total number of Chat messages sent in requested period. | [optional] 
**TotalUpvotes** | **Int32** | Total number of Chat messages which received upvotes by the user. | [optional] 
**TotalDownvotes** | **Int32** | Total number of Chat messages which received downvotes by the user. | [optional] 

## Examples

- Prepare the resource
```powershell
$AiAppActionCounts = Initialize-PSOpenAPIToolsAiAppActionCounts  -TotalSlackbotResponses null `
 -TotalSlackbotResponsesShared null `
 -TotalSlackbotResponsesNotHelpful null `
 -TotalChatMessages null `
 -TotalUpvotes null `
 -TotalDownvotes null
```

- Convert the resource to JSON
```powershell
$AiAppActionCounts | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

