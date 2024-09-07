# ResultTab
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | The unique ID of the tab. Can be passed in a search request to get results for that tab. | [optional] 
**Count** | **Int32** | The number of results in this tab for the current query. | [optional] 
**Datasource** | **String** | The datasource associated with the tab, if any. | [optional] 
**DatasourceInstance** | **String** | The datasource instance associated with the tab, if any. | [optional] 

## Examples

- Prepare the resource
```powershell
$ResultTab = Initialize-PSOpenAPIToolsResultTab  -Id null `
 -Count null `
 -Datasource null `
 -DatasourceInstance null
```

- Convert the resource to JSON
```powershell
$ResultTab | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

