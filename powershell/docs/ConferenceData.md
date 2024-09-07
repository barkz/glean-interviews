# ConferenceData
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **String** |  | 
**Uri** | **String** | A permalink for the conference. | 
**Source** | **String** |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ConferenceData = Initialize-PSOpenAPIToolsConferenceData  -Provider null `
 -Uri null `
 -Source null
```

- Convert the resource to JSON
```powershell
$ConferenceData | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

