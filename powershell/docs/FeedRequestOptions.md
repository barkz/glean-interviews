# FeedRequestOptions
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ResultSize** | **Int32** | Number of results asked in response. If a result is a collection, counts as one. | 
**TimezoneOffset** | **Int32** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**CategoryToResultSize** | [**System.Collections.Hashtable**](FeedRequestOptionsCategoryToResultSizeValue.md) | Mapping from category to number of results asked for the category. | [optional] 
**DatasourceFilter** | **String[]** | Datasources for which content should be included. Empty is for all. | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedRequestOptions = Initialize-PSOpenAPIToolsFeedRequestOptions  -ResultSize null `
 -TimezoneOffset null `
 -CategoryToResultSize null `
 -DatasourceFilter null
```

- Convert the resource to JSON
```powershell
$FeedRequestOptions | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

