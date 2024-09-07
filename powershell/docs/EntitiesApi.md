# PSOpenAPITools.PSOpenAPITools\Api.EntitiesApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Listentities**](EntitiesApi.md#Invoke-Listentities) | **POST** /listentities | List entities
[**Invoke-People**](EntitiesApi.md#Invoke-People) | **POST** /people | Read people
[**Invoke-Teams**](EntitiesApi.md#Invoke-Teams) | **POST** /teams | Read teams


<a id="Invoke-Listentities"></a>
# **Invoke-Listentities**
> ListEntitiesResponse Invoke-Listentities<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

List entities

List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$SortOptions = Initialize-SortOptions -OrderBy "ASC" -SortBy "MySortBy"
"PEOPLE"$ListEntitiesRequest = Initialize-ListEntitiesRequest -VarFilter $FacetFilter -Sort $SortOptions -EntityType "PEOPLE" -Datasource "MyDatasource" -Query "MyQuery" -IncludeFields 

$FacetFilterValue = Initialize-FacetFilterValue -Value "Spreadsheet" -RelationType "EQUALS" -IsNegated $false
$FacetFilter = Initialize-FacetFilter -FieldName "owner" -Values $FacetFilterValue -GroupName "Spreadsheet"

$SortOptions = Initialize-SortOptions -OrderBy "ASC" -SortBy "MySortBy"
"PEOPLE" -PageSize 100 -Cursor "MyCursor" -Source "MySource" # ListEntitiesRequest | List people request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# List entities
try {
    $Result = Invoke-Listentities -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Listentities: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**ListEntitiesRequest**](ListEntitiesRequest.md)| List people request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListEntitiesResponse**](ListEntitiesResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-People"></a>
# **Invoke-People**
> PeopleResponse Invoke-People<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read people

Read people details for the given IDs.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

"BADGES""PEOPLE_WITHOUT_MANAGER"$PeopleRequest = Initialize-PeopleRequest -TimezoneOffset 0 -ObfuscatedIds "MyObfuscatedIds" -EmailIds "MyEmailIds" -IncludeFields "BADGES" -IncludeTypes "BADGES""PEOPLE_WITHOUT_MANAGER" -Source "MySource" # PeopleRequest | People request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read people
try {
    $Result = Invoke-People -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-People: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**PeopleRequest**](PeopleRequest.md)| People request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PeopleResponse**](PeopleResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Teams"></a>
# **Invoke-Teams**
> TeamsResponse Invoke-Teams<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>

Read teams

Read the details of the teams with the given IDs.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

"TEAMS_DETAILS"$TeamsRequest = Initialize-TeamsRequest -Ids "MyIds" -IncludeFields "TEAMS_DETAILS" # TeamsRequest | Teams request
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

# Read teams
try {
    $Result = Invoke-Teams -Payload $Payload -XScioActas $XScioActas
} catch {
    Write-Host ("Exception occurred when calling Invoke-Teams: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | [**TeamsRequest**](TeamsRequest.md)| Teams request | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**TeamsResponse**](TeamsResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

