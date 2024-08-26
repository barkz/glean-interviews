# GetDocumentStatusResponse

Describes the response body of the /getdocumentstatus API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload\_status** | **str** | Upload status, enum of NOT\_UPLOADED, UPLOADED, STATUS\_UNKNOWN | [optional] 
**last\_uploaded\_at** | **int** | Time of last successful upload, in epoch seconds | [optional] 
**indexing\_status** | **str** | Indexing status, enum of NOT\_INDEXED, INDEXED, STATUS\_UNKNOWN | [optional] 
**last\_indexed\_at** | **int** | Time of last successful indexing, in epoch seconds | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


