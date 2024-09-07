# AssistantConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChatBannerText** | **String** | Disclaimer message to be displayed as a banner on top of chat. This could be in markdown format with &quot;&quot;\n&quot;&quot; between each line. | [optional] 
**ChatBoxDisclaimer** | **String** | Disclaimer message to be displayed below the chat box. This could be in markdown format. | [optional] 
**ChatLinkUrlTemplate** | **String** | The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat. | [optional] 
**ChatStarterHeader** | **String** | Label for the chat header during initial state. | [optional] 
**ChatStarterSubheader** | **String** | Label for the chat subheader during initial state. | [optional] 
**AgentClientConfigs** | [**AgentClientConfig[]**](AgentClientConfig.md) |  | [optional] 
**RedlistedDatasources** | **String[]** | A list of datasources that are disabled in Chat | [optional] 
**GreenlistedDatasourceInstances** | **String[]** | A list of datasources that are always visible in Chat | [optional] 
**GptAgentEnabled** | **Boolean** | Whether the GPT agent (general mode) for Chat is enabled | [optional] 
**FileUploadEnabled** | **Boolean** | Whether file upload for Chat is enabled for the deployment | [optional] 
**ChatHistoryEnabled** | **Boolean** | Whether the chat history for Chat is enabled for the deployment | [optional] 
**ChatGuideUrl** | **String** | Redirect URL for &quot;&quot;Chat guide&quot;&quot; in the default chat starter subheader | [optional] 

## Examples

- Prepare the resource
```powershell
$AssistantConfig = Initialize-PSOpenAPIToolsAssistantConfig  -ChatBannerText null `
 -ChatBoxDisclaimer null `
 -ChatLinkUrlTemplate null `
 -ChatStarterHeader null `
 -ChatStarterSubheader null `
 -AgentClientConfigs null `
 -RedlistedDatasources null `
 -GreenlistedDatasourceInstances null `
 -GptAgentEnabled null `
 -FileUploadEnabled null `
 -ChatHistoryEnabled null `
 -ChatGuideUrl null
```

- Convert the resource to JSON
```powershell
$AssistantConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

