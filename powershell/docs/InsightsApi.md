# PSOpenAPITools.PSOpenAPITools\Api.InsightsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ConvertTo-sights**](InsightsApi.md#ConvertTo-sights) | **POST** /insights | Read insights


<a id="ConvertTo-sights"></a>
# **ConvertTo-sights**
> InsightsResponse ConvertTo-sights<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read insights

Reads the aggregate information for each user, query, and content.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

"AI""GLEAN_CHAT"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$InsightsAiAppRequestOptions = Initialize-InsightsAiAppRequestOptions -AiAppIds "MyAiAppIds"
$InsightsRequest = Initialize-InsightsRequest -Categories "AI" -Departments "MyDepartments" -AssistantActivityTypes "AI""GLEAN_CHAT" -DayRange $Period -AiAppRequestOptions $InsightsAiAppRequestOptions # InsightsRequest | Includes request params for insights dashboard data.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read insights
try {
    $Result = ConvertTo-sights -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling ConvertTo-sights: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**InsightsRequest**](InsightsRequest.md)| Includes request params for insights dashboard data. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**InsightsResponse**](InsightsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

