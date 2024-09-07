# PinCollectionRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | **String** | Whether to pin or unpin | [default to "PIN"]
**VarData** | [**CollectionPinMetadata**](CollectionPinMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PinCollectionRequest = Initialize-PSOpenAPIToolsPinCollectionRequest  -Action null `
 -VarData null
```

- Convert the resource to JSON
```powershell
$PinCollectionRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

