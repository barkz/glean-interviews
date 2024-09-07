# PinDocument
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | **String[]** | The query strings for which the pinned result will show. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 
**Id** | **String** | The opaque id of the pin. | [optional] 
**DocumentId** | **String** | The document which should be a pinned result. | 
**Attribution** | [**Person**](Person.md) |  | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**CreateTime** | **System.DateTime** |  | [optional] 
**UpdateTime** | **System.DateTime** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PinDocument = Initialize-PSOpenAPIToolsPinDocument  -Queries null `
 -AudienceFilters null `
 -Id null `
 -DocumentId null `
 -Attribution null `
 -UpdatedBy null `
 -CreateTime null `
 -UpdateTime null
```

- Convert the resource to JSON
```powershell
$PinDocument | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

