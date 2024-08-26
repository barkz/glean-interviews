# DeleteDocumentRequest

Describes the request body of the /deletedocument API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | datasource of the document | 
**object\_type** | **str** | object type of the document | 
**id** | **str** | The id of the document | 
**version** | **int** | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


