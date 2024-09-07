# PSOpenAPITools.PSOpenAPITools\Api.CalendarApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Get-events**](CalendarApi.md#Get-events) | **POST** /getevents | Read events


<a id="Get-events"></a>
# **Get-events**
> GetEventsResponse Get-events<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read events

Read detailed information about the given event ids.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$AuthToken = Initialize-AuthToken -AccessToken "MyAccessToken" -Datasource "MyDatasource" -Scope "MyScope" -TokenType "MyTokenType" -AuthUser "MyAuthUser" -Expiration 0
$GetEventsRequest = Initialize-GetEventsRequest -Ids "MyIds" -AuthTokens $AuthToken -Datasource "MyDatasource" -Annotate $false # GetEventsRequest | GetEvents request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read events
try {
    $Result = Get-events -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-events: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetEventsRequest**](GetEventsRequest.md)| GetEvents request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetEventsResponse**](GetEventsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

