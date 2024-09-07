# PSOpenAPITools.PSOpenAPITools\Api.PinsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Edit-pin**](PinsApi.md#Edit-pin) | **POST** /editpin | Update pin
[**Get-pin**](PinsApi.md#Get-pin) | **POST** /getpin | Read pin
[**Invoke-Listpins**](PinsApi.md#Invoke-Listpins) | **POST** /listpins | List pins
[**Invoke-Pin**](PinsApi.md#Invoke-Pin) | **POST** /pin | Create pin
[**Invoke-Unpin**](PinsApi.md#Invoke-Unpin) | **POST** /unpin | Delete pin


<a id="Edit-pin"></a>
# **Edit-pin**
> PinDocument Edit-pin<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Update pin

Update an existing user-generated pin.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$EditPinRequest = Initialize-EditPinRequest -Queries "MyQueries" -AudienceFilters $FacetFilter -Id "MyId" # EditPinRequest | Edit pins request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Update pin
try {
    $Result = Edit-pin -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Edit-pin: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**EditPinRequest**](EditPinRequest.md)| Edit pins request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PinDocument**](PinDocument.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Get-pin"></a>
# **Get-pin**
> GetPinResponse Get-pin<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read pin

Read pin details given its ID.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$GetPinRequest = Initialize-GetPinRequest -Id "MyId" # GetPinRequest | Get pin request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read pin
try {
    $Result = Get-pin -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Get-pin: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**GetPinRequest**](GetPinRequest.md)| Get pin request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetPinResponse**](GetPinResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Listpins"></a>
# **Invoke-Listpins**
> ListPinsResponse Invoke-Listpins<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <SystemCollectionsHashtable><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List pins

Lists all pins.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$Payload = @{ key_example = ... } # SystemCollectionsHashtable | List pins request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List pins
try {
    $Result = Invoke-Listpins -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listpins: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | **SystemCollectionsHashtable**| List pins request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListPinsResponse**](ListPinsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Pin"></a>
# **Invoke-Pin**
> PinDocument Invoke-Pin<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Create pin

Pin a document as a result for a given search query.Pin results that are known to be a good match.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$PinRequest = Initialize-PinRequest -Queries "MyQueries" -AudienceFilters $FacetFilter -DocumentId "MyDocumentId" # PinRequest | Details about the document and query for the pin.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Create pin
try {
    $Result = Invoke-Pin -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Pin: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PinRequest**](PinRequest.md)| Details about the document and query for the pin. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PinDocument**](PinDocument.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Unpin"></a>
# **Invoke-Unpin**
> void Invoke-Unpin<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Delete pin

Unpin a previously pinned result.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$Unpin = Initialize-Unpin -Id "MyId" # Unpin | Details about the pin being unpinned.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Delete pin
try {
    $Result = Invoke-Unpin -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Unpin: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**Unpin**](Unpin.md)| Details about the pin being unpinned. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

