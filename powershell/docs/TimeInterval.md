# TimeInterval
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Start** | **String** | The RFC3339 timestamp formatted start time of this event. | 
**VarEnd** | **String** | The RFC3339 timestamp formatted end time of this event. | 

## Examples

- Prepare the resource
```powershell
$TimeInterval = Initialize-PSOpenAPIToolsTimeInterval  -Start null `
 -VarEnd null
```

- Convert the resource to JSON
```powershell
$TimeInterval | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

