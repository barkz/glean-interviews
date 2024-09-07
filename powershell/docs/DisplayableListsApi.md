# PSOpenAPITools.PSOpenAPITools\Api.DisplayableListsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**New-displayablelists**](DisplayableListsApi.md#New-displayablelists) | **POST** /createdisplayablelists | Create displayable lists
[**Invoke-Deletedisplayablelists**](DisplayableListsApi.md#Invoke-Deletedisplayablelists) | **POST** /deletedisplayablelists | Delete displayable lists
[**Get-displayablelists**](DisplayableListsApi.md#Get-displayablelists) | **POST** /getdisplayablelists | Read displayable lists
[**Update-displayablelists**](DisplayableListsApi.md#Update-displayablelists) | **POST** /updatedisplayablelists | Update displayable lists


<a id="New-displayablelists"></a>
# **New-displayablelists**
> CreateDisplayableListsResponse New-displayablelists<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create displayable lists

Create one or more lists that can be display on the home page.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$DisplayableListItemUIConfig = Initialize-DisplayableListItemUIConfig -ShowNewIndicator $false
$DisplayableListConfig = Initialize-DisplayableListConfig -Format "LIST" -Title "MyTitle" -Enabled $false -AudienceFilters $FacetFilter -ItemUIConfig $DisplayableListItemUIConfig

$DisplayableList = Initialize-DisplayableList -Source "SAVED_SEARCH" -Id 0 -SourceId "MySourceId" -Config $DisplayableListConfig

$CreateDisplayableListsRequest = Initialize-CreateDisplayableListsRequest -Items $DisplayableList # CreateDisplayableListsRequest | Create new displayable lists
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create displayable lists
try {
    $Result = New-displayablelists -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling New-displayablelists: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**CreateDisplayableListsRequest**](CreateDisplayableListsRequest.md)| Create new displayable lists | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateDisplayableListsResponse**](CreateDisplayableListsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Deletedisplayablelists"></a>
# **Invoke-Deletedisplayablelists**
> void Invoke-Deletedisplayablelists<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete displayable lists

Delete one or more displayable lists.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$DeleteDisplayableListsRequest = Initialize-DeleteDisplayableListsRequest -Ids 0 # DeleteDisplayableListsRequest | Updated version of the displayable list configs.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete displayable lists
try {
    $Result = Invoke-Deletedisplayablelists -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Deletedisplayablelists: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**DeleteDisplayableListsRequest**](DeleteDisplayableListsRequest.md)| Updated version of the displayable list configs. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-displayablelists"></a>
# **Get-displayablelists**
> GetDisplayableListsResponse Get-displayablelists<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read displayable lists

Read the details of the displayable lists with the given IDs.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetDisplayableListsRequest = Initialize-GetDisplayableListsRequest -Ids 0 # GetDisplayableListsRequest | 
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read displayable lists
try {
    $Result = Get-displayablelists -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-displayablelists: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetDisplayableListsRequest**](GetDisplayableListsRequest.md)|  | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDisplayableListsResponse**](GetDisplayableListsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Update-displayablelists"></a>
# **Update-displayablelists**
> UpdateDisplayableListsResponse Update-displayablelists<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update displayable lists

Update one or more displayable lists with all fields from request fields.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$DisplayableListItemUIConfig = Initialize-DisplayableListItemUIConfig -ShowNewIndicator $false
$DisplayableListConfig = Initialize-DisplayableListConfig -Format "LIST" -Title "MyTitle" -Enabled $false -AudienceFilters $FacetFilter -ItemUIConfig $DisplayableListItemUIConfig

$DisplayableList = Initialize-DisplayableList -Source "SAVED_SEARCH" -Id 0 -SourceId "MySourceId" -Config $DisplayableListConfig

$UpdateDisplayableListsRequest = Initialize-UpdateDisplayableListsRequest -Items $DisplayableList # UpdateDisplayableListsRequest | Updated version of the displayable list configs.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update displayable lists
try {
    $Result = Update-displayablelists -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Update-displayablelists: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**UpdateDisplayableListsRequest**](UpdateDisplayableListsRequest.md)| Updated version of the displayable list configs. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**UpdateDisplayableListsResponse**](UpdateDisplayableListsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

