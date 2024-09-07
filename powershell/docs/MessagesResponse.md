# MessagesResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HasMore** | **Boolean** | Whether there are more results for client to continue requesting. | 
**SearchResponse** | [**SearchResponse**](SearchResponse.md) |  | [optional] 
**RootMessage** | [**SearchResult**](SearchResult.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$MessagesResponse = Initialize-PSOpenAPIToolsMessagesResponse  -HasMore null `
 -SearchResponse null `
 -RootMessage null
```

- Convert the resource to JSON
```powershell
$MessagesResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

