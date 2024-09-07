# Verification
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**State** | **String** | The verification state for the document. | 
**Metadata** | [**VerificationMetadata**](VerificationMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$Verification = Initialize-PSOpenAPIToolsVerification  -State null `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$Verification | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

