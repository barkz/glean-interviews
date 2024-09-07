# GetDocPermissionsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AllowedUserEmails** | **String[]** | A list of emails of users who have access to the document. If the document is visible to all Glean users, a list with only a single value of &#39;VISIBLE_TO_ALL&#39;. | [optional] 

## Examples

- Prepare the resource
```powershell
$GetDocPermissionsResponse = Initialize-PSOpenAPIToolsGetDocPermissionsResponse  -AllowedUserEmails null
```

- Convert the resource to JSON
```powershell
$GetDocPermissionsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

