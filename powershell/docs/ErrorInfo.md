# ErrorInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BadGmailToken** | **Boolean** | Indicates the gmail results could not be fetched due to bad token. | [optional] 
**BadOutlookToken** | **Boolean** | Indicates the outlook results could not be fetched due to bad token. | [optional] 
**InvalidOperators** | [**InvalidOperatorValueError[]**](InvalidOperatorValueError.md) | Indicates results could not be fetched due to invalid operators in the query. | [optional] 
**ErrorMessages** | [**ErrorMessage[]**](ErrorMessage.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ErrorInfo = Initialize-PSOpenAPIToolsErrorInfo  -BadGmailToken null `
 -BadOutlookToken null `
 -InvalidOperators null `
 -ErrorMessages null
```

- Convert the resource to JSON
```powershell
$ErrorInfo | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

