# AddCredentialRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** | the datasource the credential applies to | [optional] 
**DatasourceInstance** | **String** | the datasource instance the credential applies to | [optional] 
**User** | **String** | the user info (email or username for example) for the credential | [optional] 
**Token** | **String** | the token part of the credential (password, apiToken etc) | [optional] 
**Metadata** | **String** | any metadata associated with the user credential | [optional] 

## Examples

- Prepare the resource
```powershell
$AddCredentialRequest = Initialize-PSOpenAPIToolsAddCredentialRequest  -Datasource null `
 -DatasourceInstance null `
 -User null `
 -Token null `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$AddCredentialRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

