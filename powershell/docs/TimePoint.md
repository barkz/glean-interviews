# TimePoint
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EpochSeconds** | **Int32** | Epoch seconds. Has precedence over daysFromNow. | [optional] 
**DaysFromNow** | **Int32** | The number of days from now. Specification relative to current time. Can be negative. | [optional] 

## Examples

- Prepare the resource
```powershell
$TimePoint = Initialize-PSOpenAPIToolsTimePoint  -EpochSeconds null `
 -DaysFromNow null
```

- Convert the resource to JSON
```powershell
$TimePoint | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

