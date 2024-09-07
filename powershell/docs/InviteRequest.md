# InviteRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Channel** | [**CommunicationChannel**](CommunicationChannel.md) |  | [optional] 
**Template** | [**CommunicationTemplate**](CommunicationTemplate.md) |  | [optional] 
**Recipients** | [**Person[]**](Person.md) | The people who should receive this invite | [optional] 
**RecipientFilters** | [**PeopleFilters**](PeopleFilters.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$InviteRequest = Initialize-PSOpenAPIToolsInviteRequest  -Channel null `
 -Template null `
 -Recipients null `
 -RecipientFilters null
```

- Convert the resource to JSON
```powershell
$InviteRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

