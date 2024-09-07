# CustomDataValue
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DisplayLabel** | **String** |  | [optional] 
**StringValue** | **String** |  | [optional] 
**StringListValue** | **String[]** | list of strings for multi-value properties | [optional] 
**NumberValue** | **Decimal** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomDataValue = Initialize-PSOpenAPIToolsCustomDataValue  -DisplayLabel null `
 -StringValue null `
 -StringListValue null `
 -NumberValue null
```

- Convert the resource to JSON
```powershell
$CustomDataValue | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

