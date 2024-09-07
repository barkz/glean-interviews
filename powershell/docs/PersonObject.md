# PersonObject
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The display name. | 
**ObfuscatedId** | **String** | An opaque identifier that can be used to request metadata for a Person. | 

## Examples

- Prepare the resource
```powershell
$PersonObject = Initialize-PSOpenAPIToolsPersonObject  -Name null `
 -ObfuscatedId null
```

- Convert the resource to JSON
```powershell
$PersonObject | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

