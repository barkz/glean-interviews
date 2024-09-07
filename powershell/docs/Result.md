# Result
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StructuredResults** | [**StructuredResult[]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$Result = Initialize-PSOpenAPIToolsResult  -StructuredResults null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$Result | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

