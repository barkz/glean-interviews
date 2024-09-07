# CustomerMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasourceId** | **String** | The user visible id of the salesforce customer account. | [optional] 
**CustomData** | [**System.Collections.Hashtable**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomerMetadata = Initialize-PSOpenAPIToolsCustomerMetadata  -DatasourceId null `
 -CustomData null
```

- Convert the resource to JSON
```powershell
$CustomerMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

