# CustomEntityMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CustomData** | [**System.Collections.Hashtable**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 

## Examples

- Prepare the resource
```powershell
$CustomEntityMetadata = Initialize-PSOpenAPIToolsCustomEntityMetadata  -CustomData null
```

- Convert the resource to JSON
```powershell
$CustomEntityMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

