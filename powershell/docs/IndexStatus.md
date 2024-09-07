# IndexStatus
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LastCrawledTime** | **System.DateTime** | When the document was last crawled | [optional] 
**LastIndexedTime** | **System.DateTime** | When the document was last indexed | [optional] 

## Examples

- Prepare the resource
```powershell
$IndexStatus = Initialize-PSOpenAPIToolsIndexStatus  -LastCrawledTime null `
 -LastIndexedTime null
```

- Convert the resource to JSON
```powershell
$IndexStatus | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

