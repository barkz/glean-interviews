# InviteInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SignUpTime** | **System.DateTime** | The time this person signed up in ISO format (ISO 8601). | [optional] 
**Invites** | [**ChannelInviteInfo[]**](ChannelInviteInfo.md) | Latest invites received by the user for each channel | [optional] 
**Inviter** | [**Person**](Person.md) |  | [optional] 
**InviteTime** | **System.DateTime** | The time this person was invited in ISO format (ISO 8601). | [optional] 
**ReminderTime** | **System.DateTime** | The time this person was reminded in ISO format (ISO 8601) if a reminder was sent. | [optional] 

## Examples

- Prepare the resource
```powershell
$InviteInfo = Initialize-PSOpenAPIToolsInviteInfo  -SignUpTime null `
 -Invites null `
 -Inviter null `
 -InviteTime null `
 -ReminderTime null
```

- Convert the resource to JSON
```powershell
$InviteInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

