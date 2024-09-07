# FeedResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExperimentIds** | **Int64[]** | List of experiment ids for the corresponding request. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular feed response. | [optional] 
**ServerTimestamp** | **Int32** | Server unix timestamp (in seconds since epoch UTC). | 
**Results** | [**FeedResult[]**](FeedResult.md) |  | [optional] 
**FacetResults** | [**System.Collections.Hashtable**](Array.md) | Map from category to the list of facets that can be used to filter the entry&#39;s content. | [optional] 
**MentionsTimeWindowInHours** | **Int32** | The time window (in hours) used for generating user mentions. | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedResponse = Initialize-PSOpenAPIToolsFeedResponse  -ExperimentIds null `
 -TrackingToken null `
 -ServerTimestamp null `
 -Results null `
 -FacetResults null `
 -MentionsTimeWindowInHours null
```

- Convert the resource to JSON
```powershell
$FeedResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

