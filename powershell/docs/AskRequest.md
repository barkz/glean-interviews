# AskRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DetectOnly** | **Boolean** | Whether to apply only question detection and not answering. | [optional] 
**AskExperimentalMetadata** | [**AskExperimentalMetadata**](AskExperimentalMetadata.md) |  | [optional] 
**SearchRequest** | [**SearchRequest**](SearchRequest.md) |  | 
**ExcludedDocumentSpecs** | [**DocumentSpec[]**](DocumentSpec.md) | A list of Glean Document IDs to be excluded when retrieving documents. Note that, currently, it only supports exclusion of one Glean Documnet ID based spec. If multiple specifications are provided only the first Glean Document ID based spec is excluded and the remaining specs are ignored. | [optional] 
**Operators** | **String** | Search operators to append to the query | [optional] 
**Backend** | **String** | Which backend to use to fulfill the requests. | [optional] 
**ChatApplicationId** | **String** | The ID of the application this request originates from, used to determine the configuration of underlying chat processes when invoking the CHAT backend. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used. | [optional] 

## Examples

- Prepare the resource
```powershell
$AskRequest = Initialize-PSOpenAPIToolsAskRequest  -DetectOnly null `
 -AskExperimentalMetadata null `
 -SearchRequest null `
 -ExcludedDocumentSpecs null `
 -Operators null `
 -Backend null `
 -ChatApplicationId null
```

- Convert the resource to JSON
```powershell
$AskRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

