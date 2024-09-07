# Code
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RepoName** | **String** |  | [optional] 
**FileName** | **String** |  | [optional] 
**FileUrl** | **String** |  | [optional] 
**Lines** | [**CodeLine[]**](CodeLine.md) |  | [optional] 
**IsLastMatch** | **Boolean** | Last file match for a repo | [optional] 

## Examples

- Prepare the resource
```powershell
$Code = Initialize-PSOpenAPIToolsCode  -RepoName null `
 -FileName null `
 -FileUrl null `
 -Lines null `
 -IsLastMatch null
```

- Convert the resource to JSON
```powershell
$Code | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

