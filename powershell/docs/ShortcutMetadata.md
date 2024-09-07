# ShortcutMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedBy** | [**Person**](Person.md) |  | [optional] 
**CreateTime** | **System.DateTime** | The time the shortcut was created in ISO format (ISO 8601). | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**UpdateTime** | **System.DateTime** | The time the shortcut was updated in ISO format (ISO 8601). | [optional] 
**DestinationDocument** | [**Document**](Document.md) |  | [optional] 
**IntermediateUrl** | **String** | The URL from which the user is then redirected to the destination URL. Full replacement for https://go/&lt;inputAlias&gt;. | [optional] 
**ViewPrefix** | **String** | The part of the shortcut preceding the input alias when used for showing shortcuts to users. Should end with &quot;&quot;/&quot;&quot;. e.g. &quot;&quot;go/&quot;&quot; for native shortcuts. | [optional] 
**IsExternal** | **Boolean** | Indicates whether a shortcut is native or external. | [optional] 
**EditUrl** | **String** | The URL using which the user can access the edit page of the shortcut. | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutMetadata = Initialize-PSOpenAPIToolsShortcutMetadata  -CreatedBy null `
 -CreateTime null `
 -UpdatedBy null `
 -UpdateTime null `
 -DestinationDocument null `
 -IntermediateUrl null `
 -ViewPrefix null `
 -IsExternal null `
 -EditUrl null
```

- Convert the resource to JSON
```powershell
$ShortcutMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

