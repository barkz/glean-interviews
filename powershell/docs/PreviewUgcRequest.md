# PreviewUgcRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Draft** | [**UgcDraft**](UgcDraft.md) |  | [optional] 
**DraftSpec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**Type** | [**UgcType**](UgcType.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$PreviewUgcRequest = Initialize-PSOpenAPIToolsPreviewUgcRequest  -Draft null `
 -DraftSpec null `
 -Type null
```

- Convert the resource to JSON
```powershell
$PreviewUgcRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

