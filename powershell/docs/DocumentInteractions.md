# DocumentInteractions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NumComments** | **Int32** | The count of comments (thread replies in the case of slack). | [optional] 
**NumReactions** | **Int32** | The count of reactions on the document. | [optional] 
**Reactions** | **String[]** | To be deprecated in favor of reacts. A (potentially non-exhaustive) list of reactions for the document. | [optional] 
**Reacts** | [**Reaction[]**](Reaction.md) |  | [optional] 
**Shares** | [**Share[]**](Share.md) | Describes instances of someone posting a link to this document in one of our indexed datasources. | [optional] 
**VisitorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentInteractions = Initialize-PSOpenAPIToolsDocumentInteractions  -NumComments null `
 -NumReactions null `
 -Reactions null `
 -Reacts null `
 -Shares null `
 -VisitorCount null
```

- Convert the resource to JSON
```powershell
$DocumentInteractions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

