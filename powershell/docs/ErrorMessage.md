# ErrorMessage
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Source** | **String** | The datasource this message relates to. | [optional] 
**ErrorMessage** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ErrorMessage = Initialize-PSOpenAPIToolsErrorMessage  -Source null `
 -ErrorMessage null
```

- Convert the resource to JSON
```powershell
$ErrorMessage | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

