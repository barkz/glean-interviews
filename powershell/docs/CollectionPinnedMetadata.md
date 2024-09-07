# CollectionPinnedMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExistingPins** | [**CollectionPinTarget[]**](CollectionPinTarget.md) | List of targets this Collection is pinned to. | [optional] 
**EligiblePins** | [**CollectionPinMetadata[]**](CollectionPinMetadata.md) | List of targets this Collection can be pinned to, excluding the targets this Collection is already pinned to. We also include Collection ID already is pinned to each eligible target, which will be 0 if the target has no pinned Collection. | [optional] 

## Examples

- Prepare the resource
```powershell
$CollectionPinnedMetadata = Initialize-PSOpenAPIToolsCollectionPinnedMetadata  -ExistingPins null `
 -EligiblePins null
```

- Convert the resource to JSON
```powershell
$CollectionPinnedMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

