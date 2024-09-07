# StructuredLocation
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DeskLocation** | **String** | Desk number. | [optional] 
**Timezone** | **String** | Location&#39;s timezone, e.g. UTC, PST. | [optional] 
**Address** | **String** | Office address or name. | [optional] 
**City** | **String** | Name of the city. | [optional] 
**State** | **String** | State code. | [optional] 
**Region** | **String** | Region information, e.g. NORAM, APAC. | [optional] 
**ZipCode** | **String** | ZIP Code for the address. | [optional] 
**Country** | **String** | Country name. | [optional] 
**CountryCode** | **String** | Alpha-2 or Alpha-3 ISO 3166 country code, e.g. US or USA. | [optional] 

## Examples

- Prepare the resource
```powershell
$StructuredLocation = Initialize-PSOpenAPIToolsStructuredLocation  -DeskLocation null `
 -Timezone null `
 -Address null `
 -City null `
 -State null `
 -Region null `
 -ZipCode null `
 -Country null `
 -CountryCode null
```

- Convert the resource to JSON
```powershell
$StructuredLocation | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

