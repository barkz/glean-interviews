# PSOpenAPITools.PSOpenAPITools\Api.CollectionsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Add-collectionitems**](CollectionsApi.md#Add-collectionitems) | **POST** /addcollectionitems | Add Collection item
[**New-collection**](CollectionsApi.md#New-collection) | **POST** /createcollection | Create Collection
[**Invoke-Deletecollection**](CollectionsApi.md#Invoke-Deletecollection) | **POST** /deletecollection | Delete Collection
[**Invoke-Deletecollectionitem**](CollectionsApi.md#Invoke-Deletecollectionitem) | **POST** /deletecollectionitem | Delete Collection item
[**Edit-collection**](CollectionsApi.md#Edit-collection) | **POST** /editcollection | Update Collection
[**Edit-collectionitem**](CollectionsApi.md#Edit-collectionitem) | **POST** /editcollectionitem | Update Collection item
[**Edit-documentcollections**](CollectionsApi.md#Edit-documentcollections) | **POST** /editdocumentcollections | Update document Collections
[**Get-collection**](CollectionsApi.md#Get-collection) | **POST** /getcollection | Read Collection
[**Invoke-Listcollections**](CollectionsApi.md#Invoke-Listcollections) | **POST** /listcollections | List Collections
[**Move-collectionitem**](CollectionsApi.md#Move-collectionitem) | **POST** /movecollectionitem | Move Collection item
[**Invoke-Pincollection**](CollectionsApi.md#Invoke-Pincollection) | **POST** /pincollection | Pin Collection


<a id="Add-collectionitems"></a>
# **Add-collectionitems**
> AddCollectionItemsResponse Add-collectionitems<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Add Collection item

Add items to a Collection.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$CollectionItemDescriptor = Initialize-CollectionItemDescriptor -Url "MyUrl" -DocumentId "MyDocumentId" -NewNextItemId "MyNewNextItemId" -ItemType "DOCUMENT" -Name "MyName" -Description "MyDescription" -Icon "MyIcon"
$AddCollectionItemsRequest = Initialize-AddCollectionItemsRequest -CollectionId 0 -AddedCollectionItemDescriptors $CollectionItemDescriptor # AddCollectionItemsRequest | Data describing the add operation.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Add Collection item
try {
    $Result = Add-collectionitems -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Add-collectionitems: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**AddCollectionItemsRequest**](AddCollectionItemsRequest.md)| Data describing the add operation. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**AddCollectionItemsResponse**](AddCollectionItemsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="New-collection"></a>
# **New-collection**
> CreateCollectionResponse New-collection<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create Collection

Create a publicly visible (empty) Collection of documents.

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

$CreateCollectionRequest = Initialize-CreateCollectionRequest -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -NewNextItemId "MyNewNextItemId" # CreateCollectionRequest | Collection content plus any additional metadata for the request.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create Collection
try {
    $Result = New-collection -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-collection: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateCollectionRequest**](CreateCollectionRequest.md)| Collection content plus any additional metadata for the request. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deletecollection"></a>
# **Invoke-Deletecollection**
> void Invoke-Deletecollection<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete Collection

Delete a Collection given the Collection's ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteCollectionRequest = Initialize-DeleteCollectionRequest -Ids 0 -AllowedDatasource "MyAllowedDatasource" # DeleteCollectionRequest | DeleteCollection request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete Collection
try {
    $Result = Invoke-Deletecollection -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deletecollection: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteCollectionRequest**](DeleteCollectionRequest.md)| DeleteCollection request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deletecollectionitem"></a>
# **Invoke-Deletecollectionitem**
> DeleteCollectionItemResponse Invoke-Deletecollectionitem<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete Collection item

Delete a single item from a Collection.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteCollectionItemRequest = Initialize-DeleteCollectionItemRequest -CollectionId 0 -ItemId "MyItemId" -DocumentId "MyDocumentId" # DeleteCollectionItemRequest | Data describing the delete operation.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete Collection item
try {
    $Result = Invoke-Deletecollectionitem -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deletecollectionitem: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteCollectionItemRequest**](DeleteCollectionItemRequest.md)| Data describing the delete operation. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**DeleteCollectionItemResponse**](DeleteCollectionItemResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Edit-collection"></a>
# **Edit-collection**
> EditCollectionResponse Edit-collection<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Collection

Update the properties of an existing Collection.

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

$EditCollectionRequest = Initialize-EditCollectionRequest -Name "MyName" -Description "MyDescription" -AddedRoles $UserRoleSpecification -RemovedRoles $UserRoleSpecification -AudienceFilters $FacetFilter -Icon "MyIcon" -AdminLocked $false -ParentId 0 -Thumbnail $Thumbnail -AllowedDatasource "MyAllowedDatasource" -Id 0 # EditCollectionRequest | Collection content plus any additional metadata for the request.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Collection
try {
    $Result = Edit-collection -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-collection: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditCollectionRequest**](EditCollectionRequest.md)| Collection content plus any additional metadata for the request. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**EditCollectionResponse**](EditCollectionResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Edit-collectionitem"></a>
# **Edit-collectionitem**
> EditCollectionItemResponse Edit-collectionitem<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update Collection item

Update the URL, Glean Document ID, description of an item within a Collection given its ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$EditCollectionItemRequest = Initialize-EditCollectionItemRequest -CollectionId 0 -ItemId "MyItemId" -Name "MyName" -Description "MyDescription" -Icon "MyIcon" # EditCollectionItemRequest | Edit Collection Items request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update Collection item
try {
    $Result = Edit-collectionitem -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-collectionitem: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditCollectionItemRequest**](EditCollectionItemRequest.md)| Edit Collection Items request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**EditCollectionItemResponse**](EditCollectionItemResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Edit-documentcollections"></a>
# **Edit-documentcollections**
> EditDocumentCollectionsResponse Edit-documentcollections<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update document Collections

Update the Collections that a document belongs to.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$EditDocumentCollectionsRequest = Initialize-EditDocumentCollectionsRequest -AddedCollections 0 -RemovedCollections 0 -DocumentId "MyDocumentId" -Url "MyUrl" -Name "MyName" -Description "MyDescription" # EditDocumentCollectionsRequest | Data describing the edit operation.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update document Collections
try {
    $Result = Edit-documentcollections -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-documentcollections: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditDocumentCollectionsRequest**](EditDocumentCollectionsRequest.md)| Data describing the edit operation. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**EditDocumentCollectionsResponse**](EditDocumentCollectionsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-collection"></a>
# **Get-collection**
> GetCollectionResponse Get-collection<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read Collection

Read the details of a Collection given its ID. Does not fetch items in this Collection.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetCollectionRequest = Initialize-GetCollectionRequest -Id 0 -WithItems $false -WithHierarchy $false -AllowedDatasource "MyAllowedDatasource" # GetCollectionRequest | GetCollection request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read Collection
try {
    $Result = Get-collection -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-collection: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetCollectionRequest**](GetCollectionRequest.md)| GetCollection request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listcollections"></a>
# **Invoke-Listcollections**
> ListCollectionsResponse Invoke-Listcollections<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List Collections

List all existing Collections.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ListCollectionsRequest = Initialize-ListCollectionsRequest -IncludeAudience $false -IncludeRoles $false -AllowedDatasource "MyAllowedDatasource" # ListCollectionsRequest | ListCollections request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List Collections
try {
    $Result = Invoke-Listcollections -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listcollections: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ListCollectionsRequest**](ListCollectionsRequest.md)| ListCollections request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Move-collectionitem"></a>
# **Move-collectionitem**
> MoveCollectionItemResponse Move-collectionitem<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Move Collection item

Reorder a Collection by moving a CollectionItem below another CollectionItem.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$MoveCollectionItemRequest = Initialize-MoveCollectionItemRequest -CollectionId 0 -ItemId "MyItemId" -NewNextItemId "MyNewNextItemId" # MoveCollectionItemRequest | MoveCollectionItems request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Move Collection item
try {
    $Result = Move-collectionitem -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Move-collectionitem: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**MoveCollectionItemRequest**](MoveCollectionItemRequest.md)| MoveCollectionItems request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**MoveCollectionItemResponse**](MoveCollectionItemResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Pincollection"></a>
# **Invoke-Pincollection**
> GetCollectionResponse Invoke-Pincollection<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Pin Collection

Given the Collection id and category, pins the Collection to the home page for all company users.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$CollectionPinTarget = Initialize-CollectionPinTarget -Category "COMPANY_RESOURCE" -Value "MyValue" -Target "RESOURCE_CARD"
$CollectionPinMetadata = Initialize-CollectionPinMetadata -Id 0 -Target $CollectionPinTarget

$PinCollectionRequest = Initialize-PinCollectionRequest -Action "PIN" -VarData $CollectionPinMetadata # PinCollectionRequest | PinCollection request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Pin Collection
try {
    $Result = Invoke-Pincollection -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Pincollection: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PinCollectionRequest**](PinCollectionRequest.md)| PinCollection request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

