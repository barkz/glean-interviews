# UserActivityInsight
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**User** | [**Person**](Person.md) |  | 
**Activity** | **String** | Activity e.g. search, home page visit or all. | 
**LastActivityTimestamp** | **Int32** | Unix timestamp of the last activity (in seconds since epoch UTC). | [optional] 
**ActivityCount** | [**CountInfo**](CountInfo.md) |  | [optional] 
**ActiveDayCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$UserActivityInsight = Initialize-PSOpenAPIToolsUserActivityInsight  -User null `
 -Activity null `
 -LastActivityTimestamp null `
 -ActivityCount null `
 -ActiveDayCount null
```

- Convert the resource to JSON
```powershell
$UserActivityInsight | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

