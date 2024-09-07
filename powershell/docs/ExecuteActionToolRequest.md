# ExecuteActionToolRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The name of the tool. | 
**Parameters** | [**System.Collections.Hashtable**](WriteActionParameter.md) | The parameters to be passed to the tool for action. | [optional] 

## Examples

- Prepare the resource
```powershell
$ExecuteActionToolRequest = Initialize-PSOpenAPIToolsExecuteActionToolRequest  -Name null `
 -Parameters null
```

- Convert the resource to JSON
```powershell
$ExecuteActionToolRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

