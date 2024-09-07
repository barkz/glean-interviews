# StructuredTextItem
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Link** | **String** |  | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**Text** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$StructuredTextItem = Initialize-PSOpenAPIToolsStructuredTextItem  -Link https://en.wikipedia.org/wiki/Diffuse_sky_radiation `
 -Document null `
 -Text Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.
```

- Convert the resource to JSON
```powershell
$StructuredTextItem | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

