# FeedEntry
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EntryId** | **String** | optional ID associated with a single feed entry (displayable_list_id) | [optional] 
**Title** | **String** | Title for the result. Can be document title, event title and so on. | 
**Thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**CreatedBy** | [**Person**](Person.md) |  | [optional] 
**UiConfig** | [**FeedEntryUiConfig**](FeedEntryUiConfig.md) |  | [optional] 
**JustificationType** | **String** | Type of the justification. | [optional] 
**Justification** | **String** | Server side generated justification string if server provides one. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular feed entry in this particular response. To be used for /feedback reporting. | [optional] 
**ViewUrl** | **String** | View URL for the entry if based on links that are not documents in Glean. | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**VarEvent** | [**CalendarEvent**](CalendarEvent.md) |  | [optional] 
**Announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**Collection** | [**Collection**](Collection.md) |  | [optional] 
**CollectionItem** | [**CollectionItem**](CollectionItem.md) |  | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 
**App** | [**AppResult**](AppResult.md) |  | [optional] 
**Activities** | [**UserActivity[]**](UserActivity.md) | List of activity where each activity has user, action, timestamp. | [optional] 
**DocumentVisitorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedEntry = Initialize-PSOpenAPIToolsFeedEntry  -EntryId null `
 -Title null `
 -Thumbnail null `
 -CreatedBy null `
 -UiConfig null `
 -JustificationType null `
 -Justification null `
 -TrackingToken null `
 -ViewUrl null `
 -Document null `
 -VarEvent null `
 -Announcement null `
 -Collection null `
 -CollectionItem null `
 -Person null `
 -App null `
 -Activities null `
 -DocumentVisitorCount null
```

- Convert the resource to JSON
```powershell
$FeedEntry | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

