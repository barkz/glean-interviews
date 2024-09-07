# Period
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MinDaysFromNow** | **Int32** | DEPRECATED - The number of days from now in the past to define upper boundary of time period. | [optional] 
**MaxDaysFromNow** | **Int32** | DEPRECATED - The number of days from now in the past to define lower boundary of time period. | [optional] 
**Start** | [**TimePoint**](TimePoint.md) |  | [optional] 
**VarEnd** | [**TimePoint**](TimePoint.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$Period = Initialize-PSOpenAPIToolsPeriod  -MinDaysFromNow null `
 -MaxDaysFromNow null `
 -Start null `
 -VarEnd null
```

- Convert the resource to JSON
```powershell
$Period | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

