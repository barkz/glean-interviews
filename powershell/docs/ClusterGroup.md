# ClusterGroup
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClusteredResults** | [**SearchResult[]**](SearchResult.md) | A list of results that should be displayed as associated with this result. | [optional] 
**ClusterType** | [**ClusterTypeEnum**](ClusterTypeEnum.md) |  | [optional] 
**VisibleCountHint** | **Int32** | The default number of results to display before truncating and showing a &quot;&quot;see more&quot;&quot; link | 

## Examples

- Prepare the resource
```powershell
$ClusterGroup = Initialize-PSOpenAPIToolsClusterGroup  -ClusteredResults null `
 -ClusterType null `
 -VisibleCountHint null
```

- Convert the resource to JSON
```powershell
$ClusterGroup | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

