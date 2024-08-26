# BulkIndexDocumentsRequest

Describes the request body of the /bulkindexdocuments API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload\_id** | **str** | Unique id that must be used for this bulk upload instance | 
**datasource** | **str** | Datasource of the documents | 
**documents** | [**[DocumentDefinition]**](DocumentDefinition.md) | Batch of documents for the datasource | 
**is\_first\_page** | **bool** | true if this is the first page of the upload. Defaults to false | [optional] 
**is\_last\_page** | **bool** | true if this is the last page of the upload. Defaults to false | [optional] 
**force\_restart\_upload** | **bool** | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage&#x3D;true | [optional] 
**disable\_stale\_document\_deletion\_check** | **bool** | True if older documents need to be force deleted after the upload completes. Defaults to older documents being deleted asynchronously. This must only be set when &#x60;isLastPage &#x3D; true&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


