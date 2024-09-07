# PeopleResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**Person[]**](Person.md) | A Person for each ID in the request, each with PersonMetadata populated. | [optional] 
**RelatedDocuments** | [**RelatedDocuments[]**](RelatedDocuments.md) | A list of documents related to this people response. This is only included if DOCUMENT_ACTIVITY is requested and only 1 person is included in the request. | [optional] 
**Errors** | **String[]** | A list of IDs that could not be found. | [optional] 

## Examples

- Prepare the resource
```powershell
$PeopleResponse = Initialize-PSOpenAPIToolsPeopleResponse  -Results null `
 -RelatedDocuments null `
 -Errors null
```

- Convert the resource to JSON
```powershell
$PeopleResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

