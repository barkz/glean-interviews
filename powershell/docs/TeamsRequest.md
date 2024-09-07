# TeamsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **String[]** | The IDs of the teams to retrieve. | [optional] 
**IncludeFields** | **String[]** | List of teams fields to return that aren&#39;t returned by default | [optional] 

## Examples

- Prepare the resource
```powershell
$TeamsRequest = Initialize-PSOpenAPIToolsTeamsRequest  -Ids null `
 -IncludeFields null
```

- Convert the resource to JSON
```powershell
$TeamsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

