# AskResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsQuestion** | **Boolean** | Whether or not the query was a question. | 
**Question** | **String** | The part of the query which was used as a question for search | [optional] 
**SearchResponse** | [**SearchResponse**](SearchResponse.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$AskResponse = Initialize-PSOpenAPIToolsAskResponse  -IsQuestion null `
 -Question null `
 -SearchResponse null
```

- Convert the resource to JSON
```powershell
$AskResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

