# GeneratedAttachment
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StrategyName** | [**EventStrategyName**](EventStrategyName.md) |  | [optional] 
**Documents** | [**Document[]**](Document.md) |  | [optional] 
**Person** | [**Person**](Person.md) |  | [optional] 
**Customer** | [**Customer**](Customer.md) |  | [optional] 
**ExternalLinks** | [**StructuredLink[]**](StructuredLink.md) | A list of links to external sources outside of Glean. | [optional] 
**Content** | [**GeneratedAttachmentContent[]**](GeneratedAttachmentContent.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GeneratedAttachment = Initialize-PSOpenAPIToolsGeneratedAttachment  -StrategyName null `
 -Documents null `
 -Person null `
 -Customer null `
 -ExternalLinks null `
 -Content null
```

- Convert the resource to JSON
```powershell
$GeneratedAttachment | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

