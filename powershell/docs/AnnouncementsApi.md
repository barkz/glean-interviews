# PSOpenAPITools.PSOpenAPITools\Api.AnnouncementsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**New-announcement**](AnnouncementsApi.md#New-announcement) | **POST** /createannouncement | Create Announcement
[**New-draftannouncement**](AnnouncementsApi.md#New-draftannouncement) | **POST** /createdraftannouncement | Create draft Announcement
[**Invoke-Deleteannouncement**](AnnouncementsApi.md#Invoke-Deleteannouncement) | **POST** /deleteannouncement | Delete Announcement
[**Invoke-Deletedraftannouncement**](AnnouncementsApi.md#Invoke-Deletedraftannouncement) | **POST** /deletedraftannouncement | Delete draft Announcement
[**Get-announcement**](AnnouncementsApi.md#Get-announcement) | **POST** /getannouncement | Read Announcement
[**Get-draftannouncement**](AnnouncementsApi.md#Get-draftannouncement) | **POST** /getdraftannouncement | Read draft Announcement
[**Invoke-Listannouncements**](AnnouncementsApi.md#Invoke-Listannouncements) | **POST** /listannouncements | List Announcements
[**Invoke-Previewannouncement**](AnnouncementsApi.md#Invoke-Previewannouncement) | **POST** /previewannouncement | Preview Announcement
[**Invoke-Previewannouncementdraft**](AnnouncementsApi.md#Invoke-Previewannouncementdraft) | **POST** /previewannouncementdraft | Preview draft Announcement
[**Publish-draftannouncement**](AnnouncementsApi.md#Publish-draftannouncement) | **POST** /publishdraftannouncement | Publish draft Announcement
[**Unpublish-announcement**](AnnouncementsApi.md#Unpublish-announcement) | **POST** /unpublishannouncement | Unpublish Announcement
[**Update-announcement**](AnnouncementsApi.md#Update-announcement) | **POST** /updateannouncement | Update Announcement
[**Update-draftannouncement**](AnnouncementsApi.md#Update-draftannouncement) | **POST** /updatedraftannouncement | Update draft Announcement


<a id="New-announcement"></a>
# **New-announcement**
> Announcement New-announcement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create Announcement

Create a textual announcement visible to some set of users based on department and location.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Answer = Initialize-Answer -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -Permissions $ObjectPermissions -CombinedAnswerText $StructuredText -Likes $AnswerLikes -Author $Person -CreateTime (Get-Date) -UpdateTime (Get-Date) -UpdatedBy $Person -Verification $Verification -Board $AnswerBoard -Collections $Collection -DocumentCategory "MyDocumentCategory" -SourceDocument $Document

$ExtractedQnA = Initialize-ExtractedQnA -Heading "MyHeading" -Question "MyQuestion" -QuestionResult $SearchResult

$AppResult = Initialize-AppResult -Datasource "MyDatasource" -DocType "MyDocType" -MimeType "MyMimeType" -IconUrl "MyIconUrl"

$CodeLine = Initialize-CodeLine -LineNumber 0 -Content "MyContent" -Ranges $TextRange

$Code = Initialize-Code -RepoName "MyRepoName" -FileName "MyFileName" -FileUrl "MyFileUrl" -Lines $CodeLine -IsLastMatch $false

$QuerySuggestionList = Initialize-QuerySuggestionList -Suggestions $QuerySuggestion -Person $Person

$RelatedQuestion = Initialize-RelatedQuestion -Question "MyQuestion" -Answer "MyAnswer" -Ranges $TextRange

$SearchResultSnippet = Initialize-SearchResultSnippet -Snippet "MySnippet" -MimeType "MyMimeType" -Text "MyText" -SnippetTextOrdering 0 -Ranges $TextRange -Url "MyUrl"

$StructuredResult = Initialize-StructuredResult -Document $Document -Person $Person -Customer $Customer -Team $Team -CustomEntity $CustomEntity -Answer $Answer -ExtractedQnA $ExtractedQnA -App $AppResult -Collection $Collection -AnswerBoard $AnswerBoard -Code $Code -Shortcut $Shortcut -QuerySuggestions $QuerySuggestionList -RelatedDocuments $RelatedDocuments -RelatedQuestion $RelatedQuestion -Snippets $SearchResultSnippet -TrackingToken "MyTrackingToken" -Prominence "HERO" -Source "EXPERT_DETECTION"

$ClusterGroup = Initialize-ClusterGroup -ClusteredResults $SearchResult -ClusterType "SIMILAR" -VisibleCountHint 0

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$SearchResult = Initialize-SearchResult -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Document $Document -Title "MyTitle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -Snippets $SearchResultSnippet -ExpandedSnippets "MyExpandedSnippets" -FullText "MyFullText" -FullTextList "MyFullTextList" -RelatedResults $RelatedDocuments -ClusteredResults $SearchResult -AllClusteredResults $ClusterGroup -AttachmentCount 0 -Attachments $SearchResult -BacklinkResults $SearchResult -ClusterType "SIMILAR" -MustIncludeSuggestions $QuerySuggestionList -QuerySuggestion $QuerySuggestion -Prominence "HERO" -AttachmentContext "MyAttachmentContext" -Pins $PinDocument

$RelatedDocuments = Initialize-RelatedDocuments -Relation "CASE" -AssociatedEntityId "MyAssociatedEntityId" -QuerySuggestion $QuerySuggestion -Documents $Document -Results $SearchResult

$PersonTeam = Initialize-PersonTeam -Id "MyId" -Name "MyName" -ExternalLink "MyExternalLink" -Relationship "MEMBER" -JoinDate (Get-Date)
$StructuredLocation = Initialize-StructuredLocation -DeskLocation "MyDeskLocation" -Timezone "MyTimezone" -Address "MyAddress" -City "MyCity" -State "MyState" -Region "MyRegion" -ZipCode "MyZipCode" -Country "MyCountry" -CountryCode "MyCountryCode"
$SocialNetwork = Initialize-SocialNetwork -Name "MyName" -ProfileName "MyProfileName" -ProfileUrl "MyProfileUrl"
$PersonDistance = Initialize-PersonDistance -Name "MyName" -ObfuscatedId "MyObfuscatedId" -Distance 0

$ChannelInviteInfo = Initialize-ChannelInviteInfo -Channel "COMMUNICATION_CHANNEL_EMAIL" -IsAutoInvite $false -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$InviteInfo = Initialize-InviteInfo -SignUpTime (Get-Date) -Invites $ChannelInviteInfo -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$Permissions = Initialize-Permissions -CanAdminSearch $false -CanAdminClientApiGlobalTokens $false -CanDlp $false -Read @{ key_example = $ReadPermission = Initialize-ReadPermission -ScopeType "GLOBAL" } -Write @{ key_example =  } -Grant @{ key_example = $GrantPermission = Initialize-GrantPermission -ScopeType "GLOBAL" } -Role "MyRole" -Roles "MyRoles"

$CustomFieldValue = Initialize-CustomFieldValue -StrText "MyStrText" -UrlAnchor "MyUrlAnchor" -UrlLink "MyUrlLink" -Person $Person

$CustomFieldData = Initialize-CustomFieldData -Label "MyLabel" -Values $CustomFieldValue -Displayable $false

$TimeInterval = Initialize-TimeInterval -Start "MyStart" -VarEnd "MyVarEnd"
$AnonymousEvent = Initialize-AnonymousEvent -Time $TimeInterval -EventType "DEFAULT"

$IconConfig = Initialize-IconConfig -GeneratedBackgroundColorKey "MyGeneratedBackgroundColorKey" -BackgroundColor "MyBackgroundColor" -Color "MyColor" -Key "MyKey" -IconType "COLLECTION" -Masked $false -Name "MyName" -Url "MyUrl"
$Badge = Initialize-Badge -Key "MyKey" -DisplayName "MyDisplayName" -IconConfig $IconConfig -Pinned $false

$PersonMetadata = Initialize-PersonMetadata -Type "FULL_TIME" -FirstName "MyFirstName" -LastName "MyLastName" -Title "MyTitle" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -Teams $PersonTeam -DepartmentCount 0 -Email "MyEmail" -AliasEmails "MyAliasEmails" -Location "MyLocation" -StructuredLocation $StructuredLocation -ExternalProfileLink "MyExternalProfileLink" -Manager $Person -ManagementChain $Person -Phone "MyPhone" -Timezone "MyTimezone" -TimezoneOffset 0 -PhotoUrl "MyPhotoUrl" -UneditedPhotoUrl "MyUneditedPhotoUrl" -BannerUrl "MyBannerUrl" -Reports $Person -StartDate (Get-Date) -EndDate (Get-Date) -Bio "MyBio" -Pronoun "MyPronoun" -OrgSizeCount 0 -DirectReportsCount 0 -PreferredName "MyPreferredName" -SocialNetwork $SocialNetwork -DatasourceProfile $DatasourceProfile -QuerySuggestions $QuerySuggestionList -PeopleDistance $PersonDistance -InviteInfo $InviteInfo -IsSignedUp $false -LastExtensionUse (Get-Date) -Permissions $Permissions -CustomFields $CustomFieldData -LoggingId "MyLoggingId" -StartDatePercentile 0 -BusyEvents $AnonymousEvent -ProfileBoolSettings @{ key_example = $false } -Badges $Badge -IsOrgRoot $false

$Person = Initialize-Person -Name "MyName" -ObfuscatedId "MyObfuscatedId" -RelatedDocuments $RelatedDocuments -Metadata $PersonMetadata

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$CreateAnnouncementRequest = Initialize-CreateAnnouncementRequest -StartTime (Get-Date) -EndTime (Get-Date) -Title "MyTitle" -Body $StructuredText -Emoji "MyEmoji" -Thumbnail $Thumbnail -Banner $Thumbnail -AudienceFilters $FacetFilter -SourceDocumentId "MySourceDocumentId" -HideAttribution $false -Channel "MAIN" -PostType "TEXT" -IsPrioritized $false -ViewUrl "MyViewUrl" # CreateAnnouncementRequest | Announcement content
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create Announcement
try {
    $Result = New-announcement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-announcement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateAnnouncementRequest**](CreateAnnouncementRequest.md)| Announcement content | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="New-draftannouncement"></a>
# **New-draftannouncement**
> Announcement New-draftannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create draft Announcement

Create a draft of a textual announcement visible to some set of users based on department and location.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Answer = Initialize-Answer -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -Permissions $ObjectPermissions -CombinedAnswerText $StructuredText -Likes $AnswerLikes -Author $Person -CreateTime (Get-Date) -UpdateTime (Get-Date) -UpdatedBy $Person -Verification $Verification -Board $AnswerBoard -Collections $Collection -DocumentCategory "MyDocumentCategory" -SourceDocument $Document

$ExtractedQnA = Initialize-ExtractedQnA -Heading "MyHeading" -Question "MyQuestion" -QuestionResult $SearchResult

$AppResult = Initialize-AppResult -Datasource "MyDatasource" -DocType "MyDocType" -MimeType "MyMimeType" -IconUrl "MyIconUrl"

$CodeLine = Initialize-CodeLine -LineNumber 0 -Content "MyContent" -Ranges $TextRange

$Code = Initialize-Code -RepoName "MyRepoName" -FileName "MyFileName" -FileUrl "MyFileUrl" -Lines $CodeLine -IsLastMatch $false

$QuerySuggestionList = Initialize-QuerySuggestionList -Suggestions $QuerySuggestion -Person $Person

$RelatedQuestion = Initialize-RelatedQuestion -Question "MyQuestion" -Answer "MyAnswer" -Ranges $TextRange

$SearchResultSnippet = Initialize-SearchResultSnippet -Snippet "MySnippet" -MimeType "MyMimeType" -Text "MyText" -SnippetTextOrdering 0 -Ranges $TextRange -Url "MyUrl"

$StructuredResult = Initialize-StructuredResult -Document $Document -Person $Person -Customer $Customer -Team $Team -CustomEntity $CustomEntity -Answer $Answer -ExtractedQnA $ExtractedQnA -App $AppResult -Collection $Collection -AnswerBoard $AnswerBoard -Code $Code -Shortcut $Shortcut -QuerySuggestions $QuerySuggestionList -RelatedDocuments $RelatedDocuments -RelatedQuestion $RelatedQuestion -Snippets $SearchResultSnippet -TrackingToken "MyTrackingToken" -Prominence "HERO" -Source "EXPERT_DETECTION"

$ClusterGroup = Initialize-ClusterGroup -ClusteredResults $SearchResult -ClusterType "SIMILAR" -VisibleCountHint 0

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$SearchResult = Initialize-SearchResult -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Document $Document -Title "MyTitle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -Snippets $SearchResultSnippet -ExpandedSnippets "MyExpandedSnippets" -FullText "MyFullText" -FullTextList "MyFullTextList" -RelatedResults $RelatedDocuments -ClusteredResults $SearchResult -AllClusteredResults $ClusterGroup -AttachmentCount 0 -Attachments $SearchResult -BacklinkResults $SearchResult -ClusterType "SIMILAR" -MustIncludeSuggestions $QuerySuggestionList -QuerySuggestion $QuerySuggestion -Prominence "HERO" -AttachmentContext "MyAttachmentContext" -Pins $PinDocument

$RelatedDocuments = Initialize-RelatedDocuments -Relation "CASE" -AssociatedEntityId "MyAssociatedEntityId" -QuerySuggestion $QuerySuggestion -Documents $Document -Results $SearchResult

$PersonTeam = Initialize-PersonTeam -Id "MyId" -Name "MyName" -ExternalLink "MyExternalLink" -Relationship "MEMBER" -JoinDate (Get-Date)
$StructuredLocation = Initialize-StructuredLocation -DeskLocation "MyDeskLocation" -Timezone "MyTimezone" -Address "MyAddress" -City "MyCity" -State "MyState" -Region "MyRegion" -ZipCode "MyZipCode" -Country "MyCountry" -CountryCode "MyCountryCode"
$SocialNetwork = Initialize-SocialNetwork -Name "MyName" -ProfileName "MyProfileName" -ProfileUrl "MyProfileUrl"
$PersonDistance = Initialize-PersonDistance -Name "MyName" -ObfuscatedId "MyObfuscatedId" -Distance 0

$ChannelInviteInfo = Initialize-ChannelInviteInfo -Channel "COMMUNICATION_CHANNEL_EMAIL" -IsAutoInvite $false -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$InviteInfo = Initialize-InviteInfo -SignUpTime (Get-Date) -Invites $ChannelInviteInfo -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$Permissions = Initialize-Permissions -CanAdminSearch $false -CanAdminClientApiGlobalTokens $false -CanDlp $false -Read @{ key_example = $ReadPermission = Initialize-ReadPermission -ScopeType "GLOBAL" } -Write @{ key_example =  } -Grant @{ key_example = $GrantPermission = Initialize-GrantPermission -ScopeType "GLOBAL" } -Role "MyRole" -Roles "MyRoles"

$CustomFieldValue = Initialize-CustomFieldValue -StrText "MyStrText" -UrlAnchor "MyUrlAnchor" -UrlLink "MyUrlLink" -Person $Person

$CustomFieldData = Initialize-CustomFieldData -Label "MyLabel" -Values $CustomFieldValue -Displayable $false

$TimeInterval = Initialize-TimeInterval -Start "MyStart" -VarEnd "MyVarEnd"
$AnonymousEvent = Initialize-AnonymousEvent -Time $TimeInterval -EventType "DEFAULT"

$IconConfig = Initialize-IconConfig -GeneratedBackgroundColorKey "MyGeneratedBackgroundColorKey" -BackgroundColor "MyBackgroundColor" -Color "MyColor" -Key "MyKey" -IconType "COLLECTION" -Masked $false -Name "MyName" -Url "MyUrl"
$Badge = Initialize-Badge -Key "MyKey" -DisplayName "MyDisplayName" -IconConfig $IconConfig -Pinned $false

$PersonMetadata = Initialize-PersonMetadata -Type "FULL_TIME" -FirstName "MyFirstName" -LastName "MyLastName" -Title "MyTitle" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -Teams $PersonTeam -DepartmentCount 0 -Email "MyEmail" -AliasEmails "MyAliasEmails" -Location "MyLocation" -StructuredLocation $StructuredLocation -ExternalProfileLink "MyExternalProfileLink" -Manager $Person -ManagementChain $Person -Phone "MyPhone" -Timezone "MyTimezone" -TimezoneOffset 0 -PhotoUrl "MyPhotoUrl" -UneditedPhotoUrl "MyUneditedPhotoUrl" -BannerUrl "MyBannerUrl" -Reports $Person -StartDate (Get-Date) -EndDate (Get-Date) -Bio "MyBio" -Pronoun "MyPronoun" -OrgSizeCount 0 -DirectReportsCount 0 -PreferredName "MyPreferredName" -SocialNetwork $SocialNetwork -DatasourceProfile $DatasourceProfile -QuerySuggestions $QuerySuggestionList -PeopleDistance $PersonDistance -InviteInfo $InviteInfo -IsSignedUp $false -LastExtensionUse (Get-Date) -Permissions $Permissions -CustomFields $CustomFieldData -LoggingId "MyLoggingId" -StartDatePercentile 0 -BusyEvents $AnonymousEvent -ProfileBoolSettings @{ key_example = $false } -Badges $Badge -IsOrgRoot $false

$Person = Initialize-Person -Name "MyName" -ObfuscatedId "MyObfuscatedId" -RelatedDocuments $RelatedDocuments -Metadata $PersonMetadata

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$CreateDraftAnnouncementRequest = Initialize-CreateDraftAnnouncementRequest -StartTime (Get-Date) -EndTime (Get-Date) -Title "MyTitle" -Body $StructuredText -Emoji "MyEmoji" -Thumbnail $Thumbnail -Banner $Thumbnail -AudienceFilters $FacetFilter -SourceDocumentId "MySourceDocumentId" -HideAttribution $false -Channel "MAIN" -PostType "TEXT" -IsPrioritized $false -ViewUrl "MyViewUrl" -Id 0 # CreateDraftAnnouncementRequest | Draft announcement content
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create draft Announcement
try {
    $Result = New-draftannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-draftannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateDraftAnnouncementRequest**](CreateDraftAnnouncementRequest.md)| Draft announcement content | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deleteannouncement"></a>
# **Invoke-Deleteannouncement**
> void Invoke-Deleteannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete Announcement

Delete an existing user-generated announcement.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteAnnouncementRequest = Initialize-DeleteAnnouncementRequest -Id 0 # DeleteAnnouncementRequest | Delete announcement request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete Announcement
try {
    $Result = Invoke-Deleteannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deleteannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteAnnouncementRequest**](DeleteAnnouncementRequest.md)| Delete announcement request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deletedraftannouncement"></a>
# **Invoke-Deletedraftannouncement**
> void Invoke-Deletedraftannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete draft Announcement

Delete an existing user-generated draft Announcement.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteAnnouncementRequest = Initialize-DeleteAnnouncementRequest -Id 0 # DeleteAnnouncementRequest | Delete draft announcement request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete draft Announcement
try {
    $Result = Invoke-Deletedraftannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deletedraftannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteAnnouncementRequest**](DeleteAnnouncementRequest.md)| Delete draft announcement request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-announcement"></a>
# **Get-announcement**
> GetAnnouncementResponse Get-announcement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read Announcement

Read the details of an Announcement given its ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetAnnouncementRequest = Initialize-GetAnnouncementRequest -Id 0 # GetAnnouncementRequest | GetAnnouncement request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read Announcement
try {
    $Result = Get-announcement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-announcement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetAnnouncementRequest**](GetAnnouncementRequest.md)| GetAnnouncement request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetAnnouncementResponse**](GetAnnouncementResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-draftannouncement"></a>
# **Get-draftannouncement**
> GetDraftAnnouncementResponse Get-draftannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read draft Announcement

Read the details of an existing user-generated draft Announcement.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetAnnouncementRequest = Initialize-GetAnnouncementRequest -Id 0 # GetAnnouncementRequest | Get draft announcement request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read draft Announcement
try {
    $Result = Get-draftannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-draftannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetAnnouncementRequest**](GetAnnouncementRequest.md)| Get draft announcement request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDraftAnnouncementResponse**](GetDraftAnnouncementResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listannouncements"></a>
# **Invoke-Listannouncements**
> ListAnnouncementsResponse Invoke-Listannouncements<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List Announcements

List Announcement details for all Announcements matching the given criteria.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ListAnnouncementsRequest = Initialize-ListAnnouncementsRequest -Channel "MAIN" # ListAnnouncementsRequest | Includes request params for querying announcements.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List Announcements
try {
    $Result = Invoke-Listannouncements -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listannouncements: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ListAnnouncementsRequest**](ListAnnouncementsRequest.md)| Includes request params for querying announcements. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListAnnouncementsResponse**](ListAnnouncementsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Previewannouncement"></a>
# **Invoke-Previewannouncement**
> PreviewStructuredTextResponse Invoke-Previewannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Preview Announcement

Generate a preview for a user-generated Announcement from structured text.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$PreviewStructuredTextRequest = Initialize-PreviewStructuredTextRequest -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." # PreviewStructuredTextRequest | preview structured text request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Preview Announcement
try {
    $Result = Invoke-Previewannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Previewannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PreviewStructuredTextRequest**](PreviewStructuredTextRequest.md)| preview structured text request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewStructuredTextResponse**](PreviewStructuredTextResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Previewannouncementdraft"></a>
# **Invoke-Previewannouncementdraft**
> PreviewUgcResponse Invoke-Previewannouncementdraft<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Preview draft Announcement

Generates a preview for a user-generated Announcement from a draft.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Answer = Initialize-Answer -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -Permissions $ObjectPermissions -CombinedAnswerText $StructuredText -Likes $AnswerLikes -Author $Person -CreateTime (Get-Date) -UpdateTime (Get-Date) -UpdatedBy $Person -Verification $Verification -Board $AnswerBoard -Collections $Collection -DocumentCategory "MyDocumentCategory" -SourceDocument $Document

$ExtractedQnA = Initialize-ExtractedQnA -Heading "MyHeading" -Question "MyQuestion" -QuestionResult $SearchResult

$AppResult = Initialize-AppResult -Datasource "MyDatasource" -DocType "MyDocType" -MimeType "MyMimeType" -IconUrl "MyIconUrl"

$CodeLine = Initialize-CodeLine -LineNumber 0 -Content "MyContent" -Ranges $TextRange

$Code = Initialize-Code -RepoName "MyRepoName" -FileName "MyFileName" -FileUrl "MyFileUrl" -Lines $CodeLine -IsLastMatch $false

$QuerySuggestionList = Initialize-QuerySuggestionList -Suggestions $QuerySuggestion -Person $Person

$RelatedQuestion = Initialize-RelatedQuestion -Question "MyQuestion" -Answer "MyAnswer" -Ranges $TextRange

$SearchResultSnippet = Initialize-SearchResultSnippet -Snippet "MySnippet" -MimeType "MyMimeType" -Text "MyText" -SnippetTextOrdering 0 -Ranges $TextRange -Url "MyUrl"

$StructuredResult = Initialize-StructuredResult -Document $Document -Person $Person -Customer $Customer -Team $Team -CustomEntity $CustomEntity -Answer $Answer -ExtractedQnA $ExtractedQnA -App $AppResult -Collection $Collection -AnswerBoard $AnswerBoard -Code $Code -Shortcut $Shortcut -QuerySuggestions $QuerySuggestionList -RelatedDocuments $RelatedDocuments -RelatedQuestion $RelatedQuestion -Snippets $SearchResultSnippet -TrackingToken "MyTrackingToken" -Prominence "HERO" -Source "EXPERT_DETECTION"

$ClusterGroup = Initialize-ClusterGroup -ClusteredResults $SearchResult -ClusterType "SIMILAR" -VisibleCountHint 0

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$SearchResult = Initialize-SearchResult -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Document $Document -Title "MyTitle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -Snippets $SearchResultSnippet -ExpandedSnippets "MyExpandedSnippets" -FullText "MyFullText" -FullTextList "MyFullTextList" -RelatedResults $RelatedDocuments -ClusteredResults $SearchResult -AllClusteredResults $ClusterGroup -AttachmentCount 0 -Attachments $SearchResult -BacklinkResults $SearchResult -ClusterType "SIMILAR" -MustIncludeSuggestions $QuerySuggestionList -QuerySuggestion $QuerySuggestion -Prominence "HERO" -AttachmentContext "MyAttachmentContext" -Pins $PinDocument

$RelatedDocuments = Initialize-RelatedDocuments -Relation "CASE" -AssociatedEntityId "MyAssociatedEntityId" -QuerySuggestion $QuerySuggestion -Documents $Document -Results $SearchResult

$PersonTeam = Initialize-PersonTeam -Id "MyId" -Name "MyName" -ExternalLink "MyExternalLink" -Relationship "MEMBER" -JoinDate (Get-Date)
$StructuredLocation = Initialize-StructuredLocation -DeskLocation "MyDeskLocation" -Timezone "MyTimezone" -Address "MyAddress" -City "MyCity" -State "MyState" -Region "MyRegion" -ZipCode "MyZipCode" -Country "MyCountry" -CountryCode "MyCountryCode"
$SocialNetwork = Initialize-SocialNetwork -Name "MyName" -ProfileName "MyProfileName" -ProfileUrl "MyProfileUrl"
$PersonDistance = Initialize-PersonDistance -Name "MyName" -ObfuscatedId "MyObfuscatedId" -Distance 0

$ChannelInviteInfo = Initialize-ChannelInviteInfo -Channel "COMMUNICATION_CHANNEL_EMAIL" -IsAutoInvite $false -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$InviteInfo = Initialize-InviteInfo -SignUpTime (Get-Date) -Invites $ChannelInviteInfo -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$Permissions = Initialize-Permissions -CanAdminSearch $false -CanAdminClientApiGlobalTokens $false -CanDlp $false -Read @{ key_example = $ReadPermission = Initialize-ReadPermission -ScopeType "GLOBAL" } -Write @{ key_example =  } -Grant @{ key_example = $GrantPermission = Initialize-GrantPermission -ScopeType "GLOBAL" } -Role "MyRole" -Roles "MyRoles"

$CustomFieldValue = Initialize-CustomFieldValue -StrText "MyStrText" -UrlAnchor "MyUrlAnchor" -UrlLink "MyUrlLink" -Person $Person

$CustomFieldData = Initialize-CustomFieldData -Label "MyLabel" -Values $CustomFieldValue -Displayable $false

$TimeInterval = Initialize-TimeInterval -Start "MyStart" -VarEnd "MyVarEnd"
$AnonymousEvent = Initialize-AnonymousEvent -Time $TimeInterval -EventType "DEFAULT"

$IconConfig = Initialize-IconConfig -GeneratedBackgroundColorKey "MyGeneratedBackgroundColorKey" -BackgroundColor "MyBackgroundColor" -Color "MyColor" -Key "MyKey" -IconType "COLLECTION" -Masked $false -Name "MyName" -Url "MyUrl"
$Badge = Initialize-Badge -Key "MyKey" -DisplayName "MyDisplayName" -IconConfig $IconConfig -Pinned $false

$PersonMetadata = Initialize-PersonMetadata -Type "FULL_TIME" -FirstName "MyFirstName" -LastName "MyLastName" -Title "MyTitle" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -Teams $PersonTeam -DepartmentCount 0 -Email "MyEmail" -AliasEmails "MyAliasEmails" -Location "MyLocation" -StructuredLocation $StructuredLocation -ExternalProfileLink "MyExternalProfileLink" -Manager $Person -ManagementChain $Person -Phone "MyPhone" -Timezone "MyTimezone" -TimezoneOffset 0 -PhotoUrl "MyPhotoUrl" -UneditedPhotoUrl "MyUneditedPhotoUrl" -BannerUrl "MyBannerUrl" -Reports $Person -StartDate (Get-Date) -EndDate (Get-Date) -Bio "MyBio" -Pronoun "MyPronoun" -OrgSizeCount 0 -DirectReportsCount 0 -PreferredName "MyPreferredName" -SocialNetwork $SocialNetwork -DatasourceProfile $DatasourceProfile -QuerySuggestions $QuerySuggestionList -PeopleDistance $PersonDistance -InviteInfo $InviteInfo -IsSignedUp $false -LastExtensionUse (Get-Date) -Permissions $Permissions -CustomFields $CustomFieldData -LoggingId "MyLoggingId" -StartDatePercentile 0 -BusyEvents $AnonymousEvent -ProfileBoolSettings @{ key_example = $false } -Badges $Badge -IsOrgRoot $false

$Person = Initialize-Person -Name "MyName" -ObfuscatedId "MyObfuscatedId" -RelatedDocuments $RelatedDocuments -Metadata $PersonMetadata

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$AnnouncementMutableProperties = Initialize-AnnouncementMutableProperties -StartTime (Get-Date) -EndTime (Get-Date) -Title "MyTitle" -Body $StructuredText -Emoji "MyEmoji" -Thumbnail $Thumbnail -Banner $Thumbnail -AudienceFilters $FacetFilter -SourceDocumentId "MySourceDocumentId" -HideAttribution $false -Channel "MAIN" -PostType "TEXT" -IsPrioritized $false -ViewUrl "MyViewUrl"

$AnswerMutableProperties = Initialize-AnswerMutableProperties -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT"

$UgcDraft = Initialize-UgcDraft -Announcement $AnnouncementMutableProperties -Answer $AnswerMutableProperties

$PreviewUgcRequest = Initialize-PreviewUgcRequest -Draft $UgcDraft -DraftSpec $DocumentSpec -Type "ANNOUNCEMENTS_TYPE" # PreviewUgcRequest | preview announcement request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Preview draft Announcement
try {
    $Result = Invoke-Previewannouncementdraft -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Previewannouncementdraft: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PreviewUgcRequest**](PreviewUgcRequest.md)| preview announcement request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewUgcResponse**](PreviewUgcResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Publish-draftannouncement"></a>
# **Publish-draftannouncement**
> void Publish-draftannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Publish draft Announcement

Promote a draft Announcement to be visible to others.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$PublishDraftAnnouncementRequest = Initialize-PublishDraftAnnouncementRequest -Id 0 # PublishDraftAnnouncementRequest | Publish draft announcement content.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Publish draft Announcement
try {
    $Result = Publish-draftannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Publish-draftannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PublishDraftAnnouncementRequest**](PublishDraftAnnouncementRequest.md)| Publish draft announcement content. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Unpublish-announcement"></a>
# **Unpublish-announcement**
> Announcement Unpublish-announcement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Unpublish Announcement

Unpublish an Announcement to hide it from users.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$UnpublishAnnouncementRequest = Initialize-UnpublishAnnouncementRequest -Id 0 # UnpublishAnnouncementRequest | Unpublish announcement content.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Unpublish Announcement
try {
    $Result = Unpublish-announcement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Unpublish-announcement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**UnpublishAnnouncementRequest**](UnpublishAnnouncementRequest.md)| Unpublish announcement content. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Update-announcement"></a>
# **Update-announcement**
> Announcement Update-announcement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Announcement

Update a textual announcement visible to some set of users based on department and location.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Answer = Initialize-Answer -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -Permissions $ObjectPermissions -CombinedAnswerText $StructuredText -Likes $AnswerLikes -Author $Person -CreateTime (Get-Date) -UpdateTime (Get-Date) -UpdatedBy $Person -Verification $Verification -Board $AnswerBoard -Collections $Collection -DocumentCategory "MyDocumentCategory" -SourceDocument $Document

$ExtractedQnA = Initialize-ExtractedQnA -Heading "MyHeading" -Question "MyQuestion" -QuestionResult $SearchResult

$AppResult = Initialize-AppResult -Datasource "MyDatasource" -DocType "MyDocType" -MimeType "MyMimeType" -IconUrl "MyIconUrl"

$CodeLine = Initialize-CodeLine -LineNumber 0 -Content "MyContent" -Ranges $TextRange

$Code = Initialize-Code -RepoName "MyRepoName" -FileName "MyFileName" -FileUrl "MyFileUrl" -Lines $CodeLine -IsLastMatch $false

$QuerySuggestionList = Initialize-QuerySuggestionList -Suggestions $QuerySuggestion -Person $Person

$RelatedQuestion = Initialize-RelatedQuestion -Question "MyQuestion" -Answer "MyAnswer" -Ranges $TextRange

$SearchResultSnippet = Initialize-SearchResultSnippet -Snippet "MySnippet" -MimeType "MyMimeType" -Text "MyText" -SnippetTextOrdering 0 -Ranges $TextRange -Url "MyUrl"

$StructuredResult = Initialize-StructuredResult -Document $Document -Person $Person -Customer $Customer -Team $Team -CustomEntity $CustomEntity -Answer $Answer -ExtractedQnA $ExtractedQnA -App $AppResult -Collection $Collection -AnswerBoard $AnswerBoard -Code $Code -Shortcut $Shortcut -QuerySuggestions $QuerySuggestionList -RelatedDocuments $RelatedDocuments -RelatedQuestion $RelatedQuestion -Snippets $SearchResultSnippet -TrackingToken "MyTrackingToken" -Prominence "HERO" -Source "EXPERT_DETECTION"

$ClusterGroup = Initialize-ClusterGroup -ClusteredResults $SearchResult -ClusterType "SIMILAR" -VisibleCountHint 0

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$SearchResult = Initialize-SearchResult -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Document $Document -Title "MyTitle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -Snippets $SearchResultSnippet -ExpandedSnippets "MyExpandedSnippets" -FullText "MyFullText" -FullTextList "MyFullTextList" -RelatedResults $RelatedDocuments -ClusteredResults $SearchResult -AllClusteredResults $ClusterGroup -AttachmentCount 0 -Attachments $SearchResult -BacklinkResults $SearchResult -ClusterType "SIMILAR" -MustIncludeSuggestions $QuerySuggestionList -QuerySuggestion $QuerySuggestion -Prominence "HERO" -AttachmentContext "MyAttachmentContext" -Pins $PinDocument

$RelatedDocuments = Initialize-RelatedDocuments -Relation "CASE" -AssociatedEntityId "MyAssociatedEntityId" -QuerySuggestion $QuerySuggestion -Documents $Document -Results $SearchResult

$PersonTeam = Initialize-PersonTeam -Id "MyId" -Name "MyName" -ExternalLink "MyExternalLink" -Relationship "MEMBER" -JoinDate (Get-Date)
$StructuredLocation = Initialize-StructuredLocation -DeskLocation "MyDeskLocation" -Timezone "MyTimezone" -Address "MyAddress" -City "MyCity" -State "MyState" -Region "MyRegion" -ZipCode "MyZipCode" -Country "MyCountry" -CountryCode "MyCountryCode"
$SocialNetwork = Initialize-SocialNetwork -Name "MyName" -ProfileName "MyProfileName" -ProfileUrl "MyProfileUrl"
$PersonDistance = Initialize-PersonDistance -Name "MyName" -ObfuscatedId "MyObfuscatedId" -Distance 0

$ChannelInviteInfo = Initialize-ChannelInviteInfo -Channel "COMMUNICATION_CHANNEL_EMAIL" -IsAutoInvite $false -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$InviteInfo = Initialize-InviteInfo -SignUpTime (Get-Date) -Invites $ChannelInviteInfo -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$Permissions = Initialize-Permissions -CanAdminSearch $false -CanAdminClientApiGlobalTokens $false -CanDlp $false -Read @{ key_example = $ReadPermission = Initialize-ReadPermission -ScopeType "GLOBAL" } -Write @{ key_example =  } -Grant @{ key_example = $GrantPermission = Initialize-GrantPermission -ScopeType "GLOBAL" } -Role "MyRole" -Roles "MyRoles"

$CustomFieldValue = Initialize-CustomFieldValue -StrText "MyStrText" -UrlAnchor "MyUrlAnchor" -UrlLink "MyUrlLink" -Person $Person

$CustomFieldData = Initialize-CustomFieldData -Label "MyLabel" -Values $CustomFieldValue -Displayable $false

$TimeInterval = Initialize-TimeInterval -Start "MyStart" -VarEnd "MyVarEnd"
$AnonymousEvent = Initialize-AnonymousEvent -Time $TimeInterval -EventType "DEFAULT"

$IconConfig = Initialize-IconConfig -GeneratedBackgroundColorKey "MyGeneratedBackgroundColorKey" -BackgroundColor "MyBackgroundColor" -Color "MyColor" -Key "MyKey" -IconType "COLLECTION" -Masked $false -Name "MyName" -Url "MyUrl"
$Badge = Initialize-Badge -Key "MyKey" -DisplayName "MyDisplayName" -IconConfig $IconConfig -Pinned $false

$PersonMetadata = Initialize-PersonMetadata -Type "FULL_TIME" -FirstName "MyFirstName" -LastName "MyLastName" -Title "MyTitle" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -Teams $PersonTeam -DepartmentCount 0 -Email "MyEmail" -AliasEmails "MyAliasEmails" -Location "MyLocation" -StructuredLocation $StructuredLocation -ExternalProfileLink "MyExternalProfileLink" -Manager $Person -ManagementChain $Person -Phone "MyPhone" -Timezone "MyTimezone" -TimezoneOffset 0 -PhotoUrl "MyPhotoUrl" -UneditedPhotoUrl "MyUneditedPhotoUrl" -BannerUrl "MyBannerUrl" -Reports $Person -StartDate (Get-Date) -EndDate (Get-Date) -Bio "MyBio" -Pronoun "MyPronoun" -OrgSizeCount 0 -DirectReportsCount 0 -PreferredName "MyPreferredName" -SocialNetwork $SocialNetwork -DatasourceProfile $DatasourceProfile -QuerySuggestions $QuerySuggestionList -PeopleDistance $PersonDistance -InviteInfo $InviteInfo -IsSignedUp $false -LastExtensionUse (Get-Date) -Permissions $Permissions -CustomFields $CustomFieldData -LoggingId "MyLoggingId" -StartDatePercentile 0 -BusyEvents $AnonymousEvent -ProfileBoolSettings @{ key_example = $false } -Badges $Badge -IsOrgRoot $false

$Person = Initialize-Person -Name "MyName" -ObfuscatedId "MyObfuscatedId" -RelatedDocuments $RelatedDocuments -Metadata $PersonMetadata

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$UpdateAnnouncementRequest = Initialize-UpdateAnnouncementRequest -StartTime (Get-Date) -EndTime (Get-Date) -Title "MyTitle" -Body $StructuredText -Emoji "MyEmoji" -Thumbnail $Thumbnail -Banner $Thumbnail -AudienceFilters $FacetFilter -SourceDocumentId "MySourceDocumentId" -HideAttribution $false -Channel "MAIN" -PostType "TEXT" -IsPrioritized $false -ViewUrl "MyViewUrl" -Id 0 # UpdateAnnouncementRequest | Announcement content. Id need to be specified for the announcement.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Announcement
try {
    $Result = Update-announcement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Update-announcement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**UpdateAnnouncementRequest**](UpdateAnnouncementRequest.md)| Announcement content. Id need to be specified for the announcement. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Update-draftannouncement"></a>
# **Update-draftannouncement**
> Announcement Update-draftannouncement<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update draft Announcement

Update a textual Announcement visible to some set of users based on department and location.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Answer = Initialize-Answer -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -Permissions $ObjectPermissions -CombinedAnswerText $StructuredText -Likes $AnswerLikes -Author $Person -CreateTime (Get-Date) -UpdateTime (Get-Date) -UpdatedBy $Person -Verification $Verification -Board $AnswerBoard -Collections $Collection -DocumentCategory "MyDocumentCategory" -SourceDocument $Document

$ExtractedQnA = Initialize-ExtractedQnA -Heading "MyHeading" -Question "MyQuestion" -QuestionResult $SearchResult

$AppResult = Initialize-AppResult -Datasource "MyDatasource" -DocType "MyDocType" -MimeType "MyMimeType" -IconUrl "MyIconUrl"

$CodeLine = Initialize-CodeLine -LineNumber 0 -Content "MyContent" -Ranges $TextRange

$Code = Initialize-Code -RepoName "MyRepoName" -FileName "MyFileName" -FileUrl "MyFileUrl" -Lines $CodeLine -IsLastMatch $false

$QuerySuggestionList = Initialize-QuerySuggestionList -Suggestions $QuerySuggestion -Person $Person

$RelatedQuestion = Initialize-RelatedQuestion -Question "MyQuestion" -Answer "MyAnswer" -Ranges $TextRange

$SearchResultSnippet = Initialize-SearchResultSnippet -Snippet "MySnippet" -MimeType "MyMimeType" -Text "MyText" -SnippetTextOrdering 0 -Ranges $TextRange -Url "MyUrl"

$StructuredResult = Initialize-StructuredResult -Document $Document -Person $Person -Customer $Customer -Team $Team -CustomEntity $CustomEntity -Answer $Answer -ExtractedQnA $ExtractedQnA -App $AppResult -Collection $Collection -AnswerBoard $AnswerBoard -Code $Code -Shortcut $Shortcut -QuerySuggestions $QuerySuggestionList -RelatedDocuments $RelatedDocuments -RelatedQuestion $RelatedQuestion -Snippets $SearchResultSnippet -TrackingToken "MyTrackingToken" -Prominence "HERO" -Source "EXPERT_DETECTION"

$ClusterGroup = Initialize-ClusterGroup -ClusteredResults $SearchResult -ClusterType "SIMILAR" -VisibleCountHint 0

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$SearchResult = Initialize-SearchResult -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Document $Document -Title "MyTitle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -Snippets $SearchResultSnippet -ExpandedSnippets "MyExpandedSnippets" -FullText "MyFullText" -FullTextList "MyFullTextList" -RelatedResults $RelatedDocuments -ClusteredResults $SearchResult -AllClusteredResults $ClusterGroup -AttachmentCount 0 -Attachments $SearchResult -BacklinkResults $SearchResult -ClusterType "SIMILAR" -MustIncludeSuggestions $QuerySuggestionList -QuerySuggestion $QuerySuggestion -Prominence "HERO" -AttachmentContext "MyAttachmentContext" -Pins $PinDocument

$RelatedDocuments = Initialize-RelatedDocuments -Relation "CASE" -AssociatedEntityId "MyAssociatedEntityId" -QuerySuggestion $QuerySuggestion -Documents $Document -Results $SearchResult

$PersonTeam = Initialize-PersonTeam -Id "MyId" -Name "MyName" -ExternalLink "MyExternalLink" -Relationship "MEMBER" -JoinDate (Get-Date)
$StructuredLocation = Initialize-StructuredLocation -DeskLocation "MyDeskLocation" -Timezone "MyTimezone" -Address "MyAddress" -City "MyCity" -State "MyState" -Region "MyRegion" -ZipCode "MyZipCode" -Country "MyCountry" -CountryCode "MyCountryCode"
$SocialNetwork = Initialize-SocialNetwork -Name "MyName" -ProfileName "MyProfileName" -ProfileUrl "MyProfileUrl"
$PersonDistance = Initialize-PersonDistance -Name "MyName" -ObfuscatedId "MyObfuscatedId" -Distance 0

$ChannelInviteInfo = Initialize-ChannelInviteInfo -Channel "COMMUNICATION_CHANNEL_EMAIL" -IsAutoInvite $false -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$InviteInfo = Initialize-InviteInfo -SignUpTime (Get-Date) -Invites $ChannelInviteInfo -Inviter $Person -InviteTime (Get-Date) -ReminderTime (Get-Date)

$Permissions = Initialize-Permissions -CanAdminSearch $false -CanAdminClientApiGlobalTokens $false -CanDlp $false -Read @{ key_example = $ReadPermission = Initialize-ReadPermission -ScopeType "GLOBAL" } -Write @{ key_example =  } -Grant @{ key_example = $GrantPermission = Initialize-GrantPermission -ScopeType "GLOBAL" } -Role "MyRole" -Roles "MyRoles"

$CustomFieldValue = Initialize-CustomFieldValue -StrText "MyStrText" -UrlAnchor "MyUrlAnchor" -UrlLink "MyUrlLink" -Person $Person

$CustomFieldData = Initialize-CustomFieldData -Label "MyLabel" -Values $CustomFieldValue -Displayable $false

$TimeInterval = Initialize-TimeInterval -Start "MyStart" -VarEnd "MyVarEnd"
$AnonymousEvent = Initialize-AnonymousEvent -Time $TimeInterval -EventType "DEFAULT"

$IconConfig = Initialize-IconConfig -GeneratedBackgroundColorKey "MyGeneratedBackgroundColorKey" -BackgroundColor "MyBackgroundColor" -Color "MyColor" -Key "MyKey" -IconType "COLLECTION" -Masked $false -Name "MyName" -Url "MyUrl"
$Badge = Initialize-Badge -Key "MyKey" -DisplayName "MyDisplayName" -IconConfig $IconConfig -Pinned $false

$PersonMetadata = Initialize-PersonMetadata -Type "FULL_TIME" -FirstName "MyFirstName" -LastName "MyLastName" -Title "MyTitle" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -Teams $PersonTeam -DepartmentCount 0 -Email "MyEmail" -AliasEmails "MyAliasEmails" -Location "MyLocation" -StructuredLocation $StructuredLocation -ExternalProfileLink "MyExternalProfileLink" -Manager $Person -ManagementChain $Person -Phone "MyPhone" -Timezone "MyTimezone" -TimezoneOffset 0 -PhotoUrl "MyPhotoUrl" -UneditedPhotoUrl "MyUneditedPhotoUrl" -BannerUrl "MyBannerUrl" -Reports $Person -StartDate (Get-Date) -EndDate (Get-Date) -Bio "MyBio" -Pronoun "MyPronoun" -OrgSizeCount 0 -DirectReportsCount 0 -PreferredName "MyPreferredName" -SocialNetwork $SocialNetwork -DatasourceProfile $DatasourceProfile -QuerySuggestions $QuerySuggestionList -PeopleDistance $PersonDistance -InviteInfo $InviteInfo -IsSignedUp $false -LastExtensionUse (Get-Date) -Permissions $Permissions -CustomFields $CustomFieldData -LoggingId "MyLoggingId" -StartDatePercentile 0 -BusyEvents $AnonymousEvent -ProfileBoolSettings @{ key_example = $false } -Badges $Badge -IsOrgRoot $false

$Person = Initialize-Person -Name "MyName" -ObfuscatedId "MyObfuscatedId" -RelatedDocuments $RelatedDocuments -Metadata $PersonMetadata

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$UpdateDraftAnnouncementRequest = Initialize-UpdateDraftAnnouncementRequest -StartTime (Get-Date) -EndTime (Get-Date) -Title "MyTitle" -Body $StructuredText -Emoji "MyEmoji" -Thumbnail $Thumbnail -Banner $Thumbnail -AudienceFilters $FacetFilter -SourceDocumentId "MySourceDocumentId" -HideAttribution $false -Channel "MAIN" -PostType "TEXT" -IsPrioritized $false -ViewUrl "MyViewUrl" -Id 0 -DraftId 0 # UpdateDraftAnnouncementRequest | Draft announcement content. DraftId needs to be specified.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update draft Announcement
try {
    $Result = Update-draftannouncement -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Update-draftannouncement: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**UpdateDraftAnnouncementRequest**](UpdateDraftAnnouncementRequest.md)| Draft announcement content. DraftId needs to be specified. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

