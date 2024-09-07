# Chat
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Messages** | [**ChatMessage[]**](ChatMessage.md) | The chat messages within a Chat. | [optional] 
**Id** | **String** | The opaque id of the Chat. | [optional] 
**CreateTime** | **Int32** | Server Unix timestamp of the creation time (in seconds since epoch UTC). | [optional] 
**CreatedBy** | [**Person**](Person.md) |  | [optional] 
**UpdateTime** | **Int32** | Server Unix timestamp of the update time (in seconds since epoch UTC). | [optional] 
**Name** | **String** | The name of the Chat. | [optional] 
**ApplicationId** | **String** | The ID of the AI App that this Chat is associated to. | [optional] 

## Examples

- Prepare the resource
```powershell
$Chat = Initialize-PSOpenAPIToolsChat  -Messages null `
 -Id null `
 -CreateTime null `
 -CreatedBy null `
 -UpdateTime null `
 -Name null `
 -ApplicationId null
```

- Convert the resource to JSON
```powershell
$Chat | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

