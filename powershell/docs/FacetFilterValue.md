# FacetFilterValue
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | **String** |  | [optional] 
**RelationType** | **String** |  | [optional] 
**IsNegated** | **Boolean** | DEPRECATED - please use relationType instead | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetFilterValue = Initialize-PSOpenAPIToolsFacetFilterValue  -Value Spreadsheet `
 -RelationType EQUALS `
 -IsNegated null
```

- Convert the resource to JSON
```powershell
$FacetFilterValue | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

