# EditAnswerRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The opaque ID of the Answer. | 
**DocId** | **String** | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn&#39;t available. If both are available, using the Answer ID is preferred. | [optional] 
**Question** | **String** |  | [optional] 
**QuestionVariations** | **String[]** | Additional ways of phrasing this question. | [optional] 
**BodyText** | **String** | The plain text answer to the question. | [optional] 
**BoardId** | **Int32** | The parent board ID of this Answer, or 0 if it&#39;s a floating Answer. | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search. | [optional] 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the answer added by the owner. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the answer removed by the owner. | [optional] 
**Roles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of roles for this answer explicitly granted by an owner, editor, or admin. | [optional] 
**SourceDocumentSpec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**SourceType** | **String** |  | [optional] 
**AddedCollections** | **Int32[]** | IDs of Collections to which a document is added. | [optional] 
**RemovedCollections** | **Int32[]** | IDs of Collections from which a document is removed. | [optional] 
**CombinedAnswerText** | [**StructuredTextMutableProperties**](StructuredTextMutableProperties.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$EditAnswerRequest = Initialize-PSOpenAPIToolsEditAnswerRequest  -Id 3 `
 -DocId ANSWERS_answer_3 `
 -Question Why is the sky blue? `
 -QuestionVariations null `
 -BodyText From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light. `
 -BoardId null `
 -AudienceFilters null `
 -AddedRoles null `
 -RemovedRoles null `
 -Roles null `
 -SourceDocumentSpec null `
 -SourceType null `
 -AddedCollections null `
 -RemovedCollections null `
 -CombinedAnswerText null
```

- Convert the resource to JSON
```powershell
$EditAnswerRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

