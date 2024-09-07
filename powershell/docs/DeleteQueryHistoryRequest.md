# DeleteQueryHistoryRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | **String[]** | Queries to delete. | [optional] 

## Examples

- Prepare the resource
```powershell
$DeleteQueryHistoryRequest = Initialize-PSOpenAPIToolsDeleteQueryHistoryRequest  -Queries null
```

- Convert the resource to JSON
```powershell
$DeleteQueryHistoryRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

