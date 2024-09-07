# RecommendationsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackingToken** | **String** | A token that should be passed for additional requests related to this request (such as more results requests). | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**Results** | [**SearchResult[]**](SearchResult.md) |  | [optional] 
**StructuredResults** | [**StructuredResult[]**](StructuredResult.md) |  | [optional] 
**GeneratedQnaResult** | [**GeneratedQna**](GeneratedQna.md) |  | [optional] 
**ErrorInfo** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**RequestID** | **String** | A platform-generated request ID to correlate backend logs. | [optional] 
**BackendTimeMillis** | **Int64** | Time in milliseconds the backend took to respond to the request. | [optional] 

## Examples

- Prepare the resource
```powershell
$RecommendationsResponse = Initialize-PSOpenAPIToolsRecommendationsResponse  -TrackingToken null `
 -SessionInfo null `
 -Results null `
 -StructuredResults null `
 -GeneratedQnaResult null `
 -ErrorInfo null `
 -RequestID null `
 -BackendTimeMillis 1100
```

- Convert the resource to JSON
```powershell
$RecommendationsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

