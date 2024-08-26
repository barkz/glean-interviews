# DocumentPermissionsDefinition

describes the access control details of the document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed\_users** | [**[UserReferenceDefinition]**](UserReferenceDefinition.md) | List of users who can view the document | [optional] 
**allowed\_groups** | **[str]** | List of groups that can view the document | [optional] 
**allowed\_group\_intersections** | [**[PermissionsGroupIntersectionDefinition]**](PermissionsGroupIntersectionDefinition.md) | List of allowed group intersections. This describes a permissions constraint of the form ((GroupA AND GroupB AND GroupC) OR (GroupX AND GroupY) OR ... | [optional] 
**allow\_anonymous\_access** | **bool** | If true, then any Glean user can view the document | [optional] 
**allow\_all\_datasource\_users\_access** | **bool** | If true, then any user who has an account in the datasource can view the document. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


