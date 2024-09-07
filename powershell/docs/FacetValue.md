# FacetValue
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StringValue** | **String** | The value that should be set in the FacetFilter when applying this filter to a search request. | [optional] 
**IntegerValue** | **Int32** |  | [optional] 
**DisplayLabel** | **String** | An optional user-friendly label to display in place of the facet value. | [optional] 
**IconConfig** | [**IconConfig**](IconConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetValue = Initialize-PSOpenAPIToolsFacetValue  -StringValue engineering `
 -IntegerValue 5 `
 -DisplayLabel engineering `
 -IconConfig null
```

- Convert the resource to JSON
```powershell
$FacetValue | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

