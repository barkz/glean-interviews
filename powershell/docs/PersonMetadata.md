# PersonMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **String** |  | [optional] 
**FirstName** | **String** | The first name of the person | [optional] 
**LastName** | **String** | The last name of the person | [optional] 
**Title** | **String** | Job title. | [optional] 
**BusinessUnit** | **String** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**Department** | **String** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | [optional] 
**Teams** | [**PersonTeam[]**](PersonTeam.md) | Info about the employee&#39;s team(s). | [optional] 
**DepartmentCount** | **Int32** | The number of people in this person&#39;s department. | [optional] 
**Email** | **String** | The user&#39;s primary email address | [optional] 
**AliasEmails** | **String[]** | Additional email addresses of this user beyond the primary, if any. | [optional] 
**Location** | **String** | User facing string representing the person&#39;s location. | [optional] 
**StructuredLocation** | [**StructuredLocation**](StructuredLocation.md) |  | [optional] 
**ExternalProfileLink** | **String** | Link to a customer&#39;s internal profile page. This is set to &#39;#&#39; when no link is desired. | [optional] 
**Manager** | [**Person**](Person.md) |  | [optional] 
**ManagementChain** | [**Person[]**](Person.md) | The chain of reporting in the company as far up as it goes. The last entry is this person&#39;s direct manager. | [optional] 
**Phone** | **String** | Phone number as a number string. | [optional] 
**Timezone** | **String** | The timezone of the person. E.g. &quot;&quot;Pacific Daylight Time&quot;&quot;. | [optional] 
**TimezoneOffset** | **Int64** | The offset of the person&#39;s timezone in seconds from UTC. | [optional] 
**PhotoUrl** | **String** | The URL of the person&#39;s avatar. Public, glean-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**UneditedPhotoUrl** | **String** | The original photo URL of the person&#39;s avatar before any edits they made are applied | [optional] 
**BannerUrl** | **String** | The URL of the person&#39;s banner photo. | [optional] 
**Reports** | [**Person[]**](Person.md) |  | [optional] 
**StartDate** | **System.DateTime** | The date when the employee started. | [optional] 
**EndDate** | **System.DateTime** | If a former employee, the last date of employment. | [optional] 
**Bio** | **String** | Short biography or mission statement of the employee. | [optional] 
**Pronoun** | **String** | She/her, He/his or other pronoun. | [optional] 
**OrgSizeCount** | **Int32** | The total recursive size of the people reporting to this person, or 1 | [optional] 
**DirectReportsCount** | **Int32** | The total number of people who directly report to this person, or 0 | [optional] 
**PreferredName** | **String** | The preferred name of the person, or a nickname. | [optional] 
**SocialNetwork** | [**SocialNetwork[]**](SocialNetwork.md) | List of social network profiles. | [optional] 
**DatasourceProfile** | [**DatasourceProfile[]**](DatasourceProfile.md) | List of profiles this user has in different datasources / tools that they use. | [optional] 
**QuerySuggestions** | [**QuerySuggestionList**](QuerySuggestionList.md) |  | [optional] 
**PeopleDistance** | [**PersonDistance[]**](PersonDistance.md) | List of people and distances to those people from this person. Optionally with metadata. | [optional] 
**InviteInfo** | [**InviteInfo**](InviteInfo.md) |  | [optional] 
**IsSignedUp** | **Boolean** | Whether the user has signed into Glean at least once. | [optional] 
**LastExtensionUse** | **System.DateTime** | The last time the user has used the Glean extension in ISO 8601 format. | [optional] 
**Permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**CustomFields** | [**CustomFieldData[]**](CustomFieldData.md) | User customizable fields for additional people information. | [optional] 
**LoggingId** | **String** | The logging id of the person used in scrubbed logs, tracking GA metrics. | [optional] 
**StartDatePercentile** | **Double** | Percentage of the company that started strictly after this person. Between [0,100). | [optional] 
**BusyEvents** | [**AnonymousEvent[]**](AnonymousEvent.md) | Intervals of busy time for this person, along with the type of event they&#39;re busy with. | [optional] 
**ProfileBoolSettings** | **System.Collections.Hashtable** | flag settings to indicate user profile settings for certain items | [optional] 
**Badges** | [**Badge[]**](Badge.md) | The badges that a user has earned over their lifetime. | [optional] 
**IsOrgRoot** | **Boolean** | Whether this person is a &quot;&quot;root&quot;&quot; node in their organization&#39;s hierarchy. | [optional] 

## Examples

- Prepare the resource
```powershell
$PersonMetadata = Initialize-PSOpenAPIToolsPersonMetadata  -Type FULL_TIME `
 -FirstName null `
 -LastName null `
 -Title null `
 -BusinessUnit null `
 -Department null `
 -Teams null `
 -DepartmentCount null `
 -Email null `
 -AliasEmails null `
 -Location null `
 -StructuredLocation null `
 -ExternalProfileLink null `
 -Manager null `
 -ManagementChain null `
 -Phone null `
 -Timezone null `
 -TimezoneOffset null `
 -PhotoUrl null `
 -UneditedPhotoUrl null `
 -BannerUrl null `
 -Reports null `
 -StartDate null `
 -EndDate null `
 -Bio null `
 -Pronoun null `
 -OrgSizeCount null `
 -DirectReportsCount null `
 -PreferredName null `
 -SocialNetwork null `
 -DatasourceProfile null `
 -QuerySuggestions null `
 -PeopleDistance null `
 -InviteInfo null `
 -IsSignedUp null `
 -LastExtensionUse null `
 -Permissions null `
 -CustomFields null `
 -LoggingId null `
 -StartDatePercentile null `
 -BusyEvents null `
 -ProfileBoolSettings null `
 -Badges null `
 -IsOrgRoot null
```

- Convert the resource to JSON
```powershell
$PersonMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

