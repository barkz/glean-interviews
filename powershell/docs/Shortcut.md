# Shortcut
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Int32** | The opaque id of the user generated content. | [optional] 
**InputAlias** | **String** | Link text following go/ prefix as entered by the user. | 
**DestinationUrl** | **String** | Destination URL for the shortcut. | [optional] 
**DestinationDocumentId** | **String** | Glean Document ID for the URL, if known. | [optional] 
**Description** | **String** | A short, plain text blurb to help people understand the intent of the shortcut. | [optional] 
**Unlisted** | **Boolean** | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only. | [optional] 
**UrlTemplate** | **String** | For variable shortcuts, contains the URL template; note, &#x60;destinationUrl&#x60; contains default URL. | [optional] 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles added for the Shortcut. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles removed for the Shortcut. | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**CreatedBy** | [**Person**](Person.md) |  | [optional] 
**CreateTime** | **System.DateTime** | The time the shortcut was created in ISO format (ISO 8601). | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**UpdateTime** | **System.DateTime** | The time the shortcut was updated in ISO format (ISO 8601). | [optional] 
**DestinationDocument** | [**Document**](Document.md) |  | [optional] 
**IntermediateUrl** | **String** | The URL from which the user is then redirected to the destination URL. Full replacement for https://go/&lt;inputAlias&gt;. | [optional] 
**ViewPrefix** | **String** | The part of the shortcut preceding the input alias when used for showing shortcuts to users. Should end with &quot;&quot;/&quot;&quot;. e.g. &quot;&quot;go/&quot;&quot; for native shortcuts. | [optional] 
**IsExternal** | **Boolean** | Indicates whether a shortcut is native or external. | [optional] 
**EditUrl** | **String** | The URL using which the user can access the edit page of the shortcut. | [optional] 
**Alias** | **String** | canonical link text following go/ prefix where hyphen/underscore is removed. | [optional] 
**Title** | **String** | Title for the Go Link | [optional] 
**Roles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles for the Go Link. | [optional] 

## Examples

- Prepare the resource
```powershell
$Shortcut = Initialize-PSOpenAPIToolsShortcut  -Id null `
 -InputAlias null `
 -DestinationUrl null `
 -DestinationDocumentId null `
 -Description null `
 -Unlisted null `
 -UrlTemplate null `
 -AddedRoles null `
 -RemovedRoles null `
 -Permissions null `
 -CreatedBy null `
 -CreateTime null `
 -UpdatedBy null `
 -UpdateTime null `
 -DestinationDocument null `
 -IntermediateUrl null `
 -ViewPrefix null `
 -IsExternal null `
 -EditUrl null `
 -Alias null `
 -Title null `
 -Roles null
```

- Convert the resource to JSON
```powershell
$Shortcut | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

