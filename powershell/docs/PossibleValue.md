# PossibleValue
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | **String** | Possible value | [optional] 
**Label** | **String** | User-friendly label associated with the value | [optional] 

## Examples

- Prepare the resource
```powershell
$PossibleValue = Initialize-PSOpenAPIToolsPossibleValue  -Value null `
 -Label null
```

- Convert the resource to JSON
```powershell
$PossibleValue | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

