# AiInsightsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastLogTimestamp** | **Int32** | Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC). | [optional] 
**AssistantInsights** | [**UserActivityInsight[]**](UserActivityInsight.md) |  | [optional] 
**TotalActiveAssistantUsers** | **Int32** | Total number of Active Assistant users (chat, summary, AIA) in requested period. | [optional] 
**TotalChatMessages** | **Int32** | Total number of Chat messages sent in requested period. | [optional] 
**TotalAiSummarizations** | **Int32** | Total number of AI Document Summarizations invoked in the requested period. | [optional] 
**TotalAiAnswers** | **Int32** | Total number of AI Answers generated in the requested period. | [optional] 
**TotalUpvotes** | **Int32** | Total number of Chat messages which received upvotes by the user. | [optional] 
**TotalDownvotes** | **Int32** | Total number of Chat messages which received downvotes by the user. | [optional] 
**TotalGleanbotResponses** | **Int32** | Total number of Gleanbot responses, both proactive and reactive. | [optional] 
**TotalGleanbotResponsesShared** | **Int32** | Total number of Gleanbot responses shared publicly (upvoted). | [optional] 
**TotalGleanbotResponsesNotHelpful** | **Int32** | Total number of Glean responses rejected as not helpful (downvoted). | [optional] 
**Departments** | **String[]** | list of departments applicable for users tab. | [optional] 

## Examples

- Prepare the resource
```powershell
$AiInsightsResponse = Initialize-PSOpenAPIToolsAiInsightsResponse  -LastLogTimestamp null `
 -AssistantInsights null `
 -TotalActiveAssistantUsers null `
 -TotalChatMessages null `
 -TotalAiSummarizations null `
 -TotalAiAnswers null `
 -TotalUpvotes null `
 -TotalDownvotes null `
 -TotalGleanbotResponses null `
 -TotalGleanbotResponsesShared null `
 -TotalGleanbotResponsesNotHelpful null `
 -Departments null
```

- Convert the resource to JSON
```powershell
$AiInsightsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

