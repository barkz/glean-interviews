# Badge
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **String** | An auto generated unique identifier. | [optional] 
**DisplayName** | **String** | The badge name displayed to users | [optional] 
**IconConfig** | [**IconConfig**](IconConfig.md) |  | [optional] 
**Pinned** | **Boolean** | The badge should be shown on the PersonAttribution | [optional] 

## Examples

- Prepare the resource
```powershell
$Badge = Initialize-PSOpenAPIToolsBadge  -Key null `
 -DisplayName null `
 -IconConfig null `
 -Pinned null
```

- Convert the resource to JSON
```powershell
$Badge | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

