# PSOpenAPITools.PSOpenAPITools\Api.VerificationApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Add-verificationreminder**](VerificationApi.md#Add-verificationreminder) | **POST** /addverificationreminder | Create verification
[**Invoke-Listverifications**](VerificationApi.md#Invoke-Listverifications) | **POST** /listverifications | List verifications
[**Test-**](VerificationApi.md#Test-) | **POST** /verify | Update verification


<a id="Add-verificationreminder"></a>
# **Add-verificationreminder**
> Verification Add-verificationreminder<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create verification

Creates a verification reminder for the document. Users can create verification reminders from different product surfaces.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$ReminderRequest = Initialize-ReminderRequest -DocumentId "MyDocumentId" -Assignee "MyAssignee" -RemindInDays 0 -Reason "MyReason" # ReminderRequest | Details about the reminder.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create verification
try {
    $Result = Add-verificationreminder -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Add-verificationreminder: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ReminderRequest**](ReminderRequest.md)| Details about the reminder. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Verification**](Verification.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listverifications"></a>
# **Invoke-Listverifications**
> VerificationFeed Invoke-Listverifications<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Count] <System.Nullable[Int32]><br>

List verifications

Returns the information to be rendered in verification dashboard. Includes information for each document owned by user regarding their verifications.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$Count = 56 # Int32 | Maximum number of documents to return (optional)

# List verifications
try {
    $Result = Invoke-Listverifications -XScioActas $XScioActas -Count $Count
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listverifications: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Count** | **Int32**| Maximum number of documents to return | [optional] 

### Return type

[**VerificationFeed**](VerificationFeed.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Test-"></a>
# **Test-**
> Verification Test-<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update verification

Verify documents to keep the knowledge up to date within customer corpus.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$VerifyRequest = Initialize-VerifyRequest -DocumentId "MyDocumentId" -Action "VERIFY" # VerifyRequest | Details about the verification request.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update verification
try {
    $Result = Test- -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Test-: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**VerifyRequest**](VerifyRequest.md)| Details about the verification request. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Verification**](Verification.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

