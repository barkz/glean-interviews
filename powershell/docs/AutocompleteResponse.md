# AutocompleteResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExperimentIds** | **Int64[]** | List of experiment ids for the corresponding request. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular set of autocomplete results. To be used for /feedback reporting. | [optional] 
**SessionInfo** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**Results** | [**AutocompleteResult[]**](AutocompleteResult.md) |  | [optional] 
**Groups** | [**AutocompleteResultGroup[]**](AutocompleteResultGroup.md) | Subsections of the results list from which distinct sections should be created. | [optional] 
**ErrorInfo** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**BackendTimeMillis** | **Int64** | Time in milliseconds the backend took to respond to the request. | [optional] 

## Examples

- Prepare the resource
```powershell
$AutocompleteResponse = Initialize-PSOpenAPIToolsAutocompleteResponse  -ExperimentIds null `
 -TrackingToken null `
 -SessionInfo null `
 -Results null `
 -Groups null `
 -ErrorInfo null `
 -BackendTimeMillis 1100
```

- Convert the resource to JSON
```powershell
$AutocompleteResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

