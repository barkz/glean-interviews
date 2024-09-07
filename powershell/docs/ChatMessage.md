# ChatMessage
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentConfig** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**Author** | **String** |  | [optional] [default to "USER"]
**Citations** | [**ChatMessageCitation[]**](ChatMessageCitation.md) | A list of Citations used to generate the message. | [optional] 
**UploadedFileIds** | **String[]** | IDs of files uploaded in the message that are referenced to generate the answer. | [optional] 
**Fragments** | [**ChatMessageFragment[]**](ChatMessageFragment.md) | A list of chat results. | [optional] 
**Metadata** | **String** | Metadata associated with the message (not displayed to the user but stored in the app). | [optional] 
**Ts** | **String** | Timestamp of the message. | [optional] 
**MessageId** | **String** | Unique ID of the message. | [optional] 
**MessageTrackingToken** | **String** | Opaque tracking token generated server-side. | [optional] 
**MessageType** | **String** | Used to determine the type of UI treatment to apply to this message. | [optional] 
**HasMoreFragments** | **Boolean** | Signals there are more fragments incoming. | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatMessage = Initialize-PSOpenAPIToolsChatMessage  -AgentConfig null `
 -Author null `
 -Citations null `
 -UploadedFileIds null `
 -Fragments null `
 -Metadata null `
 -Ts null `
 -MessageId null `
 -MessageTrackingToken null `
 -MessageType null `
 -HasMoreFragments null
```

- Convert the resource to JSON
```powershell
$ChatMessage | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

