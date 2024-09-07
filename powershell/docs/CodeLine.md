# CodeLine
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LineNumber** | **Int32** |  | [optional] 
**Content** | **String** |  | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | Index ranges depicting matched sections of the line | [optional] 

## Examples

- Prepare the resource
```powershell
$CodeLine = Initialize-PSOpenAPIToolsCodeLine  -LineNumber null `
 -Content null `
 -Ranges null
```

- Convert the resource to JSON
```powershell
$CodeLine | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

