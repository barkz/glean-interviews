# VerifyRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentId** | **String** | The document which is verified. | 
**Action** | **String** | The verification action requested. | [optional] 

## Examples

- Prepare the resource
```powershell
$VerifyRequest = Initialize-PSOpenAPIToolsVerifyRequest  -DocumentId null `
 -Action null
```

- Convert the resource to JSON
```powershell
$VerifyRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

