# AnnouncementAllOfViewerInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsDismissed** | **Boolean** | Whether the viewer has dismissed the announcement. | [optional] 
**IsRead** | **Boolean** | Whether the viewer has read the announcement. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnnouncementAllOfViewerInfo = Initialize-PSOpenAPIToolsAnnouncementAllOfViewerInfo  -IsDismissed null `
 -IsRead null
```

- Convert the resource to JSON
```powershell
$AnnouncementAllOfViewerInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

