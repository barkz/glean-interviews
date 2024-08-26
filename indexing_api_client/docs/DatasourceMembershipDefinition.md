# DatasourceMembershipDefinition

describes the membership row of a group. Only one of memberUserId and memberGroupName can be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group\_name** | **str** | The group for which the membership is specified | 
**member\_user\_id** | **str** | If the member is a user, then the email or datasource id for the user | [optional] 
**member\_group\_name** | **str** | If the member is a group, then the name of the member group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


