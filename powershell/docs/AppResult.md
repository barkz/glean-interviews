# AppResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** | The app or other repository type this represents | 
**DocType** | **String** | The datasource-specific type of the document (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**MimeType** | **String** | Mimetype is used to differentiate between sub applications from a datasource (e.g. Sheets, Docs from Gdrive) | [optional] 
**IconUrl** | **String** | If there is available icon URL. | [optional] 

## Examples

- Prepare the resource
```powershell
$AppResult = Initialize-PSOpenAPIToolsAppResult  -Datasource null `
 -DocType null `
 -MimeType null `
 -IconUrl null
```

- Convert the resource to JSON
```powershell
$AppResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

