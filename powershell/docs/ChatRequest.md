# ChatRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SaveChat** | **Boolean** | Save the current interaction as a Chat for the user to access later. | [optional] 
**ChatId** | **String** | The id of the Chat that this message should be added to. An empty id signifies creating a new Chat if saveChat is true. | [optional] 
**Messages** | [**ChatMessage[]**](ChatMessage.md) | A list of chat messages, from most recent to least recent. It can be assumed that the first chat message in the list is the user&#39;s most recent query. | 
**AgentConfig** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**Inclusions** | [**RestrictionFilters**](RestrictionFilters.md) |  | [optional] 
**Exclusions** | [**RestrictionFilters**](RestrictionFilters.md) |  | [optional] 
**TimeoutMillis** | **Int32** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**ApplicationId** | **String** | The ID of the application this request originates from, used to determine the configuration of underlying chat processes. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used. | [optional] 
**Stream** | **Boolean** | Whether to stream responses as they become available. If false, the entire response will be returned at once. Note if true and the model being used does not support streaming, the model&#39;s response will not be streamed but other messages from the endpoint still will. | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatRequest = Initialize-PSOpenAPIToolsChatRequest  -SaveChat null `
 -ChatId null `
 -Messages null `
 -AgentConfig null `
 -Inclusions null `
 -Exclusions null `
 -TimeoutMillis 30000 `
 -ApplicationId null `
 -Stream null
```

- Convert the resource to JSON
```powershell
$ChatRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

