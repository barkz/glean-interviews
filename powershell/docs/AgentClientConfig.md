# AgentClientConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentConfig** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**InputCharLimit** | **Int32** | The character limit of an input to GleanChat under the specified AgentConfig. | [optional] 

## Examples

- Prepare the resource
```powershell
$AgentClientConfig = Initialize-PSOpenAPIToolsAgentClientConfig  -AgentConfig null `
 -InputCharLimit null
```

- Convert the resource to JSON
```powershell
$AgentClientConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

