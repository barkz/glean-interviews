# TeamInfoDefinition

Information about an employee's team

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the team | 
**name** | **str** | Human-readable team name | 
**members** | [**[TeamMember]**](TeamMember.md) | The members of the team | 
**description** | **str** | The description of this team | [optional] 
**business\_unit** | **str** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**department** | **str** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | [optional] 
**photo\_url** | **str** | A link to the team&#39;s photo | [optional] 
**external\_link** | **str** | A link to an external team page. If set, team results will link to it.  | [optional] 
**emails** | [**[TeamEmail]**](TeamEmail.md) | The emails of the team | [optional] 
**datasource\_profiles** | [**[DatasourceProfile]**](DatasourceProfile.md) | The datasource profiles of the team, e.g. &#x60;Slack&#x60;,&#x60;Github&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


