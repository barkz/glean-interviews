# ChatMessageCitation
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackingToken** | **String** | An opaque token that represents this particular result in this particular ChatMessage. To be used for /feedback reporting. | [optional] 
**SourceDocument** | [**Document**](Document.md) |  | [optional] 
**SourceFile** | [**ChatFile**](ChatFile.md) |  | [optional] 
**SourcePerson** | [**Person**](Person.md) |  | [optional] 
**ReferenceRanges** | [**ReferenceRange[]**](ReferenceRange.md) | Each reference range and its corresponding snippets | [optional] 

## Examples

- Prepare the resource
```powershell
$ChatMessageCitation = Initialize-PSOpenAPIToolsChatMessageCitation  -TrackingToken null `
 -SourceDocument null `
 -SourceFile null `
 -SourcePerson null `
 -ReferenceRanges null
```

- Convert the resource to JSON
```powershell
$ChatMessageCitation | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

