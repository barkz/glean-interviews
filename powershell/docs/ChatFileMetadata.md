# ChatFileMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | [**ChatFileStatus**](ChatFileStatus.md) |  | [optional] 
**UploadTime** | **Int64** | Upload time, in epoch seconds. | [optional] 
**ProcessedSize** | **Int64** | Size of the processed file in bytes. | [optional] 
**FailureReason** | [**ChatFileFailureReason**](ChatFileFailureReason.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatFileMetadata = Initialize-PSOpenAPIToolsChatFileMetadata  -Status null `
 -UploadTime null `
 -ProcessedSize null `
 -FailureReason null
```

- Convert the resource to JSON
```powershell
$ChatFileMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

