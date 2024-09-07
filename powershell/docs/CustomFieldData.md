# CustomFieldData
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | **String** | A user-facing label for this field. | 
**Values** | [**CustomFieldValue[]**](CustomFieldValue.md) |  | 
**Displayable** | **Boolean** | Determines whether the client should display this custom field | [default to $true]

## Examples

- Prepare the resource
```powershell
$CustomFieldData = Initialize-PSOpenAPIToolsCustomFieldData  -Label null `
 -Values null `
 -Displayable null
```

- Convert the resource to JSON
```powershell
$CustomFieldData | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

