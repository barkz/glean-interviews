# UserViewInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocId** | **String** | Unique Glean Document ID of the associated document. | [optional] 
**DocTitle** | **String** | Title of associated document. | [optional] 
**DocUrl** | **String** | URL of associated document. | [optional] 

## Examples

- Prepare the resource
```powershell
$UserViewInfo = Initialize-PSOpenAPIToolsUserViewInfo  -DocId null `
 -DocTitle null `
 -DocUrl null
```

- Convert the resource to JSON
```powershell
$UserViewInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

