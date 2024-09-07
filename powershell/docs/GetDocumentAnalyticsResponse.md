# GetDocumentAnalyticsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**DocumentAnalytics[]**](DocumentAnalytics.md) | Analytics for requested documents. There will be one-to-one mapping for documents included in the request. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDocumentAnalyticsResponse = Initialize-PSOpenAPIToolsGetDocumentAnalyticsResponse  -Results null
```

- Convert the resource to JSON
```powershell
$GetDocumentAnalyticsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

