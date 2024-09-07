# OperatorMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** |  | 
**IsCustom** | **Boolean** | Whether this operator is supported by default or something that was created within a workplace app (e.g. custom jira field). | [optional] 
**OperatorType** | **String** |  | [optional] 
**HelpText** | **String** |  | [optional] 
**Scopes** | [**OperatorScope[]**](OperatorScope.md) |  | [optional] 
**Value** | **String** | Raw/canonical value of the operator. Only applies when result is an operator value. | [optional] 
**DisplayValue** | **String** | Human readable value of the operator that can be shown to the user. Only applies when result is an operator value. | [optional] 

## Examples

- Prepare the resource
```powershell
$OperatorMetadata = Initialize-PSOpenAPIToolsOperatorMetadata  -Name null `
 -IsCustom null `
 -OperatorType null `
 -HelpText null `
 -Scopes null `
 -Value null `
 -DisplayValue null
```

- Convert the resource to JSON
```powershell
$OperatorMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

