# StructuredText
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Text** | **String** |  | 
**StructuredList** | [**StructuredTextItem[]**](StructuredTextItem.md) | An array of objects each of which contains either a string or a link which optionally corresponds to a document. | [optional] 

## Examples

- Prepare the resource
```powershell
$StructuredText = Initialize-PSOpenAPIToolsStructuredText  -Text From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light. `
 -StructuredList null
```

- Convert the resource to JSON
```powershell
$StructuredText | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

