# CalendarEvent
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**EventType** | **String** | The nature of the event, for example &quot;&quot;out of office&quot;&quot;. | [optional] 
**Id** | **String** | The calendar event id | 
**Url** | **String** | A permalink for this calendar event | 
**Attendees** | [**CalendarAttendees**](CalendarAttendees.md) |  | [optional] 
**Location** | **String** | The location that this event is taking place at. | [optional] 
**ConferenceData** | [**ConferenceData**](ConferenceData.md) |  | [optional] 
**Description** | **String** | The HTML description of the event. | [optional] 
**Datasource** | **String** | The app or other repository type from which the event was extracted | [optional] 
**Classifications** | [**EventClassification[]**](EventClassification.md) |  | [optional] 
**GeneratedAttachments** | [**GeneratedAttachment[]**](GeneratedAttachment.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$CalendarEvent = Initialize-PSOpenAPIToolsCalendarEvent  -Time null `
 -EventType null `
 -Id null `
 -Url null `
 -Attendees null `
 -Location null `
 -ConferenceData null `
 -Description null `
 -Datasource null `
 -Classifications null `
 -GeneratedAttachments null
```

- Convert the resource to JSON
```powershell
$CalendarEvent | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

