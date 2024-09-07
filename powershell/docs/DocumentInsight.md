# DocumentInsight
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Document** | [**Document**](Document.md) |  | 
**ViewCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**VisitorCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentInsight = Initialize-PSOpenAPIToolsDocumentInsight  -Document null `
 -ViewCount null `
 -VisitorCount null
```

- Convert the resource to JSON
```powershell
$DocumentInsight | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

