# GetEventsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Events** | [**FeedResult[]**](FeedResult.md) | The requested events. Uses a FeedResult for now as a Calendar Event doesn&#39;t have all event info such as attachments. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetEventsResponse = Initialize-PSOpenAPIToolsGetEventsResponse  -Events null
```

- Convert the resource to JSON
```powershell
$GetEventsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

