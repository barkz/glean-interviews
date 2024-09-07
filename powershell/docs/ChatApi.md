# PSOpenAPITools.PSOpenAPITools\Api.ChatApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Ask**](ChatApi.md#Invoke-Ask) | **POST** /ask | Detect and answer questions
[**Invoke-Chat**](ChatApi.md#Invoke-Chat) | **POST** /chat | Chat
[**Invoke-Deleteallchats**](ChatApi.md#Invoke-Deleteallchats) | **POST** /deleteallchats | Deletes all saved Chats owned by a user
[**Invoke-Deletechats**](ChatApi.md#Invoke-Deletechats) | **POST** /deletechats | Deletes saved Chats
[**Get-chat**](ChatApi.md#Get-chat) | **POST** /getchat | Retrieves a Chat
[**Get-chatapplication**](ChatApi.md#Get-chatapplication) | **POST** /getchatapplication | Gets the metadata for a custom Chat application
[**Invoke-Listchats**](ChatApi.md#Invoke-Listchats) | **POST** /listchats | Retrieves all saved Chats


<a id="Invoke-Ask"></a>
# **Invoke-Ask**
> AskResponse Invoke-Ask<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>

Detect and answer questions

Classify a query as information seeking or not. If so, generate an AI answer and/or provide relevant documents. Useful for integrating into existing chat interfaces.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$AskExperimentalMetadata = Initialize-AskExperimentalMetadata -QueryHasMentions $false -QueryIsLengthAppropriate $false -QueryIsAnswerable $false

$SessionInfo = Initialize-SessionInfo -SessionTrackingToken "MySessionTrackingToken" -TabId "MyTabId" -LastSeen (Get-Date) -LastQuery "MyLastQuery"

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

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

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

$SearchRequestInputDetails = Initialize-SearchRequestInputDetails -HasCopyPaste $false
$SearchRequest = Initialize-SearchRequest -Timestamp (Get-Date) -TrackingToken "MyTrackingToken" -SessionInfo $SessionInfo -SourceDocument $Document -PageSize 100 -MaxSnippetSize 400 -Query "vacation policy" -Cursor "MyCursor" -ResultTabIds "MyResultTabIds" -InputDetails $SearchRequestInputDetails -RequestOptions $SearchRequestOptions -TimeoutMillis 5000 -People $Person -DisableSpellcheck $false

$AskRequest = Initialize-AskRequest -DetectOnly $false -AskExperimentalMetadata $AskExperimentalMetadata -SearchRequest $SearchRequest -ExcludedDocumentSpecs $DocumentSpec -Operators "MyOperators" -Backend "SEARCH" -ChatApplicationId "MyChatApplicationId" # AskRequest | Ask request (optional)

# Detect and answer questions
try {
    $Result = Invoke-Ask -XScioActas $XScioActas -Payload $Payload
} catch {
    Write-Host ("Exception occurred when calling Invoke-Ask: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Payload** | [**AskRequest**](AskRequest.md)| Ask request | [optional] 

### Return type

[**AskResponse**](AskResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Chat"></a>
# **Invoke-Chat**
> ChatResponse Invoke-Chat<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Chat

Have a conversation with Glean AI. Responses will be sent as data-only server-sent events as they become available line by line. Each line will be a ChatResponse. Please reach out to the Glean support team for access to this API.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$AgentConfig = Initialize-AgentConfig -Agent "DEFAULT" -Mode "DEFAULT"

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

$StructuredTextItem = Initialize-StructuredTextItem -Link "https://en.wikipedia.org/wiki/Diffuse_sky_radiation" -Document $Document -Text "Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue."

$StructuredText = Initialize-StructuredText -Text "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light." -StructuredList $StructuredTextItem

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

$ChatFileMetadata = Initialize-ChatFileMetadata -Status "PROCESSING" -UploadTime 0 -ProcessedSize 0 -FailureReason "PARSE_FAILED"
$ChatFile = Initialize-ChatFile -Id "FILE_1234" -Name "sample.pdf" -Metadata $ChatFileMetadata

$ReferenceRange = Initialize-ReferenceRange -TextRange $TextRange -Snippets $SearchResultSnippet

$ChatMessageCitation = Initialize-ChatMessageCitation -TrackingToken "MyTrackingToken" -SourceDocument $Document -SourceFile $ChatFile -SourcePerson $Person -ReferenceRanges $ReferenceRange

$ToolConfig = Initialize-ToolConfig -DisplayName "MyDisplayName" -ObjectName "["HR ticket","Email","Chat message"]" -LogoUrl "MyLogoUrl" -Type "REDIRECT"

$PossibleValue = Initialize-PossibleValue -Value "MyValue" -Label "MyLabel"
$WriteActionParameter = Initialize-WriteActionParameter -Type "UNKNOWN" -DisplayName "MyDisplayName" -Value "MyValue" -Label "MyLabel" -IsRequired $false -Description "MyDescription" -PossibleValues $PossibleValue

$WriteAction = Initialize-WriteAction -ToolName "MyToolName" -ToolConfig $ToolConfig -RedirectUrl "MyRedirectUrl" -Parameters @{ key_example = $WriteActionParameter }

$ChatMessageFragment = Initialize-ChatMessageFragment -StructuredResults $StructuredResult -TrackingToken "MyTrackingToken" -Text "MyText" -QuerySuggestion $QuerySuggestion -WriteAction $WriteAction -File $ChatFile

$ChatMessage = Initialize-ChatMessage -AgentConfig $AgentConfig -Author "USER" -Citations $ChatMessageCitation -UploadedFileIds "MyUploadedFileIds" -Fragments $ChatMessageFragment -Metadata "MyMetadata" -Ts "MyTs" -MessageId "MyMessageId" -MessageTrackingToken "MyMessageTrackingToken" -MessageType "UPDATE" -HasMoreFragments $false

$RestrictionFilters = Initialize-RestrictionFilters -DocumentSpecs $DocumentSpec -DatasourceInstances "MyDatasourceInstances"

$ChatRequest = Initialize-ChatRequest -SaveChat $false -ChatId "MyChatId" -Messages $ChatMessage -AgentConfig $AgentConfig -Inclusions $RestrictionFilters -Exclusions $RestrictionFilters -TimeoutMillis 30000 -ApplicationId "MyApplicationId" -Stream $false # ChatRequest | Includes chat history for Glean AI to respond to.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Chat
try {
    $Result = Invoke-Chat -Payload $Payload -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Invoke-Chat: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ChatRequest**](ChatRequest.md)| Includes chat history for Glean AI to respond to. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**ChatResponse**](ChatResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deleteallchats"></a>
# **Invoke-Deleteallchats**
> void Invoke-Deleteallchats<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Deletes all saved Chats owned by a user

Deletes all saved Chats a user has had and all their contained conversational content.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Deletes all saved Chats owned by a user
try {
    $Result = Invoke-Deleteallchats -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deleteallchats: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deletechats"></a>
# **Invoke-Deletechats**
> void Invoke-Deletechats<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Deletes saved Chats

Deletes saved Chats and all their contained conversational content.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteChatsRequest = Initialize-DeleteChatsRequest -Ids "MyIds" # DeleteChatsRequest | 
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Deletes saved Chats
try {
    $Result = Invoke-Deletechats -Payload $Payload -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deletechats: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteChatsRequest**](DeleteChatsRequest.md)|  | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-chat"></a>
# **Get-chat**
> GetChatResponse Get-chat<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Retrieves a Chat

Retrieves the chat history between Glean Assistant and the user for a given Chat.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetChatRequest = Initialize-GetChatRequest -Id "MyId" # GetChatRequest | 
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Retrieves a Chat
try {
    $Result = Get-chat -Payload $Payload -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Get-chat: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetChatRequest**](GetChatRequest.md)|  | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**GetChatResponse**](GetChatResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-chatapplication"></a>
# **Get-chatapplication**
> GetChatApplicationResponse Get-chatapplication<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Gets the metadata for a custom Chat application

Gets the Chat application details for the specified application ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetChatApplicationRequest = Initialize-GetChatApplicationRequest -Id "MyId" # GetChatApplicationRequest | 
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Gets the metadata for a custom Chat application
try {
    $Result = Get-chatapplication -Payload $Payload -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Get-chatapplication: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetChatApplicationRequest**](GetChatApplicationRequest.md)|  | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**GetChatApplicationResponse**](GetChatApplicationResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listchats"></a>
# **Invoke-Listchats**
> ListChatsResponse Invoke-Listchats<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Retrieves all saved Chats

Retrieves all the saved Chats between Glean Assistant and the user. The returned Chats contain only metadata and no conversational content.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Retrieves all saved Chats
try {
    $Result = Invoke-Listchats -XScioActas $XScioActas -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listchats: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**ListChatsResponse**](ListChatsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

