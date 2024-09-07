# EmailRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EmailTemplate** | [**CommunicationTemplate**](CommunicationTemplate.md) |  | 
**AlertData** | [**AlertData**](AlertData.md) |  | [optional] 
**Recipients** | [**Person[]**](Person.md) | The people to send emails to | [optional] 
**RecipientFilters** | [**PeopleFilters**](PeopleFilters.md) |  | [optional] 
**CompanyName** | **String** | Name of the company. | [optional] 
**DatasourceInstance** | **String** | The instance ID of the datasource (if any) | [optional] 
**Senders** | [**Person[]**](Person.md) | The people who triggered this email | [optional] 
**WebAppUrl** | **String** | The URL of the client triggering the request, as received in the ClientConfig | [optional] 
**ServerUrl** | **String** | The URL of the QE instance the email request is processed by. | [optional] 
**UnsubscribeUrl** | **String** | The URL to unsubscribe from emails. | [optional] 
**Documents** | [**Document[]**](Document.md) | The documents this email request refers to | [optional] 
**Reasons** | **String[]** | Reasons this email request was sent. Will be shown directly to end user. | [optional] 
**Blocks** | [**System.Collections.Hashtable**](Array.md) | For building complex email UIs, we use a block structure that dictates what we create in the UI | [optional] 
**Subjects** | **System.Collections.Hashtable** | Mapping of recipientIds to the email subject they are to receive. Optional and only meant for templates with Sendgrid subject set to {{subject}} | [optional] 
**FeedbackPayload** | [**EmailRequestFeedbackPayload**](EmailRequestFeedbackPayload.md) |  | [optional] 
**ChatFeedbackPayload** | [**EmailRequestChatFeedbackPayload**](EmailRequestChatFeedbackPayload.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$EmailRequest = Initialize-PSOpenAPIToolsEmailRequest  -EmailTemplate null `
 -AlertData null `
 -Recipients null `
 -RecipientFilters null `
 -CompanyName null `
 -DatasourceInstance null `
 -Senders null `
 -WebAppUrl null `
 -ServerUrl null `
 -UnsubscribeUrl null `
 -Documents null `
 -Reasons null `
 -Blocks null `
 -Subjects null `
 -FeedbackPayload null `
 -ChatFeedbackPayload null
```

- Convert the resource to JSON
```powershell
$EmailRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

