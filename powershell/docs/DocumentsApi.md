# PSOpenAPITools.PSOpenAPITools\Api.DocumentsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Get-docpermissions**](DocumentsApi.md#Get-docpermissions) | **POST** /getdocpermissions | Read document permissions
[**Get-documentanalytics**](DocumentsApi.md#Get-documentanalytics) | **POST** /getdocumentanalytics | Read document analytics
[**Get-documents**](DocumentsApi.md#Get-documents) | **POST** /getdocuments | Read documents


<a id="Get-docpermissions"></a>
# **Get-docpermissions**
> GetDocPermissionsResponse Get-docpermissions<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read document permissions

Read the emails of all users who have access to the given document.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetDocPermissionsRequest = Initialize-GetDocPermissionsRequest -DocumentId "MyDocumentId" # GetDocPermissionsRequest | Document permissions request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read document permissions
try {
    $Result = Get-docpermissions -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-docpermissions: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetDocPermissionsRequest**](GetDocPermissionsRequest.md)| Document permissions request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDocPermissionsResponse**](GetDocPermissionsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-documentanalytics"></a>
# **Get-documentanalytics**
> GetDocumentAnalyticsResponse Get-documentanalytics<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>

Read document analytics

Read the document analytics information for the given list of Glean Document IDs or URLs specified in the request

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"

$TimePoint = Initialize-TimePoint -EpochSeconds 0 -DaysFromNow 0
$Period = Initialize-Period -MinDaysFromNow 0 -MaxDaysFromNow 0 -Start $TimePoint -VarEnd $TimePoint

$GetDocumentAnalyticsRequest = Initialize-GetDocumentAnalyticsRequest -DocumentSpecs $DocumentSpec -DayRange $Period -WithClickerCounts $false -WithImpressionCounts $false -WithFacetAggregations $false -WithVisitCounts $false # GetDocumentAnalyticsRequest | Information about analytics requested. (optional)

# Read document analytics
try {
    $Result = Get-documentanalytics -XScioActas $XScioActas -Payload $Payload
} catch {
    Write-Host ("Exception occurred when calling Get-documentanalytics: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Payload** | [**GetDocumentAnalyticsRequest**](GetDocumentAnalyticsRequest.md)| Information about analytics requested. | [optional] 

### Return type

[**GetDocumentAnalyticsResponse**](GetDocumentAnalyticsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-documents"></a>
# **Get-documents**
> GetDocumentsResponse Get-documents<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>

Read documents

Read the documents including metadata (does not include enhanced metadata via `/documentmetadata`) for the given list of Glean Document IDs or URLs specified in the request.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
"LAST_VIEWED_AT"$GetDocumentsRequest = Initialize-GetDocumentsRequest -DocumentSpecs $DocumentSpec -IncludeFields 
$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
"LAST_VIEWED_AT" # GetDocumentsRequest | Information about documents requested. (optional)

# Read documents
try {
    $Result = Get-documents -XScioActas $XScioActas -Payload $Payload
} catch {
    Write-Host ("Exception occurred when calling Get-documents: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Payload** | [**GetDocumentsRequest**](GetDocumentsRequest.md)| Information about documents requested. | [optional] 

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

