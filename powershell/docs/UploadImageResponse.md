# UploadImageResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **String** | URL of the uploaded image. | 
**Metadata** | [**ImageMetadata**](ImageMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$UploadImageResponse = Initialize-PSOpenAPIToolsUploadImageResponse  -Url null `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$UploadImageResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

