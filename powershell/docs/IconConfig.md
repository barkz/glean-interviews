# IconConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GeneratedBackgroundColorKey** | **String** |  | [optional] 
**BackgroundColor** | **String** |  | [optional] 
**Color** | **String** |  | [optional] 
**Key** | **String** |  | [optional] 
**IconType** | **String** |  | [optional] 
**Masked** | **Boolean** | Whether the icon should be masked based on current theme. | [optional] 
**Name** | **String** | The name of the icon if applicable, e.g. the glyph name for &#x60;IconType.GLYPH&#x60; icons. | [optional] 
**Url** | **String** | The URL to an image to be displayed if applicable, e.g. the URL for &#x60;iconType.URL&#x60; icons. | [optional] 

## Examples

- Prepare the resource
```powershell
$IconConfig = Initialize-PSOpenAPIToolsIconConfig  -GeneratedBackgroundColorKey null `
 -BackgroundColor null `
 -Color null `
 -Key null `
 -IconType null `
 -Masked null `
 -Name null `
 -Url null
```

- Convert the resource to JSON
```powershell
$IconConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

