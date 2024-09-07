# ToolsConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvailableTools** | [**ToolMetadata[]**](ToolMetadata.md) | List of tools available to the user. | [optional] 

## Examples

- Prepare the resource
```powershell
$ToolsConfig = Initialize-PSOpenAPIToolsToolsConfig  -AvailableTools null
```

- Convert the resource to JSON
```powershell
$ToolsConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

