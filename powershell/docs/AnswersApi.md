# PSOpenAPITools.PSOpenAPITools\Api.AnswersApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**New-answer**](AnswersApi.md#New-answer) | **POST** /createanswer | Create Answer
[**New-answerboard**](AnswersApi.md#New-answerboard) | **POST** /createanswerboard | Create Answer Board
[**Invoke-Deleteanswer**](AnswersApi.md#Invoke-Deleteanswer) | **POST** /deleteanswer | Delete Answer
[**Invoke-Deleteanswerboards**](AnswersApi.md#Invoke-Deleteanswerboards) | **POST** /deleteanswerboards | Delete Answer Board
[**Edit-answer**](AnswersApi.md#Edit-answer) | **POST** /editanswer | Update Answer
[**Edit-answerboard**](AnswersApi.md#Edit-answerboard) | **POST** /editanswerboard | Update Answer Board
[**Get-answer**](AnswersApi.md#Get-answer) | **POST** /getanswer | Read Answer
[**Get-answerboard**](AnswersApi.md#Get-answerboard) | **POST** /getanswerboard | Read Answer Board
[**Invoke-Listanswerboards**](AnswersApi.md#Invoke-Listanswerboards) | **POST** /listanswerboards | List Answer Boards
[**Invoke-Listanswers**](AnswersApi.md#Invoke-Listanswers) | **POST** /listanswers | List Answers
[**Invoke-Previewanswer**](AnswersApi.md#Invoke-Previewanswer) | **POST** /previewanswer | Preview Answer
[**Invoke-Previewanswerdraft**](AnswersApi.md#Invoke-Previewanswerdraft) | **POST** /previewanswerdraft | Preview draft Answer
[**Update-answerlikes**](AnswersApi.md#Update-answerlikes) | **POST** /updateanswerlikes | Update Answer likes


<a id="New-answer"></a>
# **New-answer**
> Answer New-answer<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create Answer

Create a user-generated Answer that contains a question and answer.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

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

$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$StructuredTextMutableProperties = Initialize-StructuredTextMutableProperties -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light."
$AnswerCreationData = Initialize-AnswerCreationData -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -AddedCollections 0 -CombinedAnswerText $StructuredTextMutableProperties

$CreateAnswerRequest = Initialize-CreateAnswerRequest -VarData $AnswerCreationData # CreateAnswerRequest | CreateAnswer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create Answer
try {
    $Result = New-answer -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-answer: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateAnswerRequest**](CreateAnswerRequest.md)| CreateAnswer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Answer**](Answer.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="New-answerboard"></a>
# **New-answerboard**
> CreateAnswerBoardResponse New-answerboard<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create Answer Board

Create a board of Answers.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"

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

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

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

$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$CreateAnswerBoardRequest = Initialize-CreateAnswerBoardRequest -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter # CreateAnswerBoardRequest | Answer Board content plus any additional metadata for the request.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create Answer Board
try {
    $Result = New-answerboard -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-answerboard: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateAnswerBoardRequest**](CreateAnswerBoardRequest.md)| Answer Board content plus any additional metadata for the request. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateAnswerBoardResponse**](CreateAnswerBoardResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deleteanswer"></a>
# **Invoke-Deleteanswer**
> void Invoke-Deleteanswer<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete Answer

Delete an existing user-generated Answer.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteAnswerRequest = Initialize-DeleteAnswerRequest -Id 3 -DocId "ANSWERS_answer_3" # DeleteAnswerRequest | DeleteAnswer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete Answer
try {
    $Result = Invoke-Deleteanswer -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deleteanswer: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteAnswerRequest**](DeleteAnswerRequest.md)| DeleteAnswer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deleteanswerboards"></a>
# **Invoke-Deleteanswerboards**
> DeleteAnswerBoardsResponse Invoke-Deleteanswerboards<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete Answer Board

Delete an Answer Board given the Answer Board's ID. Multi-delete is not currently supported.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteAnswerBoardsRequest = Initialize-DeleteAnswerBoardsRequest -Ids 0 # DeleteAnswerBoardsRequest | DeleteAnswerBoards request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete Answer Board
try {
    $Result = Invoke-Deleteanswerboards -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deleteanswerboards: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteAnswerBoardsRequest**](DeleteAnswerBoardsRequest.md)| DeleteAnswerBoards request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**DeleteAnswerBoardsResponse**](DeleteAnswerBoardsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Edit-answer"></a>
# **Edit-answer**
> Answer Edit-answer<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Answer

Update an existing user-generated Answer.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS"$SearchRequestOptions = Initialize-SearchRequestOptions -DatasourceFilter "MyDatasourceFilter" -DatasourcesFilter "MyDatasourcesFilter" -QueryOverridesFacetFilters $false -FacetFilters $FacetFilter -FacetFilterSets $FacetFilterSet -FacetBucketFilter $FacetBucketFilter -FacetBucketSize 0 -DefaultFacets "MyDefaultFacets" -AuthTokens $AuthToken -FetchAllDatasourceCounts $false -ResponseHints 

$FacetFilterSet = Initialize-FacetFilterSet -Filters $FacetFilter

$FacetBucketFilter = Initialize-FacetBucketFilter -Facet "MyFacet" -Prefix "MyPrefix"
$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
"RESULTS" -TimezoneOffset 0 -ForceNegation $false -DisableSpellcheck $false -DisableQueryAutocorrect $false -ReturnLlmContentOverSnippets $false

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

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

$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$StructuredTextMutableProperties = Initialize-StructuredTextMutableProperties -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light."
$EditAnswerRequest = Initialize-EditAnswerRequest -Id 3 -DocId "ANSWERS_answer_3" -Question "Why is the sky blue?" -QuestionVariations "MyQuestionVariations" -BodyText "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -BoardId 0 -AudienceFilters $FacetFilter -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Roles $UserRoleSpecification -SourceDocumentSpec $DocumentSpec -SourceType "DOCUMENT" -AddedCollections 0 -RemovedCollections 0 -CombinedAnswerText $StructuredTextMutableProperties # EditAnswerRequest | EditAnswer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Answer
try {
    $Result = Edit-answer -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-answer: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditAnswerRequest**](EditAnswerRequest.md)| EditAnswer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Answer**](Answer.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Edit-answerboard"></a>
# **Edit-answerboard**
> EditAnswerBoardResponse Edit-answerboard<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Answer Board

Modifies the properties of an existing Answer Board.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"

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

$DocumentContent = Initialize-DocumentContent -FullTextList "MyFullTextList"

$PinDocument = Initialize-PinDocument -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" -DocumentId "MyDocumentId" -Attribution $Person -UpdatedBy $Person -CreateTime (Get-Date) -UpdateTime (Get-Date)

$Thumbnail = Initialize-Thumbnail -PhotoId "MyPhotoId" -Url "MyUrl"

$WritePermission = Initialize-WritePermission -ScopeType "GLOBAL" -Create $false -Update $false -Delete $false
$ObjectPermissions = Initialize-ObjectPermissions -Write $WritePermission

$Shortcut = Initialize-Shortcut -Id 0 -InputAlias "MyInputAlias" -DestinationUrl "MyDestinationUrl" -DestinationDocumentId "MyDestinationDocumentId" -Description "MyDescription" -Unlisted $false -UrlTemplate "MyUrlTemplate" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -Permissions $ObjectPermissions -CreatedBy $Person -CreateTime (Get-Date) -UpdatedBy $Person -UpdateTime (Get-Date) -DestinationDocument $Document -IntermediateUrl "MyIntermediateUrl" -ViewPrefix "MyViewPrefix" -IsExternal $false -EditUrl "MyEditUrl" -Alias "MyAlias" -Title "MyTitle" -Roles $UserRoleSpecification

$CollectionItem = Initialize-CollectionItem -Name "MyName" -Description "MyDescription" -Icon "MyIcon" -CollectionId 0 -DocumentId "MyDocumentId" -Url "MyUrl" -ItemId "MyItemId" -CreatedBy $Person -CreatedAt (Get-Date) -Document $Document -Shortcut $Shortcut -Collection $Collection -ItemType "DOCUMENT"

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"

$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$CollectionPinnedMetadata = Initialize-CollectionPinnedMetadata -ExistingPins $CollectionPinTarget -EligiblePins $CollectionPinMetadata

$Collection = Initialize-Collection -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -ChildCount 0 -Items $CollectionItem -PinMetadata $CollectionPinnedMetadata -Shortcuts "MyShortcuts" -Children $Collection -Roles $UserRoleSpecification

$Reaction = Initialize-Reaction -Type "MyType" -Count 0 -Reactors $Person -ReactedByViewer $false

$Share = Initialize-Share -NumDaysAgo 0 -Sharer $Person -SharingDocument $Document

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$CountInfo = Initialize-CountInfo -Count 0 -Period $Period -Org "MyOrg"

$DocumentInteractions = Initialize-DocumentInteractions -NumComments 0 -NumReactions 0 -Reactions "MyReactions" -Reacts $Reaction -Shares $Share -VisitorCount $CountInfo

$Reminder = Initialize-Reminder -Assignee $Person -Requestor $Person -RemindAt 0 -CreatedAt 0 -Reason "MyReason"

$VerificationMetadata = Initialize-VerificationMetadata -LastVerifier $Person -LastVerificationTs 0 -ExpirationTs 0 -Document $Document -Reminders $Reminder -LastReminder $Reminder -VisitorCount $CountInfo -CandidateVerifiers $Person

$Verification = Initialize-Verification -State "UNVERIFIED" -Metadata $VerificationMetadata

$ViewerInfo = Initialize-ViewerInfo -Role "ANSWER_MODERATOR" -LastViewedTime (Get-Date)
$CustomDataValue = Initialize-CustomDataValue -DisplayLabel "MyDisplayLabel" -StringValue "MyStringValue" -StringListValue "MyStringListValue" -NumberValue 0
$IndexStatus = Initialize-IndexStatus -LastCrawledTime (Get-Date) -LastIndexedTime (Get-Date)
$DocumentMetadata = Initialize-DocumentMetadata -Datasource "MyDatasource" -DatasourceInstance "MyDatasourceInstance" -ObjectType "MyObjectType" -Container "MyContainer" -ContainerId "MyContainerId" -SuperContainerId "MySuperContainerId" -ParentId "MyParentId" -MimeType "MyMimeType" -DocumentId "MyDocumentId" -LoggingId "MyLoggingId" -DocumentIdHash "MyDocumentIdHash" -CreateTime (Get-Date) -UpdateTime (Get-Date) -Author $Person -Owner $Person -Visibility "PRIVATE" -Components "MyComponents" -Status "MyStatus" -StatusCategory "MyStatusCategory" -Pins $PinDocument -Priority "MyPriority" -AssignedTo $Person -UpdatedBy $Person -Labels "MyLabels" -Collections $Collection -DatasourceId "MyDatasourceId" -Interactions $DocumentInteractions -Verification $Verification -ViewerInfo $ViewerInfo -Permissions $ObjectPermissions -VisitCount $CountInfo -Shortcuts $Shortcut -Path "MyPath" -CustomData @{ key_example = $CustomDataValue } -DocumentCategory "MyDocumentCategory" -ContactPerson $Person -Thumbnail $Thumbnail -IndexStatus $IndexStatus -Ancestors $Document

$DocumentSection = Initialize-DocumentSection -Title "MyTitle" -Url "MyUrl"
$Document = Initialize-Document -Id "MyId" -Datasource "MyDatasource" -ConnectorType "API_CRAWL" -DocType "MyDocType" -Content $DocumentContent -ContainerDocument $Document -ParentDocument $Document -Title "MyTitle" -Url "MyUrl" -Metadata $DocumentMetadata -Sections $DocumentSection

$TextRange = Initialize-TextRange -StartIndex 0 -EndIndex 0 -Type "BOLD" -Url "MyUrl" -Document $Document

$QuerySuggestion = Initialize-QuerySuggestion -MissingTerm "MyMissingTerm" -Query "MyQuery" -Label "MyLabel" -Datasource "MyDatasource" -RequestOptions $SearchRequestOptions -Ranges $TextRange

$Company = Initialize-Company -Name "MyName" -ProfileUrl "MyProfileUrl" -WebsiteUrls "MyWebsiteUrls" -LogoUrl "MyLogoUrl" -Location "New York City" -Phone "MyPhone" -Fax "MyFax" -Industry "Finances" -AnnualRevenue 0 -NumberOfEmployees 0 -StockSymbol "MyStockSymbol" -FoundedDate (Get-Date) -About "Financial, software, data, and media company headquartered in Midtown Manhattan, New York City"

$CustomerMetadata = Initialize-CustomerMetadata -DatasourceId "MyDatasourceId" -CustomData @{ key_example = $CustomDataValue }

$Customer = Initialize-Customer -Id "MyId" -Domains "MyDomains" -Company $Company -DocumentCounts @{ key_example = 0 } -Poc $Person -Metadata $CustomerMetadata -MergedCustomers $Customer -StartDate (Get-Date) -ContractAnnualRevenue 0 -Notes "CIO is interested in trying out the product."

$RelatedObjectMetadata = Initialize-RelatedObjectMetadata -Name "MyName"
$RelatedObject = Initialize-RelatedObject -Id "MyId" -Metadata $RelatedObjectMetadata

$RelatedObjectEdge = Initialize-RelatedObjectEdge -Objects $RelatedObject

$PersonToTeamRelationship = Initialize-PersonToTeamRelationship -Person $Person -Relationship "MEMBER" -CustomRelationshipStr "MyCustomRelationshipStr" -JoinDate (Get-Date)

$TeamEmail = Initialize-TeamEmail -Email "MyEmail" -Type "PRIMARY" -IsUserGenerated $false
$DatasourceProfile = Initialize-DatasourceProfile -Datasource "github" -Handle "MyHandle" -Url "MyUrl" -NativeAppUrl "MyNativeAppUrl" -IsUserGenerated $false
$Team = Initialize-Team -RelatedObjects @{ key_example = $RelatedObjectEdge } -Permissions $ObjectPermissions -Id "MyId" -Name "MyName" -Description "MyDescription" -BusinessUnit "MyBusinessUnit" -Department "MyDepartment" -PhotoUrl "MyPhotoUrl" -BannerUrl "MyBannerUrl" -ExternalLink "MyExternalLink" -Members $PersonToTeamRelationship -MemberCount 0 -Emails $TeamEmail -DatasourceProfiles $DatasourceProfile -Datasource "MyDatasource" -CreatedFrom "MyCreatedFrom" -LastUpdatedAt (Get-Date) -Status "PROCESSED" -CanBeDeleted $false -LoggingId "MyLoggingId"

$CustomEntityMetadata = Initialize-CustomEntityMetadata -CustomData @{ key_example = $CustomDataValue }

$CustomEntity = Initialize-CustomEntity -Permissions $ObjectPermissions -Id "MyId" -Title "MyTitle" -Datasource "MyDatasource" -ObjectType "MyObjectType" -Metadata $CustomEntityMetadata -Roles $UserRoleSpecification

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

$AnswerLike = Initialize-AnswerLike -User $Person -CreateTime (Get-Date)

$AnswerLikes = Initialize-AnswerLikes -LikedBy $AnswerLike -LikedByUser $false -NumLikes 0

$AnswerBoard = Initialize-AnswerBoard -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Permissions $ObjectPermissions -Id 0 -CreateTime (Get-Date) -UpdateTime (Get-Date) -Creator $Person -UpdatedBy $Person -ItemCount 0 -Roles $UserRoleSpecification

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

$Group = Initialize-Group -Type "DEPARTMENT" -Id "MyId" -Name "MyName"
$UserRoleSpecification = Initialize-UserRoleSpecification -SourceDocumentSpec $DocumentSpec -Person $Person -Group $Group -Role "OWNER"

$EditAnswerBoardRequest = Initialize-EditAnswerBoardRequest -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Id 0 # EditAnswerBoardRequest | Answer Board content plus any additional metadata for the request.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Answer Board
try {
    $Result = Edit-answerboard -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-answerboard: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditAnswerBoardRequest**](EditAnswerBoardRequest.md)| Answer Board content plus any additional metadata for the request. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**EditAnswerBoardResponse**](EditAnswerBoardResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-answer"></a>
# **Get-answer**
> GetAnswerResponse Get-answer<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read Answer

Read the details of a particular Answer given its ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetAnswerRequest = Initialize-GetAnswerRequest -Id 3 -DocId "ANSWERS_answer_3" # GetAnswerRequest | GetAnswer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read Answer
try {
    $Result = Get-answer -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-answer: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetAnswerRequest**](GetAnswerRequest.md)| GetAnswer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetAnswerResponse**](GetAnswerResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-answerboard"></a>
# **Get-answerboard**
> GetAnswerBoardResponse Get-answerboard<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read Answer Board

Read the details of an Answer Board given its ID. Does not fetch items in this Answer Board, use /listanswers instead.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetAnswerBoardRequest = Initialize-GetAnswerBoardRequest -Id 0 # GetAnswerBoardRequest | GetAnswerBoard request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read Answer Board
try {
    $Result = Get-answerboard -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-answerboard: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetAnswerBoardRequest**](GetAnswerBoardRequest.md)| GetAnswerBoard request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetAnswerBoardResponse**](GetAnswerBoardResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listanswerboards"></a>
# **Invoke-Listanswerboards**
> ListAnswerBoardsResponse Invoke-Listanswerboards<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List Answer Boards

List all existing Answer Boards

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ListAnswerBoardsRequest = Initialize-ListAnswerBoardsRequest -WithAudience $false -WithRoles $false # ListAnswerBoardsRequest | ListAnswerBoards request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List Answer Boards
try {
    $Result = Invoke-Listanswerboards -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listanswerboards: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ListAnswerBoardsRequest**](ListAnswerBoardsRequest.md)| ListAnswerBoards request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListAnswerBoardsResponse**](ListAnswerBoardsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listanswers"></a>
# **Invoke-Listanswers**
> ListAnswersResponse Invoke-Listanswers<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List Answers

List Answers created by the current user.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ListAnswersRequest = Initialize-ListAnswersRequest -BoardId 0 # ListAnswersRequest | ListAnswers request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List Answers
try {
    $Result = Invoke-Listanswers -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listanswers: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ListAnswersRequest**](ListAnswersRequest.md)| ListAnswers request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListAnswersResponse**](ListAnswersResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Previewanswer"></a>
# **Invoke-Previewanswer**
> PreviewStructuredTextResponse Invoke-Previewanswer<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Preview Answer

Generate a preview for a user-generated Answer that contains a question and answer.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$PreviewStructuredTextRequest = Initialize-PreviewStructuredTextRequest -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." # PreviewStructuredTextRequest | PreviewAnswer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Preview Answer
try {
    $Result = Invoke-Previewanswer -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Previewanswer: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PreviewStructuredTextRequest**](PreviewStructuredTextRequest.md)| PreviewAnswer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewStructuredTextResponse**](PreviewStructuredTextResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Previewanswerdraft"></a>
# **Invoke-Previewanswerdraft**
> PreviewUgcResponse Invoke-Previewanswerdraft<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Preview draft Answer

Generate a preview for a user-generated answer from a draft.

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

$PreviewUgcRequest = Initialize-PreviewUgcRequest -Draft $UgcDraft -DraftSpec $DocumentSpec -Type "ANNOUNCEMENTS_TYPE" # PreviewUgcRequest | preview answer request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Preview draft Answer
try {
    $Result = Invoke-Previewanswerdraft -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Previewanswerdraft: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PreviewUgcRequest**](PreviewUgcRequest.md)| preview answer request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewUgcResponse**](PreviewUgcResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Update-answerlikes"></a>
# **Update-answerlikes**
> UpdateAnswerLikesResponse Update-answerlikes<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Answer likes

Update the likes for an existing user-generated Answer. Examples are liking or unliking the Answer.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$UpdateAnswerLikesRequest = Initialize-UpdateAnswerLikesRequest -AnswerId 3 -AnswerDocId "ANSWERS_answer_3" -Action "LIKE" # UpdateAnswerLikesRequest | UpdateAnswerLikes request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Answer likes
try {
    $Result = Update-answerlikes -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Update-answerlikes: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**UpdateAnswerLikesRequest**](UpdateAnswerLikesRequest.md)| UpdateAnswerLikes request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**UpdateAnswerLikesResponse**](UpdateAnswerLikesResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

