# OperatorScope
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** |  | [optional] 
**DocType** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$OperatorScope = Initialize-PSOpenAPIToolsOperatorScope  -Datasource null `
 -DocType null
```

- Convert the resource to JSON
```powershell
$OperatorScope | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

