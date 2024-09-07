# PeopleRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TimezoneOffset** | **Int32** | The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 
**ObfuscatedIds** | **String[]** | The Person IDs to retrieve. If no IDs are requested, the current user&#39;s details are returned. | [optional] 
**EmailIds** | **String[]** | The email IDs to retrieve. The result is the deduplicated union of emailIds and obfuscatedIds. | [optional] 
**IncludeFields** | **String[]** | List of PersonMetadata fields to return (that aren&#39;t returned by default) | [optional] 
**IncludeTypes** | **String[]** | The types of people entities to include in the response in addition to those returned by default. | [optional] 
**Source** | **String** | A string denoting the search surface from which the endpoint is called. | [optional] 

## Examples

- Prepare the resource
```powershell
$PeopleRequest = Initialize-PSOpenAPIToolsPeopleRequest  -TimezoneOffset null `
 -ObfuscatedIds null `
 -EmailIds null `
 -IncludeFields null `
 -IncludeTypes null `
 -Source null
```

- Convert the resource to JSON
```powershell
$PeopleRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

