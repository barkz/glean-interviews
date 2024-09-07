# TeamsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**Team[]**](Team.md) | A Team and a deep copy of all its members for each ID in the request | [optional] 
**Errors** | **String[]** | A list of IDs that could not be found. | [optional] 

## Examples

- Prepare the resource
```powershell
$TeamsResponse = Initialize-PSOpenAPIToolsTeamsResponse  -Results null `
 -Errors null
```

- Convert the resource to JSON
```powershell
$TeamsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

