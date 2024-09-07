# DocumentSection
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **String** | The title of the document section (e.g. the section header). | [optional] 
**Url** | **String** | The permalink of the document section. | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentSection = Initialize-PSOpenAPIToolsDocumentSection  -Title null `
 -Url null
```

- Convert the resource to JSON
```powershell
$DocumentSection | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

