# CollectionPinTarget
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | [**CollectionPinnableCategories**](CollectionPinnableCategories.md) |  | 
**Value** | **String** | Optional. If category supports values, then the additional value for the category e.g. department name for DEPARTMENT_RESOURCE, team name/id for TEAM_RESOURCE and so on. | [optional] 
**Target** | [**CollectionPinnableTargets**](CollectionPinnableTargets.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$CollectionPinTarget = Initialize-PSOpenAPIToolsCollectionPinTarget  -Category null `
 -Value null `
 -Target null
```

- Convert the resource to JSON
```powershell
$CollectionPinTarget | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

