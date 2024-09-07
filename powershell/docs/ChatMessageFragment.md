# ChatMessageFragment
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StructuredResults** | [**StructuredResult[]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**Text** | **String** |  | [optional] 
**QuerySuggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**WriteAction** | [**WriteAction**](WriteAction.md) |  | [optional] 
**File** | [**ChatFile**](ChatFile.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatMessageFragment = Initialize-PSOpenAPIToolsChatMessageFragment  -StructuredResults null `
 -TrackingToken null `
 -Text null `
 -QuerySuggestion null `
 -WriteAction null `
 -File null
```

- Convert the resource to JSON
```powershell
$ChatMessageFragment | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

