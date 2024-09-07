# ToolConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DisplayName** | **String** | Human understandable name of the tool. Max 50 characters. | [optional] 
**ObjectName** | **String** | Name of the generated object. This will be used to indicate to the end user what the generated object contains. | [optional] 
**LogoUrl** | **String** | URL used to fetch the logo. | [optional] 
**Type** | **String** | Valid only for ACTION tools. Represents the type of action tool REDIRECT - The client renders the URL which contains information for carrying out the action. EXECUTION - Send a request to an external server and execute the action. | [optional] 

## Examples

- Prepare the resource
```powershell
$ToolConfig = Initialize-PSOpenAPIToolsToolConfig  -DisplayName null `
 -ObjectName [&quot;HR ticket&quot;,&quot;Email&quot;,&quot;Chat message&quot;] `
 -LogoUrl null `
 -Type null
```

- Convert the resource to JSON
```powershell
$ToolConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

