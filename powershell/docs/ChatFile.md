# ChatFile
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | Unique identifier of the file. | [optional] 
**Name** | **String** | Name of the uploaded file. | [optional] 
**Metadata** | [**ChatFileMetadata**](ChatFileMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatFile = Initialize-PSOpenAPIToolsChatFile  -Id FILE_1234 `
 -Name sample.pdf `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$ChatFile | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

