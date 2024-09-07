# GetAnnouncementResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular announcement. To be used for /feedback reporting. | [optional] 
**VarError** | [**AnnouncementError**](AnnouncementError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetAnnouncementResponse = Initialize-PSOpenAPIToolsGetAnnouncementResponse  -Announcement null `
 -TrackingToken null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$GetAnnouncementResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

