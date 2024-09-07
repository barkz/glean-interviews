# Themes
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Light** | **System.Collections.Hashtable** | A map of {string, string} pairs where the key represents a known theme option and the value is the CSS color to apply. Supported options are documented in https://dev.glean.com/meta/browser_api/interfaces/Theme.html. | [optional] 
**Dark** | **System.Collections.Hashtable** | A map of {string, string} pairs where the key represents a known theme option and the value is the CSS color to apply. Supported options are documented in https://dev.glean.com/meta/browser_api/interfaces/Theme.html. | [optional] 

## Examples

- Prepare the resource
```powershell
$Themes = Initialize-PSOpenAPIToolsThemes  -Light {&quot;background&quot;:&quot;#fafafa&quot;,&quot;textPrimary&quot;:&quot;#1e1e1e&quot;} `
 -Dark {&quot;background&quot;:&quot;#fafafa&quot;,&quot;textPrimary&quot;:&quot;#1e1e1e&quot;}
```

- Convert the resource to JSON
```powershell
$Themes | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

