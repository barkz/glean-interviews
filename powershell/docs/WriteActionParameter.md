# WriteActionParameter
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **String** | The type of the value (e.g., integer, string, etc.) | [optional] 
**DisplayName** | **String** | Human readable display name for the key. | [optional] 
**Value** | **String** | The value of the field. | [optional] 
**Label** | **String** | User-friendly label associated with the value. | [optional] 
**IsRequired** | **Boolean** | Is the parameter a required field. | [optional] 
**Description** | **String** | Description of the parameter. | [optional] 
**PossibleValues** | [**PossibleValue[]**](PossibleValue.md) | Possible values that the parameter can take. | [optional] 

## Examples

- Prepare the resource
```powershell
$WriteActionParameter = Initialize-PSOpenAPIToolsWriteActionParameter  -Type null `
 -DisplayName null `
 -Value null `
 -Label null `
 -IsRequired null `
 -Description null `
 -PossibleValues null
```

- Convert the resource to JSON
```powershell
$WriteActionParameter | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

