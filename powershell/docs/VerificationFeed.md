# VerificationFeed
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Documents** | [**Verification[]**](Verification.md) | List of document infos that include verification related information for them. | [optional] 

## Examples

- Prepare the resource
```powershell
$VerificationFeed = Initialize-PSOpenAPIToolsVerificationFeed  -Documents null
```

- Convert the resource to JSON
```powershell
$VerificationFeed | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

