# DeleteChatsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **String[]** | A non-empty list of ids of the Chats to be deleted. | 

## Examples

- Prepare the resource
```powershell
$DeleteChatsRequest = Initialize-PSOpenAPIToolsDeleteChatsRequest  -Ids null
```

- Convert the resource to JSON
```powershell
$DeleteChatsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

