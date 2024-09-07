# ViewerInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **String** | DEPRECATED - use permissions instead. Viewer&#39;s role on the specific document. | [optional] 
**LastViewedTime** | **System.DateTime** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ViewerInfo = Initialize-PSOpenAPIToolsViewerInfo  -Role null `
 -LastViewedTime null
```

- Convert the resource to JSON
```powershell
$ViewerInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

