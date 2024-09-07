# ActivityEvent
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | Universally unique identifier of the event. To allow for reliable retransmission, only the earliest received event of a given UUID is considered valid by the server and subsequent are ignored. | [optional] 
**Action** | **String** | The type of activity this represents. | 
**Params** | [**ActivityEventParams**](ActivityEventParams.md) |  | [optional] 
**Timestamp** | **System.DateTime** | The ISO 8601 timestamp when the activity began. | 
**Url** | **String** | The URL of the activity. | 

## Examples

- Prepare the resource
```powershell
$ActivityEvent = Initialize-PSOpenAPIToolsActivityEvent  -Id null `
 -Action null `
 -Params null `
 -Timestamp null `
 -Url null
```

- Convert the resource to JSON
```powershell
$ActivityEvent | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

