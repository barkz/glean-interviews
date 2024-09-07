# Branding
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CompanyBackgroundImageName** | **String** | User facing company background image to be displayed to users on the home page. | [optional] 
**CompanyLogoUrl** | **String** | An image URL pointing to a custom logo that should be displayed to users. Must be square and recognizable down to 40x40px. SVG images with transparent background are preferred. | [optional] 
**CompanyWideLogoUrl** | **String** | An image URL pointing to a wide format custom logo that should be displayed to users. Should be rectangular and recognizable at 40px height, and aspect ratio should be between 2:1 and 4:1. SVG images with transparent background are preferred. | [optional] 
**CompanyLogoBackgroundColor** | **String** | A hex RGB color to display behind custom logo (e.g. &#39;#ff4080&#39;). | [optional] 

## Examples

- Prepare the resource
```powershell
$Branding = Initialize-PSOpenAPIToolsBranding  -CompanyBackgroundImageName null `
 -CompanyLogoUrl null `
 -CompanyWideLogoUrl null `
 -CompanyLogoBackgroundColor null
```

- Convert the resource to JSON
```powershell
$Branding | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

