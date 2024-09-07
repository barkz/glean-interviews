# PersonDistance
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The display name. | 
**ObfuscatedId** | **String** | An opaque identifier that can be used to request metadata for a Person. | 
**Distance** | **Double** | Distance to person, refer to PeopleDistance pipeline on interpretation of the value. | 

## Examples

- Prepare the resource
```powershell
$PersonDistance = Initialize-PSOpenAPIToolsPersonDistance  -Name null `
 -ObfuscatedId null `
 -Distance null
```

- Convert the resource to JSON
```powershell
$PersonDistance | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

