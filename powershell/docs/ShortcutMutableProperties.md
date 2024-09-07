# ShortcutMutableProperties
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InputAlias** | **String** | Link text following go/ prefix as entered by the user. | [optional] 
**DestinationUrl** | **String** | Destination URL for the shortcut. | [optional] 
**DestinationDocumentId** | **String** | Glean Document ID for the URL, if known. | [optional] 
**Description** | **String** | A short, plain text blurb to help people understand the intent of the shortcut. | [optional] 
**Unlisted** | **Boolean** | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only. | [optional] 
**UrlTemplate** | **String** | For variable shortcuts, contains the URL template; note, &#x60;destinationUrl&#x60; contains default URL. | [optional] 
**AddedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles added for the Shortcut. | [optional] 
**RemovedRoles** | [**UserRoleSpecification[]**](UserRoleSpecification.md) | A list of user roles removed for the Shortcut. | [optional] 

## Examples

- Prepare the resource
```powershell
$ShortcutMutableProperties = Initialize-PSOpenAPIToolsShortcutMutableProperties  -InputAlias null `
 -DestinationUrl null `
 -DestinationDocumentId null `
 -Description null `
 -Unlisted null `
 -UrlTemplate null `
 -AddedRoles null `
 -RemovedRoles null
```

- Convert the resource to JSON
```powershell
$ShortcutMutableProperties | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

