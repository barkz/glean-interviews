# CalendarAttendee
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsOrganizer** | **Boolean** | Whether or not this attendee is an organizer. | [optional] 
**IsInGroup** | **Boolean** | Whether or not this attendee is in a group. Needed temporarily at least to support both flat attendees and tree for compatibility. | [optional] 
**Person** | [**Person**](Person.md) |  | 
**GroupAttendees** | [**CalendarAttendee[]**](CalendarAttendee.md) | If this attendee is a group, represents the list of individual attendees in the group. | [optional] 
**ResponseStatus** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$CalendarAttendee = Initialize-PSOpenAPIToolsCalendarAttendee  -IsOrganizer null `
 -IsInGroup null `
 -Person null `
 -GroupAttendees null `
 -ResponseStatus null
```

- Convert the resource to JSON
```powershell
$CalendarAttendee | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

