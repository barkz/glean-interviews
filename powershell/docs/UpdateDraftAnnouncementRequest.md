# UpdateDraftAnnouncementRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartTime** | **System.DateTime** | The date and time at which the announcement becomes active. | [optional] 
**EndTime** | **System.DateTime** | The date and time at which the announcement expires. | [optional] 
**Title** | **String** | The headline of the announcement. | [optional] 
**Body** | [**StructuredText**](StructuredText.md) |  | [optional] 
**Emoji** | **String** | An emoji used to indicate the nature of the announcement. | [optional] 
**Thumbnail** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**Banner** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**AudienceFilters** | [**FacetFilter[]**](FacetFilter.md) | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search. | [optional] 
**SourceDocumentId** | **String** | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread). | [optional] 
**HideAttribution** | **Boolean** | Whether or not to hide an author attribution. | [optional] 
**Channel** | **String** | This determines whether this is a Social Feed post or a regular announcement. | [optional] 
**PostType** | **String** | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. | [optional] 
**IsPrioritized** | **Boolean** | Used by the Social Feed to pin posts to the front of the feed. | [optional] 
**ViewUrl** | **String** | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel&#x3D;&quot;&quot;SOCIAL_FEED&quot;&quot;. | [optional] 
**Id** | **Int32** | The opaque id of the announcement. | [optional] 
**DraftId** | **Int32** | The opaque id of the draft. | 

## Examples

- Prepare the resource
```powershell
$UpdateDraftAnnouncementRequest = Initialize-PSOpenAPIToolsUpdateDraftAnnouncementRequest  -StartTime null `
 -EndTime null `
 -Title null `
 -Body null `
 -Emoji null `
 -Thumbnail null `
 -Banner null `
 -AudienceFilters null `
 -SourceDocumentId null `
 -HideAttribution null `
 -Channel null `
 -PostType null `
 -IsPrioritized null `
 -ViewUrl null `
 -Id null `
 -DraftId null
```

- Convert the resource to JSON
```powershell
$UpdateDraftAnnouncementRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

