# QueryInsight
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Query** | **String** | The query string the information is about. | 
**SearchCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**SearchorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**SearchWithClickCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**ClickCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**SimilarQueries** | [**QueryInsight[]**](QueryInsight.md) | list of similar queries to current one. | [optional] 

## Examples

- Prepare the resource
```powershell
$QueryInsight = Initialize-PSOpenAPIToolsQueryInsight  -Query null `
 -SearchCount null `
 -SearchorCount null `
 -SearchWithClickCount null `
 -ClickCount null `
 -SimilarQueries null
```

- Convert the resource to JSON
```powershell
$QueryInsight | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

