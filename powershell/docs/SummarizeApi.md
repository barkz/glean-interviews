# PSOpenAPITools.PSOpenAPITools\Api.SummarizeApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Summarize**](SummarizeApi.md#Invoke-Summarize) | **POST** /summarize | Summarize documents


<a id="Invoke-Summarize"></a>
# **Invoke-Summarize**
> SummarizeResponse Invoke-Summarize<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Summarize documents

Generate an AI summary of the requested documents.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DocumentSpec = Initialize-DocumentSpec -Url "MyUrl" -Id "MyId" -UgcType "ANNOUNCEMENTS" -ContentId 0 -DocType "MyDocType"
$SummarizeRequest = Initialize-SummarizeRequest -Timestamp (Get-Date) -Query "MyQuery" -PreferredSummaryLength 0 -DocumentSpecs $DocumentSpec -TrackingToken "MyTrackingToken" # SummarizeRequest | Includes request params such as the query and specs of the documents to summarize.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Summarize documents
try {
    $Result = Invoke-Summarize -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Summarize: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**SummarizeRequest**](SummarizeRequest.md)| Includes request params such as the query and specs of the documents to summarize. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**SummarizeResponse**](SummarizeResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

