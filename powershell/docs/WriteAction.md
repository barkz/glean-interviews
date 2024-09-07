# WriteAction
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolName** | **String** | The name of the tool. | [optional] 
**ToolConfig** | [**ToolConfig**](ToolConfig.md) |  | [optional] 
**RedirectUrl** | **String** | If a &#x60;REDIRECT&#x60; action, the URL to visit to execute the action. | [optional] 
**Parameters** | [**System.Collections.Hashtable**](WriteActionParameter.md) | The parameters to be passed to the redirect URL for actions. | [optional] 

## Examples

- Prepare the resource
```powershell
$WriteAction = Initialize-PSOpenAPIToolsWriteAction  -ToolName null `
 -ToolConfig null `
 -RedirectUrl null `
 -Parameters null
```

- Convert the resource to JSON
```powershell
$WriteAction | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

