# FacetResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceName** | **String** | The source of this facet (e.g. container_name, type, last_updated_at). | [optional] 
**OperatorName** | **String** | How to display this facet. Currently supportes &#39;SelectSingle&#39; and &#39;SelectMultiple&#39;. | [optional] 
**Buckets** | [**FacetBucket[]**](FacetBucket.md) | A list of unique buckets that exist within this result set. | [optional] 
**HasMoreBuckets** | **Boolean** | Returns true if more buckets exist than those returned. Additional buckets can be retrieve by requesting again with a higher facetBucketSize. | [optional] 
**GroupName** | **String** | For most facets this will be the empty string, meaning the facet is high-level and applies to all documents for the datasource. When non-empty, this is used to group facets together (i.e. group facets for each doctype for a certain datasource) | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetResult = Initialize-PSOpenAPIToolsFacetResult  -SourceName container_name `
 -OperatorName SelectMultiple `
 -Buckets null `
 -HasMoreBuckets false `
 -GroupName Service Cloud
```

- Convert the resource to JSON
```powershell
$FacetResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

