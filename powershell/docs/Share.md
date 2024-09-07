# Share
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NumDaysAgo** | **Int32** | The number of days that has passed since the share happened | 
**Sharer** | [**Person**](Person.md) |  | [optional] 
**SharingDocument** | [**Document**](Document.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$Share = Initialize-PSOpenAPIToolsShare  -NumDaysAgo null `
 -Sharer null `
 -SharingDocument null
```

- Convert the resource to JSON
```powershell
$Share | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

