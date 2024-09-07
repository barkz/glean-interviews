# RemovedCollections
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RemovedCollections** | **Int32[]** | IDs of Collections from which a document is removed. | [optional] 

## Examples

- Prepare the resource
```powershell
$RemovedCollections = Initialize-PSOpenAPIToolsRemovedCollections  -RemovedCollections null
```

- Convert the resource to JSON
```powershell
$RemovedCollections | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

