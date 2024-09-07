# RestrictionFilters
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentSpecs** | [**DocumentSpec[]**](DocumentSpec.md) |  | [optional] 
**DatasourceInstances** | **String[]** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$RestrictionFilters = Initialize-PSOpenAPIToolsRestrictionFilters  -DocumentSpecs null `
 -DatasourceInstances null
```

- Convert the resource to JSON
```powershell
$RestrictionFilters | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

