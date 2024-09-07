# PersonTeam
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | Unique identifier | [optional] 
**Name** | **String** | Team name | [optional] 
**ExternalLink** | **String** | Link to a team page on the internet or your company&#39;s intranet | [optional] 
**Relationship** | **String** | The team member&#39;s relationship to the team. This defaults to MEMBER if not set. | [optional] [default to "MEMBER"]
**JoinDate** | **System.DateTime** | The team member&#39;s start date | [optional] 

## Examples

- Prepare the resource
```powershell
$PersonTeam = Initialize-PSOpenAPIToolsPersonTeam  -Id null `
 -Name null `
 -ExternalLink null `
 -Relationship null `
 -JoinDate null
```

- Convert the resource to JSON
```powershell
$PersonTeam | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

