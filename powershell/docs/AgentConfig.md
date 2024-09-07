# AgentConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Agent** | **String** | Name of the agent. | [optional] 
**Mode** | **String** | Top level modes to run GleanChat in. | [optional] 

## Examples

- Prepare the resource
```powershell
$AgentConfig = Initialize-PSOpenAPIToolsAgentConfig  -Agent null `
 -Mode null
```

- Convert the resource to JSON
```powershell
$AgentConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

