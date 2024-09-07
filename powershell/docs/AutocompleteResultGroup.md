# AutocompleteResultGroup
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartIndex** | **Int32** | The inclusive start index of the range. | [optional] 
**EndIndex** | **Int32** | The exclusive end index of the range. | [optional] 
**Title** | **String** | The title of the result group to be displayed. Empty means no title. | [optional] 

## Examples

- Prepare the resource
```powershell
$AutocompleteResultGroup = Initialize-PSOpenAPIToolsAutocompleteResultGroup  -StartIndex null `
 -EndIndex null `
 -Title null
```

- Convert the resource to JSON
```powershell
$AutocompleteResultGroup | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

