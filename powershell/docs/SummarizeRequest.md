# SummarizeRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Timestamp** | **System.DateTime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**Query** | **String** | Optional query that the summary should be about | [optional] 
**PreferredSummaryLength** | **Int32** | Optional length of summary output. If not given, defaults to 500 chars. | [optional] 
**DocumentSpecs** | [**DocumentSpec[]**](DocumentSpec.md) | Specifications of documents to summarize | 
**TrackingToken** | **String** | An opaque token that represents this particular result. To be used for /feedback reporting. | [optional] 

## Examples

- Prepare the resource
```powershell
$SummarizeRequest = Initialize-PSOpenAPIToolsSummarizeRequest  -Timestamp null `
 -Query null `
 -PreferredSummaryLength null `
 -DocumentSpecs null `
 -TrackingToken null
```

- Convert the resource to JSON
```powershell
$SummarizeRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

