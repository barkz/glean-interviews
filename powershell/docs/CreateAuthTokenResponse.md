# CreateAuthTokenResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Token** | **String** | An authentication token that can be passed to any endpoint via Bearer Authentication | 
**ExpirationTime** | **Int64** | Unix timestamp for when this token expires (in seconds since epoch UTC). | 

## Examples

- Prepare the resource
```powershell
$CreateAuthTokenResponse = Initialize-PSOpenAPIToolsCreateAuthTokenResponse  -Token null `
 -ExpirationTime null
```

- Convert the resource to JSON
```powershell
$CreateAuthTokenResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

