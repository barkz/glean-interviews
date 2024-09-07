# SearchWarning
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WarningType** | **String** | The type of the warning. | 
**LastUsedTerm** | **String** | The last term we considered in the user&#39;s long query. | [optional] 
**QuotesIgnoredQuery** | **String** | The query after ignoring/removing quotes. | [optional] 
**IgnoredTerms** | **String[]** | A list of query terms that were ignored when generating search results, if any. For example, terms containing invalid filters such as &quot;&quot;updated:invalid_date&quot;&quot; will be ignored. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchWarning = Initialize-PSOpenAPIToolsSearchWarning  -WarningType null `
 -LastUsedTerm null `
 -QuotesIgnoredQuery null `
 -IgnoredTerms null
```

- Convert the resource to JSON
```powershell
$SearchWarning | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

