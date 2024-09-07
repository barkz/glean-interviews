# PeopleSuggestResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Suggestions** | [**PersonSuggestionList[]**](PersonSuggestionList.md) | Information about people suggestions for asked categories. | [optional] 

## Examples

- Prepare the resource
```powershell
$PeopleSuggestResponse = Initialize-PSOpenAPIToolsPeopleSuggestResponse  -Suggestions null
```

- Convert the resource to JSON
```powershell
$PeopleSuggestResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

