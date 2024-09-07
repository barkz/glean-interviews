# ChatMetadataResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Chat** | [**ChatMetadata**](ChatMetadata.md) |  | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular Chat. To be used for &#x60;/feedback&#x60; reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatMetadataResult = Initialize-PSOpenAPIToolsChatMetadataResult  -Chat null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$ChatMetadataResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

