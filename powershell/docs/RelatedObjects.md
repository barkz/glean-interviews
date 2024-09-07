# RelatedObjects
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RelatedObjects** | [**System.Collections.Hashtable**](RelatedObjectEdge.md) | A list of objects related to a source object. | [optional] 

## Examples

- Prepare the resource
```powershell
$RelatedObjects = Initialize-PSOpenAPIToolsRelatedObjects  -RelatedObjects null
```

- Convert the resource to JSON
```powershell
$RelatedObjects | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

