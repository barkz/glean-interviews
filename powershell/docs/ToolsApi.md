# PSOpenAPITools.PSOpenAPITools\Api.ToolsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Executeactiontool**](ToolsApi.md#Invoke-Executeactiontool) | **POST** /executeactiontool | Execute Action Tool


<a id="Invoke-Executeactiontool"></a>
# **Invoke-Executeactiontool**
> ExecuteActionToolResponse Invoke-Executeactiontool<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-TimezoneOffset] <System.Nullable[Int32]><br>

Execute Action Tool

Executes an Action tool with the specified parameters.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$PossibleValue = Initialize-PossibleValue -Value "MyValue" -Label "MyLabel"
$WriteActionParameter = Initialize-WriteActionParameter -Type "UNKNOWN" -DisplayName "MyDisplayName" -Value "MyValue" -Label "MyLabel" -IsRequired $false -Description "MyDescription" -PossibleValues $PossibleValue

$ExecuteActionToolRequest = Initialize-ExecuteActionToolRequest -Name "MyName" -Parameters @{ key_example = $WriteActionParameter } # ExecuteActionToolRequest | Execute Action Tool request
$TimezoneOffset = 56 # Int32 | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. (optional)

# Execute Action Tool
try {
    $Result = Invoke-Executeactiontool -Payload $Payload -TimezoneOffset $TimezoneOffset
} catch {
    Write-Host ("Exception occurred when calling Invoke-Executeactiontool: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ExecuteActionToolRequest**](ExecuteActionToolRequest.md)| Execute Action Tool request | 
 **TimezoneOffset** | **Int32**| The offset of the client&#39;s timezone in minutes from UTC. e.g. PDT is -420 because it&#39;s 7 hours behind UTC. | [optional] 

### Return type

[**ExecuteActionToolResponse**](ExecuteActionToolResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

