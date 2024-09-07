# TeamEmail
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **String** | An email address | [optional] 
**Type** | **String** |  | [optional] [default to "OTHER"]
**IsUserGenerated** | **Boolean** | true iff the email was manually added by a user from within Glean (aka not from the original data source) | [optional] 

## Examples

- Prepare the resource
```powershell
$TeamEmail = Initialize-PSOpenAPIToolsTeamEmail  -Email null `
 -Type null `
 -IsUserGenerated null
```

- Convert the resource to JSON
```powershell
$TeamEmail | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

