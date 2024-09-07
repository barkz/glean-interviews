# EventClassification
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | [**EventClassificationName**](EventClassificationName.md) |  | [optional] 
**Strategies** | [**EventStrategyName[]**](EventStrategyName.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$EventClassification = Initialize-PSOpenAPIToolsEventClassification  -Name null `
 -Strategies null
```

- Convert the resource to JSON
```powershell
$EventClassification | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

