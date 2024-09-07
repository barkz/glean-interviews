# PeopleSuggestRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Categories** | [**PeopleSuggestionCategory[]**](PeopleSuggestionCategory.md) | Categories of data requested. Request can include single or multiple categories. | 
**Departments** | **String[]** | Departments that the data is requested for. If empty, corresponds to whole company. | [optional] 

## Examples

- Prepare the resource
```powershell
$PeopleSuggestRequest = Initialize-PSOpenAPIToolsPeopleSuggestRequest  -Categories null `
 -Departments null
```

- Convert the resource to JSON
```powershell
$PeopleSuggestRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

