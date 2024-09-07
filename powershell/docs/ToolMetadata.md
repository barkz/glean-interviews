# ToolMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **String** | The type of tool. | 
**Name** | **String** | Unique identifier for the tool. Name should be understandable by the LLM, and will be used to invoke a tool. | 
**DisplayName** | **String** | Human understandable name of the tool. Max 50 characters. | 
**ToolId** | **String** | An opaque id which is unique identifier for the tool. | [optional] 
**DisplayDescription** | **String** | Description of the tool meant for a human. | 
**LogoUrl** | **String** | URL used to fetch the logo. | [optional] 
**ObjectName** | **String** | Name of the generated object. This will be used to indicate to the end user what the generated object contains. | [optional] 
**CreatedBy** | [**PersonObject**](PersonObject.md) |  | [optional] 
**LastUpdatedBy** | [**PersonObject**](PersonObject.md) |  | [optional] 
**CreatedAt** | **System.DateTime** | The time the tool was created in ISO format (ISO 8601) | [optional] 
**LastUpdatedAt** | **System.DateTime** | The time the tool was last updated in ISO format (ISO 8601) | [optional] 
**Auth** | [**AuthConfig**](AuthConfig.md) |  | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ToolMetadata = Initialize-PSOpenAPIToolsToolMetadata  -Type null `
 -Name null `
 -DisplayName null `
 -ToolId null `
 -DisplayDescription null `
 -LogoUrl null `
 -ObjectName [&quot;HR ticket&quot;,&quot;Email&quot;,&quot;Chat message&quot;] `
 -CreatedBy null `
 -LastUpdatedBy null `
 -CreatedAt null `
 -LastUpdatedAt null `
 -Auth null `
 -Permissions null
```

- Convert the resource to JSON
```powershell
$ToolMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

