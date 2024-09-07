# Quicklink
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | Full action name. Used in autocomplete. | [optional] 
**ShortName** | **String** | Shortened name. Used in app cards. | [optional] 
**Url** | **String** | The URL of the action. | [optional] 
**IconConfig** | [**IconConfig**](IconConfig.md) |  | [optional] 
**Id** | **String** | Unique identifier of this quicklink | [optional] 
**Scopes** | **String[]** | The scopes for which this quicklink is applicable | [optional] 

## Examples

- Prepare the resource
```powershell
$Quicklink = Initialize-PSOpenAPIToolsQuicklink  -Name null `
 -ShortName null `
 -Url null `
 -IconConfig null `
 -Id null `
 -Scopes null
```

- Convert the resource to JSON
```powershell
$Quicklink | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

