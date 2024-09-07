# InvalidOperatorValueError
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **String** | The operator key that has an invalid value. | [optional] 
**Value** | **String** | The invalid operator value. | [optional] 

## Examples

- Prepare the resource
```powershell
$InvalidOperatorValueError = Initialize-PSOpenAPIToolsInvalidOperatorValueError  -Key null `
 -Value null
```

- Convert the resource to JSON
```powershell
$InvalidOperatorValueError | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

