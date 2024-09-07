# CustomFieldValue
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StrText** | **String** | Text field for string value. | [optional] 
**UrlAnchor** | **String** | Anchor text for hyperlink. | [optional] 
**UrlLink** | **String** | Link for this URL. | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomFieldValue = Initialize-PSOpenAPIToolsCustomFieldValue  -StrText null `
 -UrlAnchor null `
 -UrlLink null `
 -Person null
```

- Convert the resource to JSON
```powershell
$CustomFieldValue | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

