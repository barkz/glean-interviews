# AuthConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsOnPrem** | **Boolean** | Whether or not this tool is hosted on-premise. | [optional] 
**Type** | **String** | The type of authentication being used. Use &#39;OAUTH_*&#39; when Glean calls an external API (e.g., Jira) on behalf of a user to obtain an OAuth token. &#39;OAUTH_ADMIN&#39; utilizes an admin token for external API calls on behalf all users. &#39;OAUTH_USER&#39; uses individual user tokens for external API calls. | [optional] 
**Status** | **String** | Auth status of the tool. | [optional] 
**ClientUrl** | **String** | The URL where users will be directed to start the OAuth flow. | [optional] 
**Scopes** | **String[]** | A list of strings denoting the different scopes or access levels required by the tool. | [optional] 
**AuthorizationUrl** | **String** | The OAuth provider&#39;s endpoint, where access tokens are requested. | [optional] 

## Examples

- Prepare the resource
```powershell
$AuthConfig = Initialize-PSOpenAPIToolsAuthConfig  -IsOnPrem null `
 -Type null `
 -Status null `
 -ClientUrl null `
 -Scopes null `
 -AuthorizationUrl null
```

- Convert the resource to JSON
```powershell
$AuthConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

