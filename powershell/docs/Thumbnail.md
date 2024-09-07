# Thumbnail
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PhotoId** | **String** | Photo id if the thumbnail is from splash. | [optional] 
**Url** | **String** | Thumbnail URL. This can be user provided image and/or from downloaded images hosted by Glean. | [optional] 

## Examples

- Prepare the resource
```powershell
$Thumbnail = Initialize-PSOpenAPIToolsThumbnail  -PhotoId null `
 -Url null
```

- Convert the resource to JSON
```powershell
$Thumbnail | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

