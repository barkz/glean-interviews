# Document
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | The Glean Document ID. | [optional] 
**Datasource** | **String** | The app or other repository type from which the document was extracted | [optional] 
**ConnectorType** | [**ConnectorType**](ConnectorType.md) |  | [optional] 
**DocType** | **String** | The datasource-specific type of the document (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**Content** | [**DocumentContent**](DocumentContent.md) |  | [optional] 
**ContainerDocument** | [**Document**](Document.md) |  | [optional] 
**ParentDocument** | [**Document**](Document.md) |  | [optional] 
**Title** | **String** | The title of the document. | [optional] 
**Url** | **String** | A permalink for the document. | [optional] 
**Metadata** | [**DocumentMetadata**](DocumentMetadata.md) |  | [optional] 
**Sections** | [**DocumentSection[]**](DocumentSection.md) | A list of content sub-sections in the document, e.g. text blocks with different headings in a Drive doc or Confluence page. | [optional] 

## Examples

- Prepare the resource
```powershell
$Document = Initialize-PSOpenAPIToolsDocument  -Id null `
 -Datasource null `
 -ConnectorType null `
 -DocType null `
 -Content null `
 -ContainerDocument null `
 -ParentDocument null `
 -Title null `
 -Url null `
 -Metadata null `
 -Sections null
```

- Convert the resource to JSON
```powershell
$Document | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

