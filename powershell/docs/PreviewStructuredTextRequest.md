# PreviewStructuredTextRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Text** | **String** |  | 

## Examples

- Prepare the resource
```powershell
$PreviewStructuredTextRequest = Initialize-PSOpenAPIToolsPreviewStructuredTextRequest  -Text From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.
```

- Convert the resource to JSON
```powershell
$PreviewStructuredTextRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

