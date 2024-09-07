# SessionInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SessionTrackingToken** | **String** | A unique token for this session. A new session (and token) is created when the user issues a request from a new tab or when our server hasn&#39;t seen activity for more than 10 minutes from a tab. | [optional] 
**TabId** | **String** | A unique id for all requests a user makes from a given tab, no matter how far apart. A new tab id is only generated when a user issues a request from a new tab. | [optional] 
**LastSeen** | **System.DateTime** | The last time the server saw this token. | [optional] 
**LastQuery** | **String** | The last query seen by the server. | [optional] 

## Examples

- Prepare the resource
```powershell
$SessionInfo = Initialize-PSOpenAPIToolsSessionInfo  -SessionTrackingToken null `
 -TabId null `
 -LastSeen null `
 -LastQuery null
```

- Convert the resource to JSON
```powershell
$SessionInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

