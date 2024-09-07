# DisplayableList
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Source** | **String** | The type of data that backs this displayable list | [optional] 
**Id** | **Int32** | Unique identifier of this list. Unique amongst only DisplayableLists, not unique amongst other types of UGC. | [optional] 
**SourceId** | **String** | Unstructured identifier for the source to render (ID, URL, query). | [optional] 
**Config** | [**DisplayableListConfig**](DisplayableListConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DisplayableList = Initialize-PSOpenAPIToolsDisplayableList  -Source null `
 -Id null `
 -SourceId null `
 -Config null
```

- Convert the resource to JSON
```powershell
$DisplayableList | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

