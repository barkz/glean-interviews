# LabeledCountInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Label** | **String** | Label for the included count information. | 
**CountInfo** | [**CountInfo[]**](CountInfo.md) | List of data points for counts for a given date period. | [optional] 

## Examples

- Prepare the resource
```powershell
$LabeledCountInfo = Initialize-PSOpenAPIToolsLabeledCountInfo  -Label null `
 -CountInfo null
```

- Convert the resource to JSON
```powershell
$LabeledCountInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

