# GetDraftAnnouncementResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**VarError** | [**AnnouncementError**](AnnouncementError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDraftAnnouncementResponse = Initialize-PSOpenAPIToolsGetDraftAnnouncementResponse  -Announcement null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$GetDraftAnnouncementResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

