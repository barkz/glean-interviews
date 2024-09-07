# PSOpenAPITools.PSOpenAPITools\Api.MessagesApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Messages**](MessagesApi.md#Invoke-Messages) | **POST** /messages | Read messages


<a id="Invoke-Messages"></a>
# **Invoke-Messages**
> MessagesResponse Invoke-Messages<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read messages

Retrieves list of messages from messaging/chat datasources (e.g. Slack, Teams).

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$MessagesRequest = Initialize-MessagesRequest -IdType "CHANNEL_NAME" -Id "MyId" -WorkspaceId "MyWorkspaceId" -Direction "OLDER" -TimestampMillis 0 -IncludeRootMessage $false -Datasource "SLACK" -DatasourceInstanceDisplayName "MyDatasourceInstanceDisplayName" # MessagesRequest | Includes request params such as the id for channel/message and direction.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read messages
try {
    $Result = Invoke-Messages -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Messages: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**MessagesRequest**](MessagesRequest.md)| Includes request params such as the id for channel/message and direction. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**MessagesResponse**](MessagesResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

