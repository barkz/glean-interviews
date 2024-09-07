# CountInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Count** | **Int32** | The counter value | 
**Period** | [**Period**](Period.md) |  | [optional] 
**Org** | **String** | The unit of organization over which we did the count aggregation, e.g. org (department) or company | [optional] 

## Examples

- Prepare the resource
```powershell
$CountInfo = Initialize-PSOpenAPIToolsCountInfo  -Count null `
 -Period null `
 -Org null
```

- Convert the resource to JSON
```powershell
$CountInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

