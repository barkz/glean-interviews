# PSOpenAPITools.PSOpenAPITools\Api.ActivityApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Activity**](ActivityApi.md#Invoke-Activity) | **POST** /activity | Report document activity
[**Invoke-Feedback**](ActivityApi.md#Invoke-Feedback) | **POST** /feedback | Report client activity


<a id="Invoke-Activity"></a>
# **Invoke-Activity**
> void Invoke-Activity<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>

Report document activity

Report user activity that occurs on indexed documents such as viewing or editing. This signal improves search quality.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ActivityEventParams = Initialize-ActivityEventParams -BodyContent "MyBodyContent" -DatasourceInstance "MyDatasourceInstance" -Datasource "MyDatasource" -InstanceOnlyName "MyInstanceOnlyName" -Duration 0 -Query "MyQuery" -Referrer "MyReferrer" -Title "MyTitle" -Truncated $false
$ActivityEvent = Initialize-ActivityEvent -Id "MyId" -Action "VIEW" -Params $ActivityEventParams -Timestamp (Get-Date) -Url "MyUrl"

$Activity = Initialize-Activity -Events $ActivityEvent # Activity | 

# Report document activity
try {
    $Result = Invoke-Activity -Payload $Payload
} catch {
    Write-Host ("Exception occurred when calling Invoke-Activity: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**Activity**](Activity.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Feedback"></a>
# **Invoke-Feedback**
> void Invoke-Feedback<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Feedback] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>

Report client activity

Report events that happen to results within a Glean client UI, such as search result views and clicks.  This signal improves search quality.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$Feedback = "MyFeedback" # String | A URL encoded versions of Feedback. This is useful for requests. (optional)
$SessionInfo = Initialize-SessionInfo -SessionTrackingToken "MySessionTrackingToken" -TabId "MyTabId" -LastSeen (Get-Date) -LastQuery "MyLastQuery"
$User = Initialize-User -UserID "MyUserID" -OrigID "MyOrigID"
"COMPANY"$ManualFeedbackInfo = Initialize-ManualFeedbackInfo -Email "MyEmail" -Source "AUTOCOMPLETE" -Issue "MyIssue" -ImageUrls "MyImageUrls" -Query "MyQuery" -ObscuredQuery "MyObscuredQuery" -ActiveTab "MyActiveTab" -Comments "MyComments" -SearchResults "MySearchResults" -PreviousMessages "MyPreviousMessages" -NumQueriesFromFirstRun 0 -Vote "UPVOTE" -Rating 0 -RatingKey "MyRatingKey" -RatingScale 0
$SeenFeedbackInfo = Initialize-SeenFeedbackInfo -IsExplicit $false
$UserViewInfo = Initialize-UserViewInfo -DocId "MyDocId" -DocTitle "MyDocTitle" -DocUrl "MyDocUrl"
$FeedbackDebugInfo = Initialize-FeedbackDebugInfo -DesktopAppVersion "MyDesktopAppVersion"
$Feedback = Initialize-Feedback -Id "MyId" -Category "ANNOUNCEMENT" -TrackingTokens "MyTrackingTokens" -VarEvent "CLICK" -Position 0 -Payload "MyPayload" -SessionInfo $SessionInfo -Timestamp (Get-Date) -User $User -Pathname "MyPathname" -Channels 
$SessionInfo = Initialize-SessionInfo -SessionTrackingToken "MySessionTrackingToken" -TabId "MyTabId" -LastSeen (Get-Date) -LastQuery "MyLastQuery"
$User = Initialize-User -UserID "MyUserID" -OrigID "MyOrigID"
"COMPANY" -Url "MyUrl" -UiElement "MyUiElement" -ManualFeedbackInfo $ManualFeedbackInfo -SeenFeedbackInfo $SeenFeedbackInfo -UserViewInfo $UserViewInfo -DebugInfo $FeedbackDebugInfo -ApplicationId "MyApplicationId" # Feedback |  (optional)

# Report client activity
try {
    $Result = Invoke-Feedback -XScioActas $XScioActas -Feedback $Feedback -Payload $Payload
} catch {
    Write-Host ("Exception occurred when calling Invoke-Feedback: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Feedback** | **String**| A URL encoded versions of Feedback. This is useful for requests. | [optional] 
 **Payload** | [**Feedback**](Feedback.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

