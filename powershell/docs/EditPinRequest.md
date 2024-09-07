# EditPinRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | **String[]** | The query strings for which the pinned result will show. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 
**Id** | **String** | The opaque id of the pin to be edited. | [optional] 

## Examples

- Prepare the resource
```powershell
$EditPinRequest = Initialize-PSOpenAPIToolsEditPinRequest  -Queries null `
 -AudienceFilters null `
 -Id null
```

- Convert the resource to JSON
```powershell
$EditPinRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

