# PSOpenAPITools.PSOpenAPITools\Api.AuthenticationApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**New-anonymoustoken**](AuthenticationApi.md#New-anonymoustoken) | **POST** /createanonymoustoken | Create anonymous token
[**New-authtoken**](AuthenticationApi.md#New-authtoken) | **POST** /createauthtoken | Create authentication token


<a id="New-anonymoustoken"></a>
# **New-anonymoustoken**
> CreateAuthTokenResponse New-anonymoustoken<br>

Create anonymous token

Create an authentication token for an anonymous user of external search.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration


# Create anonymous token
try {
    $Result = New-anonymoustoken
} catch {
    Write-Host ("Exception occurred when calling New-anonymoustoken: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAuthTokenResponse**](CreateAuthTokenResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="New-authtoken"></a>
# **New-authtoken**
> CreateAuthTokenResponse New-authtoken<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create authentication token

Creates an authentication token for the authenticated user.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create authentication token
try {
    $Result = New-authtoken -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-authtoken: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateAuthTokenResponse**](CreateAuthTokenResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

