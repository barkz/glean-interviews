# Feedback
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | Universally unique identifier of the event. To allow for reliable retransmission, only the earliest received event of a given UUID is considered valid by the server and subsequent are ignored. | [optional] 
**Category** | **String** | The feature category to which the feedback applies. These should be broad product areas such as Announcements, Answers, Search, etc. rather than specific components or UI treatments within those areas. | [optional] 
**TrackingTokens** | **String[]** | A list of server-generated trackingTokens to which this event applies. | 
**VarEvent** | **String** | The action the user took within a Glean client with respect to the object referred to by the given &#x60;trackingToken&#x60;. | 
**Position** | **Int32** | Position of the element in the case that the client controls order (such as feed and autocomplete). | [optional] 
**Payload** | **String** | For type MANUAL_FEEDBACK, contains string of user feedback. For autocomplete, partial query string. For feed, string of user feedback in addition to manual feedback signals extracted from all suggested content. | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**Timestamp** | **System.DateTime** | The ISO 8601 timestamp when the event occured. | [optional] 
**User** | [**User**](User.md) |  | [optional] 
**Pathname** | **String** | The path the client was at when the feedback event triggered. | [optional] 
**Channels** | **String[]** | Where the feedback will be sent, e.g. to Glean, the user&#39;s company, or both. If no channels are specified, feedback will go only to Glean. | [optional] 
**Url** | **String** | The URL the client was at when the feedback event triggered. | [optional] 
**UiElement** | **String** | The UI element associated with the event, if any. | [optional] 
**ManualFeedbackInfo** | [**ManualFeedbackInfo**](ManualFeedbackInfo.md) |  | [optional] 
**SeenFeedbackInfo** | [**SeenFeedbackInfo**](SeenFeedbackInfo.md) |  | [optional] 
**UserViewInfo** | [**UserViewInfo**](UserViewInfo.md) |  | [optional] 
**DebugInfo** | [**FeedbackDebugInfo**](FeedbackDebugInfo.md) |  | [optional] 
**ApplicationId** | **String** | The application ID of the client that sent the feedback event. | [optional] 

## Examples

- Prepare the resource
```powershell
$Feedback = Initialize-PSOpenAPIToolsFeedback  -Id null `
 -Category null `
 -TrackingTokens null `
 -VarEvent null `
 -Position null `
 -Payload null `
 -SessionInfo null `
 -Timestamp null `
 -User null `
 -Pathname null `
 -Channels null `
 -Url null `
 -UiElement null `
 -ManualFeedbackInfo null `
 -SeenFeedbackInfo null `
 -UserViewInfo null `
 -DebugInfo null `
 -ApplicationId null
```

- Convert the resource to JSON
```powershell
$Feedback | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

