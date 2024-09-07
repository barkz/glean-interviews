# ReminderRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentId** | **String** | The document which the verification is for new reminders and/or update. | 
**Assignee** | **String** | The obfuscated id of the person this verification is assigned to. | [optional] 
**RemindInDays** | **Int32** | Reminder for the next verifications in terms of days. For deletion, this will be omitted. | [optional] 
**Reason** | **String** | An optional free-text reason for the reminder. This is particularly useful when a reminder is used to ask for verification from another user (for example, &quot;&quot;Duplicate&quot;&quot;, &quot;&quot;Incomplete&quot;&quot;, &quot;&quot;Incorrect&quot;&quot;). | [optional] 

## Examples

- Prepare the resource
```powershell
$ReminderRequest = Initialize-PSOpenAPIToolsReminderRequest  -DocumentId null `
 -Assignee null `
 -RemindInDays null `
 -Reason null
```

- Convert the resource to JSON
```powershell
$ReminderRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

