# Group
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | [**GroupType**](GroupType.md) |  | 
**Id** | **String** | A unique identifier for the group. May be the same as name. | 
**Name** | **String** | Name of the group. | [optional] 

## Examples

- Prepare the resource
```powershell
$Group = Initialize-PSOpenAPIToolsGroup  -Type null `
 -Id null `
 -Name null
```

- Convert the resource to JSON
```powershell
$Group | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

