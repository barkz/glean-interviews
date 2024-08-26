# EmployeeInfoDefinition

Describes employee info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The employee&#39;s email | 
**department** | **str** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | 
**first\_name** | **str** | The first name of the employee. **Note**: The value cannot be empty  | [optional] 
**last\_name** | **str** | The last name of the employee. **Note**: The value cannot be empty  | [optional] 
**preferred\_name** | **str** | The preferred name or nickname of the employee | [optional] 
**id** | **str** | **[Advanced]** A unique universal internal identifier for the employee. This is solely used for understanding manager relationships along with &#x60;managerId&#x60;.  | [optional] 
**phone\_number** | **str** | The employee&#39;s phone number. | [optional] 
**location** | **str** | The employee&#39;s location (city/office name etc). | [optional] 
**structured\_location** | [**StructuredLocation**](StructuredLocation.md) |  | [optional] 
**title** | **str** | The employee&#39;s role title. | [optional] 
**photo\_url** | **str** | The employee&#39;s profile pic | [optional] 
**business\_unit** | **str** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**datasource\_profiles** | [**[DatasourceProfile]**](DatasourceProfile.md) | The datasource profiles of the employee, e.g. &#x60;Slack&#x60;,&#x60;Github&#x60;. | [optional] 
**teams** | [**[EmployeeTeamInfo]**](EmployeeTeamInfo.md) | Info about the employee&#39;s team(s) | [optional] 
**start\_date** | **date** | The date when the employee started | [optional] 
**end\_date** | **date** | If a former employee, the last date of employment. | [optional] 
**bio** | **str** | Short biography or mission statement of the employee. | [optional] 
**pronoun** | **str** | She/her, He/his or other pronoun. | [optional] 
**also\_known\_as** | **[str]** | Other names associated with the employee. | [optional] 
**profile\_url** | **str** | Link to internal company person profile. | [optional] 
**social\_networks** | [**[SocialNetworkDefinition]**](SocialNetworkDefinition.md) | List of social network profiles. | [optional] 
**manager\_email** | **str** | The email of the employee&#39;s manager | [optional] 
**manager\_id** | **str** | **[Advanced]** A unique universal internal identifier for the employee&#39;s manager. This is solely used in conjunction with &#x60;id&#x60;.  | [optional] 
**type** | **str** | The type of the employee, an enum of &#x60;FULL\_TIME&#x60;, &#x60;CONTRACTOR&#x60;, &#x60;NON\_EMPLOYEE&#x60; | [optional]  if omitted the server will use the default value of "FULL\_TIME"
**relationships** | [**[EntityRelationship]**](EntityRelationship.md) | List of unidirectional relationships with other employees. E.g. this employee (&#x60;A&#x60;) is a CHIEF\_OF\_STAFF to another employee (&#x60;B&#x60;); or this employee (&#x60;A&#x60;) is an EXECUTIVE\_ASSISTANT of another employee (&#x60;C&#x60;). The mapping should be attached to &#x60;A&#x60;&#39;s profile. | [optional] 
**status** | **str** | The status of the employee, an enum of &#x60;CURRENT&#x60;, &#x60;FUTURE&#x60;, &#x60;EX&#x60; | [optional]  if omitted the server will use the default value of "CURRENT"
**additional\_fields** | [**[AdditionalFieldDefinition]**](AdditionalFieldDefinition.md) | List of additional fields with more information about the employee. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


