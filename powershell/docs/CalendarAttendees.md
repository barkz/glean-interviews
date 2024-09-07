# CalendarAttendees
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**People** | [**CalendarAttendee[]**](CalendarAttendee.md) | Full details of some of the attendees of this event | [optional] 
**IsLimit** | **Boolean** | Whether the total count of the people returned is at the retrieval limit. | [optional] 
**Total** | **Int32** | Total number of attendees in this event. | [optional] 
**NumAccepted** | **Int32** | Total number of attendees who have accepted this event. | [optional] 
**NumDeclined** | **Int32** | Total number of attendees who have declined this event. | [optional] 
**NumNoResponse** | **Int32** | Total number of attendees who have not responded to this event. | [optional] 
**NumTentative** | **Int32** | Total number of attendees who have responded tentatively (i.e. responded maybe) to this event. | [optional] 

## Examples

- Prepare the resource
```powershell
$CalendarAttendees = Initialize-PSOpenAPIToolsCalendarAttendees  -People null `
 -IsLimit null `
 -Total null `
 -NumAccepted null `
 -NumDeclined null `
 -NumNoResponse null `
 -NumTentative null
```

- Convert the resource to JSON
```powershell
$CalendarAttendees | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

