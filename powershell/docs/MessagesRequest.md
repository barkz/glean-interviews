# MessagesRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IdType** | **String** | Type of the id in the incoming request. | 
**Id** | **String** | ID corresponding to the requested idType. Note that channel and threads are represented by the underlying datasource&#39;s ID and conversations are represented by their document&#39;s ID. | 
**WorkspaceId** | **String** | Id for the for the workspace in case of multiple workspaces. | [optional] 
**Direction** | **String** | The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. | [optional] 
**TimestampMillis** | **Int64** | Timestamp in millis of the reference message. | 
**IncludeRootMessage** | **Boolean** | Whether to include root message in response. | [optional] 
**Datasource** | **String** | The type of the data source. Missing field defaults to SLACK. | [optional] 
**DatasourceInstanceDisplayName** | **String** | The datasource instance display name from which the document was extracted. This is used for appinstance facet filter for datasources that support multiple instances. | [optional] 

## Examples

- Prepare the resource
```powershell
$MessagesRequest = Initialize-PSOpenAPIToolsMessagesRequest  -IdType null `
 -Id null `
 -WorkspaceId null `
 -Direction null `
 -TimestampMillis null `
 -IncludeRootMessage null `
 -Datasource null `
 -DatasourceInstanceDisplayName null
```

- Convert the resource to JSON
```powershell
$MessagesRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

