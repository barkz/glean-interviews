# Person
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The display name. | 
**ObfuscatedId** | **String** | An opaque identifier that can be used to request metadata for a Person. | 
**RelatedDocuments** | [**RelatedDocuments[]**](RelatedDocuments.md) | A list of documents related to this person. | [optional] 
**Metadata** | [**PersonMetadata**](PersonMetadata.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$Person = Initialize-PSOpenAPIToolsPerson  -Name null `
 -ObfuscatedId null `
 -RelatedDocuments null `
 -Metadata null
```

- Convert the resource to JSON
```powershell
$Person | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

