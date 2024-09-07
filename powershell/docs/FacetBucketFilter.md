# FacetBucketFilter
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Facet** | **String** | The facet whose buckets should be filtered. | [optional] 
**Prefix** | **String** | The per-term prefix that facet buckets should be filtered on. | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetBucketFilter = Initialize-PSOpenAPIToolsFacetBucketFilter  -Facet null `
 -Prefix null
```

- Convert the resource to JSON
```powershell
$FacetBucketFilter | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

