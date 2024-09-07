# VerificationMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastVerifier** | [**Person**](Person.md) |  | [optional] 
**LastVerificationTs** | **Int32** | The unix timestamp of the verification (in seconds since epoch UTC). | [optional] 
**ExpirationTs** | **Int32** | The unix timestamp of the verification expiration if applicable (in seconds since epoch UTC). | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**Reminders** | [**Reminder[]**](Reminder.md) | Info about all outstanding verification reminders for the document if exists. | [optional] 
**LastReminder** | [**Reminder**](Reminder.md) |  | [optional] 
**VisitorCount** | [**CountInfo[]**](CountInfo.md) | Number of visitors to the document during included time periods. | [optional] 
**CandidateVerifiers** | [**Person[]**](Person.md) | List of potential verifiers for the document e.g. old verifiers and/or users with view/edit permissions. | [optional] 

## Examples

- Prepare the resource
```powershell
$VerificationMetadata = Initialize-PSOpenAPIToolsVerificationMetadata  -LastVerifier null `
 -LastVerificationTs null `
 -ExpirationTs null `
 -Document null `
 -Reminders null `
 -LastReminder null `
 -VisitorCount null `
 -CandidateVerifiers null
```

- Convert the resource to JSON
```powershell
$VerificationMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

