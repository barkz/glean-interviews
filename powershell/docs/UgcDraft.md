# UgcDraft
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Announcement** | [**AnnouncementMutableProperties**](AnnouncementMutableProperties.md) |  | [optional] 
**Answer** | [**AnswerMutableProperties**](AnswerMutableProperties.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$UgcDraft = Initialize-PSOpenAPIToolsUgcDraft  -Announcement null `
 -Answer null
```

- Convert the resource to JSON
```powershell
$UgcDraft | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

