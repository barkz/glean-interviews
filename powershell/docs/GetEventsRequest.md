# GetEventsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **String[]** | The ids of the calendar events to be retrieved. | 
**AuthTokens** | [**AuthToken[]**](AuthToken.md) | Auth tokens if client-side authentication. | [optional] 
**Datasource** | **String** | The app or other repository type from which the event was extracted | [optional] 
**Annotate** | **Boolean** | Whether relevant content and documents, via GeneratedAttachments, should be attached to the events. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetEventsRequest = Initialize-PSOpenAPIToolsGetEventsRequest  -Ids null `
 -AuthTokens null `
 -Datasource null `
 -Annotate null
```

- Convert the resource to JSON
```powershell
$GetEventsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

