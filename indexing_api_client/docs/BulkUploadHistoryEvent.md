# BulkUploadHistoryEvent

Information about a successful bulk upload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload\_id** | **str** | The unique ID of the upload | [optional] 
**start\_time\_ms** | **int** | The start time of the upload in milliseconds since the epoch | [optional] 
**start\_time** | **str** | The start time of the upload in ISO 8601 format | [optional] 
**end\_time\_ms** | **int** | The end time of the upload in milliseconds since the epoch, -1 if the upload is still active | [optional] 
**end\_time** | **str** | The end time of the upload in ISO 8601 format, &#39;NA&#39; if the upload is still active | [optional] 
**status** | **str** | The status of the upload, an enum of ACTIVE, SUCCESSFUL | [optional] 
**processing\_state** | **str** | The current state of the upload, an enum of UNAVAILABLE, UPLOAD STARTED, UPLOAD IN PROGRESS, UPLOAD COMPLETED, DELETION PAUSED, INDEXING COMPLETED | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


