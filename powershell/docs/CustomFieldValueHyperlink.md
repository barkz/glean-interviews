# CustomFieldValueHyperlink
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UrlAnchor** | **String** | Anchor text for hyperlink. | [optional] 
**UrlLink** | **String** | Link for this URL. | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomFieldValueHyperlink = Initialize-PSOpenAPIToolsCustomFieldValueHyperlink  -UrlAnchor null `
 -UrlLink null
```

- Convert the resource to JSON
```powershell
$CustomFieldValueHyperlink | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

