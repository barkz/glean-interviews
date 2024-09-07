# SearchRequestInputDetails
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HasCopyPaste** | **Boolean** | Whether the associated query was at least partially copy-pasted.  If subsequent requests are issued after a copy-pasted query is constructed (e.g. with facet modifications), this bit should continue to be set for those requests. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchRequestInputDetails = Initialize-PSOpenAPIToolsSearchRequestInputDetails  -HasCopyPaste null
```

- Convert the resource to JSON
```powershell
$SearchRequestInputDetails | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

