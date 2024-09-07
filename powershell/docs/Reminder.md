# Reminder
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assignee** | [**Person**](Person.md) |  | 
**Requestor** | [**Person**](Person.md) |  | [optional] 
**RemindAt** | **Int32** | Unix timestamp for when the reminder should trigger (in seconds since epoch UTC). | 
**CreatedAt** | **Int32** | Unix timestamp for when the reminder was first created (in seconds since epoch UTC). | [optional] 
**Reason** | **String** | An optional free-text reason for the reminder. This is particularly useful when a reminder is used to ask for verification from another user (for example, &quot;&quot;Duplicate&quot;&quot;, &quot;&quot;Incomplete&quot;&quot;, &quot;&quot;Incorrect&quot;&quot;). | [optional] 

## Examples

- Prepare the resource
```powershell
$Reminder = Initialize-PSOpenAPIToolsReminder  -Assignee null `
 -Requestor null `
 -RemindAt null `
 -CreatedAt null `
 -Reason null
```

- Convert the resource to JSON
```powershell
$Reminder | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

