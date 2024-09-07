# FeedRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Categories** | **String[]** | Categories of content requested. An allowlist gives flexibility to request content separately or together. | [optional] 
**RequestOptions** | [**FeedRequestOptions**](FeedRequestOptions.md) |  | [optional] 
**TimeoutMillis** | **Int32** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedRequest = Initialize-PSOpenAPIToolsFeedRequest  -Categories null `
 -RequestOptions null `
 -TimeoutMillis 5000 `
 -SessionInfo null
```

- Convert the resource to JSON
```powershell
$FeedRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

