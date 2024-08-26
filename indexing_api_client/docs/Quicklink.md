# Quicklink

An action for a specific datasource that will show up in autocomplete and app card, e.g. \"Create new issue\" for jira.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full action name. Used in autocomplete. | [optional] 
**short\_name** | **str** | Shortened name. Used in app cards. | [optional] 
**url** | **str** | The URL of the action. | [optional] 
**icon\_config** | [**IconConfig**](IconConfig.md) |  | [optional] 
**id** | **str** | Unique identifier of this quicklink | [optional] 
**scopes** | **[str]** | The scopes for which this quicklink is applicable | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


