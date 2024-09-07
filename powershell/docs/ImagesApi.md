# PSOpenAPITools.PSOpenAPITools\Api.ImagesApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Invoke-Images**](ImagesApi.md#Invoke-Images) | **GET** /images | Get image
[**Invoke-Uploadimage**](ImagesApi.md#Invoke-Uploadimage) | **POST** /uploadimage | Upload images


<a id="Invoke-Images"></a>
# **Invoke-Images**
> System.IO.FileInfo Invoke-Images<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Key] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Type] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Id] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Ds] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Cid] <String><br>

Get image

Serves images of various types (profile pic, background, UGC thumnail/content, etc).

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$Key = "MyKey" # String | Primary key for the image being asked. The key is returned by the API when an image is uploaded. If key is used, other parameters should not be used. (optional)
$Type = "BACKGROUND" # ImageType | The type of image requested. Supported values are listed in ImageMetadata.type enum. (optional)
$Id = "MyId" # String | ID, if a specific entity/type is requested. The id may have different meaning for each type. for user, it is user id, for UGC, it is the id of the content, and so on. (optional)
$Ds = "MyDs" # String | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. (optional)
$Cid = "MyCid" # String | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. (optional)

# Get image
try {
    $Result = Invoke-Images -XScioActas $XScioActas -Key $Key -Type $Type -Id $Id -Ds $Ds -Cid $Cid
} catch {
    Write-Host ("Exception occurred when calling Invoke-Images: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Key** | **String**| Primary key for the image being asked. The key is returned by the API when an image is uploaded. If key is used, other parameters should not be used. | [optional] 
 **Type** | [**ImageType**](ImageType.md)| The type of image requested. Supported values are listed in ImageMetadata.type enum. | [optional] 
 **Id** | **String**| ID, if a specific entity/type is requested. The id may have different meaning for each type. for user, it is user id, for UGC, it is the id of the content, and so on. | [optional] 
 **Ds** | **String**| A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. | [optional] 
 **Cid** | **String**| Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 

### Return type

**System.IO.FileInfo**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="Invoke-Uploadimage"></a>
# **Invoke-Uploadimage**
> UploadImageResponse Invoke-Uploadimage<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Payload] <System.IO.FileInfo><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-XScioActas] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Type] <PSCustomObject><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Id] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Ds] <String><br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-Cid] <String><br>

Upload images

Upload images for various types (profile pic, background, UGC thumnail/content, etc) with additional metadata.

### Example
```powershell
# general setting of the PowerShell module, e.g. base URL, authentication, etc
$Configuration = Get-Configuration

$Payload =  # System.IO.FileInfo | Content and metadata for the image. Content is in the POST body, metadata is in the URL.
$XScioActas = "MyXScioActas" # String | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
$Type = "BACKGROUND" # ImageType | The type of image requested. Supported values are listed in ImageMetadata.type enum. (optional)
$Id = "MyId" # String | ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. (optional)
$Ds = "MyDs" # String | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. (optional)
$Cid = "MyCid" # String | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. (optional)

# Upload images
try {
    $Result = Invoke-Uploadimage -Payload $Payload -XScioActas $XScioActas -Type $Type -Id $Id -Ds $Ds -Cid $Cid
} catch {
    Write-Host ("Exception occurred when calling Invoke-Uploadimage: {0}" -f ($_.ErrorDetails | ConvertFrom-Json))
    Write-Host ("Response headers: {0}" -f ($_.Exception.Response.Headers | ConvertTo-Json))
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **Payload** | **System.IO.FileInfo****System.IO.FileInfo**| Content and metadata for the image. Content is in the POST body, metadata is in the URL. | 
 **XScioActas** | **String**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **Type** | [**ImageType**](ImageType.md)| The type of image requested. Supported values are listed in ImageMetadata.type enum. | [optional] 
 **Id** | **String**| ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. | [optional] 
 **Ds** | **String**| A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. | [optional] 
 **Cid** | **String**| Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 

### Return type

[**UploadImageResponse**](UploadImageResponse.md) (PSCustomObject)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

