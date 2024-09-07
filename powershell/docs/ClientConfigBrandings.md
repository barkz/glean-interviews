# ClientConfigBrandings
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Light** | [**Branding**](Branding.md) |  | [optional] 
**Dark** | [**Branding**](Branding.md) |  | [optional] 
**ProductTerms** | [**ProductTerms**](ProductTerms.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ClientConfigBrandings = Initialize-PSOpenAPIToolsClientConfigBrandings  -Light null `
 -Dark null `
 -ProductTerms null
```

- Convert the resource to JSON
```powershell
$ClientConfigBrandings | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

