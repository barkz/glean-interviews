# AskExperimentalMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QueryHasMentions** | **Boolean** | Whether or not the query (i.e. the slack message) has a mention. | [optional] 
**QueryIsLengthAppropriate** | **Boolean** | Whether or not the query (i.e. the slack message) is length appropriate. | [optional] 
**QueryIsAnswerable** | **Boolean** | Whether or not the query (i.e. the slack message) has a question term. | [optional] 

## Examples

- Prepare the resource
```powershell
$AskExperimentalMetadata = Initialize-PSOpenAPIToolsAskExperimentalMetadata  -QueryHasMentions null `
 -QueryIsLengthAppropriate null `
 -QueryIsAnswerable null
```

- Convert the resource to JSON
```powershell
$AskExperimentalMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

