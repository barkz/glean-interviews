# PersonToTeamRelationship
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Person** | [**Person**](Person.md) |  | 
**Relationship** | **String** | The team member&#39;s relationship to the team. This defaults to MEMBER if not set. | [optional] [default to "MEMBER"]
**CustomRelationshipStr** | **String** | Displayed name for the relationship if relationship is set to &#x60;OTHER&#x60;. | [optional] 
**JoinDate** | **System.DateTime** | The team member&#39;s start date | [optional] 

## Examples

- Prepare the resource
```powershell
$PersonToTeamRelationship = Initialize-PSOpenAPIToolsPersonToTeamRelationship  -Person null `
 -Relationship null `
 -CustomRelationshipStr null `
 -JoinDate null
```

- Convert the resource to JSON
```powershell
$PersonToTeamRelationship | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

