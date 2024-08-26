# BulkIndexEmployeesRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employees** | [**[EmployeeInfoDefinition]**](EmployeeInfoDefinition.md) | Batch of employee information | 
**disable\_stale\_data\_deletion\_check** | **bool** | True if older employee data needs to be force deleted after the upload completes. Defaults to older data being deleted only if the percentage of data being deleted is less than 20%. This must only be set when &#x60;isLastPage &#x3D; true&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


