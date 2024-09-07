# PreviewUgcResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**Answer** | [**Answer**](Answer.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PreviewUgcResponse = Initialize-PSOpenAPIToolsPreviewUgcResponse  -Announcement null `
 -Answer null
```

- Convert the resource to JSON
```powershell
$PreviewUgcResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

