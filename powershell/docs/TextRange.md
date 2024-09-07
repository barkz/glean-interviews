# TextRange
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartIndex** | **Int32** | The inclusive start index of the range. | 
**EndIndex** | **Int32** | The exclusive end index of the range. | [optional] 
**Type** | **String** |  | [optional] 
**Url** | **String** | The URL associated with the range, if applicable. For example, the linked URL for a LINK range. | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$TextRange = Initialize-PSOpenAPIToolsTextRange  -StartIndex null `
 -EndIndex null `
 -Type null `
 -Url null `
 -Document null
```

- Convert the resource to JSON
```powershell
$TextRange | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

