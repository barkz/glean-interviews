# ChannelInviteInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Channel** | [**CommunicationChannel**](CommunicationChannel.md) |  | [optional] 
**IsAutoInvite** | **Boolean** | Bit that tracks if this invite was automatically sent or user-sent | [optional] 
**Inviter** | [**Person**](Person.md) |  | [optional] 
**InviteTime** | **System.DateTime** | The time this person was invited in ISO format (ISO 8601). | [optional] 
**ReminderTime** | **System.DateTime** | The time this person was reminded in ISO format (ISO 8601) if a reminder was sent. | [optional] 

## Examples

- Prepare the resource
```powershell
$ChannelInviteInfo = Initialize-PSOpenAPIToolsChannelInviteInfo  -Channel null `
 -IsAutoInvite null `
 -Inviter null `
 -InviteTime null `
 -ReminderTime null
```

- Convert the resource to JSON
```powershell
$ChannelInviteInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

