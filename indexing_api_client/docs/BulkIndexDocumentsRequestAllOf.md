# BulkIndexDocumentsRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | Datasource of the documents | 
**documents** | [**[DocumentDefinition]**](DocumentDefinition.md) | Batch of documents for the datasource | 
**disable\_stale\_document\_deletion\_check** | **bool** | True if older documents need to be force deleted after the upload completes. Defaults to older documents being deleted asynchronously. This must only be set when &#x60;isLastPage &#x3D; true&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


