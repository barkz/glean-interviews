# PersonSuggestionList
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | [**PeopleSuggestionCategory**](PeopleSuggestionCategory.md) |  | 
**People** | [**Person[]**](Person.md) | Information about suggested users. | [optional] 

## Examples

- Prepare the resource
```powershell
$PersonSuggestionList = Initialize-PSOpenAPIToolsPersonSuggestionList  -Category null `
 -People null
```

- Convert the resource to JSON
```powershell
$PersonSuggestionList | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

