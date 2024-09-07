# DocumentMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** |  | [optional] 
**DatasourceInstance** | **String** | The datasource instance from which the document was extracted. | [optional] 
**ObjectType** | **String** | The type of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**Container** | **String** | The name of the container (higher level parent, not direct parent) of the result. Interpretation is specific to each datasource (e.g. Channels for Slack, Project for Jira). cf. parentId | [optional] 
**ContainerId** | **String** | The Glean Document ID of the container. Uniquely identifies the container. | [optional] 
**SuperContainerId** | **String** | The Glean Document ID of the super container. Super container represents a broader abstraction that contains many containers. For example, whereas container might refer to a folder, super container would refer to a drive. | [optional] 
**ParentId** | **String** | The id of the direct parent of the result. Interpretation is specific to each datasource (e.g. parent issue for Jira). cf. container | [optional] 
**MimeType** | **String** |  | [optional] 
**DocumentId** | **String** | The index-wide unique identifier. | [optional] 
**LoggingId** | **String** | A unique identifier used to represent the document in any logging or feedback requests in place of documentId. | [optional] 
**DocumentIdHash** | **String** | Hash of the Glean Document ID. | [optional] 
**CreateTime** | **System.DateTime** |  | [optional] 
**UpdateTime** | **System.DateTime** |  | [optional] 
**Author** | [**Person**](Person.md) |  | [optional] 
**Owner** | [**Person**](Person.md) |  | [optional] 
**Visibility** | [**DocumentVisibility**](DocumentVisibility.md) |  | [optional] 
**Components** | **String[]** | A list of components this result is associated with. Interpretation is specific to each datasource. (e.g. for Jira issues, these are [components](https://confluence.atlassian.com/jirasoftwarecloud/organizing-work-with-components-764478279.html).) | [optional] 
**Status** | **String** | The status or disposition of the result. Interpretation is specific to each datasource. (e.g. for Jira issues, this is the issue status such as Done, In Progress or Will Not Fix). | [optional] 
**StatusCategory** | **String** | The status category of the result. Meant to be more general than status. Interpretation is specific to each datasource. | [optional] 
**Pins** | [**PinDocument[]**](PinDocument.md) | A list of stars associated with this result.  &quot;&quot;Pin&quot;&quot; is an older name. | [optional] 
**Priority** | **String** | The document priority. Interpretation is datasource specific. | [optional] 
**AssignedTo** | [**Person**](Person.md) |  | [optional] 
**UpdatedBy** | [**Person**](Person.md) |  | [optional] 
**Labels** | **String[]** | A list of tags for the document. Interpretation is datasource specific. | [optional] 
**Collections** | [**Collection[]**](Collection.md) | A list of collections that the document belongs to. | [optional] 
**DatasourceId** | **String** | The user-visible datasource specific id (e.g. Salesforce case number for example, GitHub PR number). | [optional] 
**Interactions** | [**DocumentInteractions**](DocumentInteractions.md) |  | [optional] 
**Verification** | [**Verification**](Verification.md) |  | [optional] 
**ViewerInfo** | [**ViewerInfo**](ViewerInfo.md) |  | [optional] 
**Permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**VisitCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**Shortcuts** | [**Shortcut[]**](Shortcut.md) | A list of shortcuts of which destination URL is for the document. | [optional] 
**Path** | **String** | For file datasources like onedrive/github etc this has the path to the file | [optional] 
**CustomData** | [**System.Collections.Hashtable**](CustomDataValue.md) | Custom fields specific to individual datasources | [optional] 
**DocumentCategory** | **String** | The document&#39;s document_category(.proto). | [optional] 
**ContactPerson** | [**Person**](Person.md) |  | [optional] 
**Thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**IndexStatus** | [**IndexStatus**](IndexStatus.md) |  | [optional] 
**Ancestors** | [**Document[]**](Document.md) | A list of documents that are ancestors of this document in the hierarchy of the document&#39;s datasource, for example parent folders or containers. Ancestors can be of different types and some may not be indexed. Higher level ancestors appear earlier in the list. | [optional] 

## Examples

- Prepare the resource
```powershell
$DocumentMetadata = Initialize-PSOpenAPIToolsDocumentMetadata  -Datasource null `
 -DatasourceInstance null `
 -ObjectType null `
 -Container null `
 -ContainerId null `
 -SuperContainerId null `
 -ParentId null `
 -MimeType null `
 -DocumentId null `
 -LoggingId null `
 -DocumentIdHash null `
 -CreateTime null `
 -UpdateTime null `
 -Author null `
 -Owner null `
 -Visibility null `
 -Components null `
 -Status null `
 -StatusCategory null `
 -Pins null `
 -Priority null `
 -AssignedTo null `
 -UpdatedBy null `
 -Labels null `
 -Collections null `
 -DatasourceId null `
 -Interactions null `
 -Verification null `
 -ViewerInfo null `
 -Permissions null `
 -VisitCount null `
 -Shortcuts null `
 -Path null `
 -CustomData null `
 -DocumentCategory null `
 -ContactPerson null `
 -Thumbnail null `
 -IndexStatus null `
 -Ancestors null
```

- Convert the resource to JSON
```powershell
$DocumentMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

