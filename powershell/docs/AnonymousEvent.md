# AnonymousEvent
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Time** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**EventType** | **String** | The nature of the event, for example &quot;&quot;out of office&quot;&quot;. | [optional] 

## Examples

- Prepare the resource
```powershell
$AnonymousEvent = Initialize-PSOpenAPIToolsAnonymousEvent  -Time null `
 -EventType null
```

- Convert the resource to JSON
```powershell
$AnonymousEvent | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

