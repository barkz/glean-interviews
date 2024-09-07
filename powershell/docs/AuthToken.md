# AuthToken
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccessToken** | **String** |  | 
**Datasource** | **String** |  | 
**Scope** | **String** |  | [optional] 
**TokenType** | **String** |  | [optional] 
**AuthUser** | **String** | Used by Google to indicate the index of the logged in user. Useful for generating hyperlinks that support multilogin. | [optional] 
**Expiration** | **Int64** | Unix timestamp when this token expires (in seconds since epoch UTC). | [optional] 

## Examples

- Prepare the resource
```powershell
$AuthToken = Initialize-PSOpenAPIToolsAuthToken  -AccessToken null `
 -Datasource null `
 -Scope null `
 -TokenType null `
 -AuthUser null `
 -Expiration null
```

- Convert the resource to JSON
```powershell
$AuthToken | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

