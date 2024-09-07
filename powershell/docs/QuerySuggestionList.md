# QuerySuggestionList
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Suggestions** | [**QuerySuggestion[]**](QuerySuggestion.md) |  | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$QuerySuggestionList = Initialize-PSOpenAPIToolsQuerySuggestionList  -Suggestions null `
 -Person null
```

- Convert the resource to JSON
```powershell
$QuerySuggestionList | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

