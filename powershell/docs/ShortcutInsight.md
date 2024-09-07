# ShortcutInsight
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shortcut** | [**Shortcut**](Shortcut.md) |  | 
**VisitCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**VisitorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutInsight = Initialize-PSOpenAPIToolsShortcutInsight  -Shortcut null `
 -VisitCount null `
 -VisitorCount null
```

- Convert the resource to JSON
```powershell
$ShortcutInsight | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

