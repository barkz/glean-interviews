# Team
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RelatedObjects** | [**System.Collections.Hashtable**](RelatedObjectEdge.md) | A list of objects related to a source object. | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**Id** | **String** | Unique identifier | 
**Name** | **String** | Team name | 
**Description** | **String** | A description of the team | [optional] 
**BusinessUnit** | **String** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**Department** | **String** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | [optional] 
**PhotoUrl** | **String** | A link to the team&#39;s photo. | [optional] 
**BannerUrl** | **String** | A link to the team&#39;s banner photo. | [optional] 
**ExternalLink** | **String** | Link to a team page on the internet or your company&#39;s intranet | [optional] 
**Members** | [**PersonToTeamRelationship[]**](PersonToTeamRelationship.md) | The members on this team | [optional] 
**MemberCount** | **Int32** | Number of members on this team (recursive; includes all individuals that belong to this team, and all individuals that belong to a subteam within this team) | [optional] 
**Emails** | [**TeamEmail[]**](TeamEmail.md) | The emails for this team | [optional] 
**DatasourceProfiles** | [**DatasourceProfile[]**](DatasourceProfile.md) | The datasource profiles of the team | [optional] 
**Datasource** | **String** | the data source of the team, e.g. GDRIVE | [optional] 
**CreatedFrom** | **String** | For teams created from docs, the doc title. Otherwise empty. | [optional] 
**LastUpdatedAt** | **System.DateTime** | when this team was last updated. | [optional] 
**Status** | **String** | whether this team is fully processed or there are still unprocessed operations that&#39;ll affect it | [optional] [default to "PROCESSED"]
**CanBeDeleted** | **Boolean** | can this team be deleted. Some manually ingested teams like GCS_CSV or PUSH_API cannot | [optional] [default to $true]
**LoggingId** | **String** | The logging id of the team used in scrubbed logs, client analytics, and metrics. | [optional] 

## Examples

- Prepare the resource
```powershell
$Team = Initialize-PSOpenAPIToolsTeam  -RelatedObjects null `
 -Permissions null `
 -Id null `
 -Name null `
 -Description null `
 -BusinessUnit null `
 -Department null `
 -PhotoUrl null `
 -BannerUrl null `
 -ExternalLink null `
 -Members null `
 -MemberCount null `
 -Emails null `
 -DatasourceProfiles null `
 -Datasource null `
 -CreatedFrom null `
 -LastUpdatedAt null `
 -Status null `
 -CanBeDeleted null `
 -LoggingId null
```

- Convert the resource to JSON
```powershell
$Team | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

