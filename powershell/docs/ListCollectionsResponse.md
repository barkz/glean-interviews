# ListCollectionsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Collections** | [**Collection[]**](Collection.md) | List of all Collections, no Collection items are fetched. | 

## Examples

- Prepare the resource
```powershell
$ListCollectionsResponse = Initialize-PSOpenAPIToolsListCollectionsResponse  -Collections null
```

- Convert the resource to JSON
```powershell
$ListCollectionsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

