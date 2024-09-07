# RemoveCredentialRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** | the datasource the credential applies to | [optional] 
**DatasourceInstance** | **String** | the datasource instance the credential applies to | [optional] 
**User** | **String** | the user info (email or username for example) for the credential | [optional] 

## Examples

- Prepare the resource
```powershell
$RemoveCredentialRequest = Initialize-PSOpenAPIToolsRemoveCredentialRequest  -Datasource null `
 -DatasourceInstance null `
 -User null
```

- Convert the resource to JSON
```powershell
$RemoveCredentialRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

