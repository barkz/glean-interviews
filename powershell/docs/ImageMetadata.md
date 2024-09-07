# ImageMetadata
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | [**ImageType**](ImageType.md) |  | 
**Id** | **String** | ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. | [optional] 
**Ds** | **String** | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. | [optional] 
**Cid** | **String** | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 
**Ext** | **String** | Extension the image is saved with. The extension data is deduced from content type for image uploads. | [optional] 

## Examples

- Prepare the resource
```powershell
$ImageMetadata = Initialize-PSOpenAPIToolsImageMetadata  -Type null `
 -Id null `
 -Ds null `
 -Cid null `
 -Ext null
```

- Convert the resource to JSON
```powershell
$ImageMetadata | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

