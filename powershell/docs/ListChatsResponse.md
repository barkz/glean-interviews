# ListChatsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChatResults** | [**ChatMetadataResult[]**](ChatMetadataResult.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ListChatsResponse = Initialize-PSOpenAPIToolsListChatsResponse  -ChatResults null
```

- Convert the resource to JSON
```powershell
$ListChatsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

