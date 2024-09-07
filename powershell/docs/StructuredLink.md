# StructuredLink
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The display name for the link | [optional] 
**Url** | **String** | The URL for the link. | [optional] 
**IconConfig** | [**IconConfig**](IconConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$StructuredLink = Initialize-PSOpenAPIToolsStructuredLink  -Name null `
 -Url null `
 -IconConfig null
```

- Convert the resource to JSON
```powershell
$StructuredLink | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

