# PublicConfigRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ThemeKeys** | **String[]** | A list of theme keys to include in the response. | [optional] 
**BoolKeys** | **String[]** | A list of boolean flag keys to include in the response. | [optional] 

## Examples

- Prepare the resource
```powershell
$PublicConfigRequest = Initialize-PSOpenAPIToolsPublicConfigRequest  -ThemeKeys null `
 -BoolKeys null
```

- Convert the resource to JSON
```powershell
$PublicConfigRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

