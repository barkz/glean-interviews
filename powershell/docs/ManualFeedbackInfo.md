# ManualFeedbackInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **String** | The email address of the user who submitted the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**Source** | **String** | The source associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**Issue** | **String** | The issue the user indicated in the feedback. | [optional] 
**ImageUrls** | **String[]** | URLs of images uploaded by user when providing feedback | [optional] 
**Query** | **String** | The query associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**ObscuredQuery** | **String** | The query associated with the Feedback.event.MANUAL_FEEDBACK event, but obscured such that the vowels are replaced with special characters. For search feedback events only. | [optional] 
**ActiveTab** | **String** | Which tabs the user had chosen at the time of the Feedback.event.MANUAL_FEEDBACK event. For search feedback events only. | [optional] 
**Comments** | **String** | The comments users can optionally add to the Feedback.event.MANUAL_FEEDBACK events. | [optional] 
**SearchResults** | **String[]** | The array of search result Glean Document IDs, ordered by top to bottom result. | [optional] 
**PreviousMessages** | **String[]** | The array of previous messages in a chat session, ordered by oldest to newest. | [optional] 
**NumQueriesFromFirstRun** | **Int32** | How many times this query has been run in the past. | [optional] 
**Vote** | **String** | The vote associated with the Feedback.event.MANUAL_FEEDBACK event. | [optional] 
**Rating** | **Int32** | A rating associated with the user feedback. The value will be between one and the maximum given by ratingScale, inclusive. | [optional] 
**RatingKey** | **String** | A description of the rating that contextualizes how it appeared to the user, e.g. &quot;&quot;satisfied&quot;&quot;. | [optional] 
**RatingScale** | **Int32** | The scale of comparison for a rating associated with the feedback. Rating values start from one and go up to the maximum specified by ratingScale. For example, a five-option satisfaction rating will have a ratingScale of 5 and a thumbs-up/thumbs-down rating will have a ratingScale of 2. | [optional] 

## Examples

- Prepare the resource
```powershell
$ManualFeedbackInfo = Initialize-PSOpenAPIToolsManualFeedbackInfo  -Email null `
 -Source null `
 -Issue null `
 -ImageUrls null `
 -Query null `
 -ObscuredQuery null `
 -ActiveTab null `
 -Comments null `
 -SearchResults null `
 -PreviousMessages null `
 -NumQueriesFromFirstRun null `
 -Vote null `
 -Rating null `
 -RatingKey null `
 -RatingScale null
```

- Convert the resource to JSON
```powershell
$ManualFeedbackInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

