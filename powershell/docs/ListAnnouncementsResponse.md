# ListAnnouncementsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Announcements** | [**Announcement[]**](Announcement.md) | List of announcements. | [optional] 

## Examples

- Prepare the resource
```powershell
$ListAnnouncementsResponse = Initialize-PSOpenAPIToolsListAnnouncementsResponse  -Announcements null
```

- Convert the resource to JSON
```powershell
$ListAnnouncementsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

