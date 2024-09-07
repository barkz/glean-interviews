# SummarizeResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VarError** | [**SummarizeResponseError**](SummarizeResponseError.md) |  | [optional] 
**Summary** | [**Summary**](Summary.md) |  | [optional] 
**TrackingToken** | **String** | An opaque token that represents this summary in this particular query. To be used for /feedback reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$SummarizeResponse = Initialize-PSOpenAPIToolsSummarizeResponse  -VarError null `
 -Summary null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$SummarizeResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

