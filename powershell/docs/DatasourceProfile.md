# DatasourceProfile
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Datasource** | **String** | The datasource the profile is of. | 
**Handle** | **String** | The display name of the entity in the given datasource. | 
**Url** | **String** | URL to view the entity&#39;s profile. | [optional] 
**NativeAppUrl** | **String** | A deep link, if available, into the datasource&#39;s native application for the entity&#39;s platform (i.e. slack://...). | [optional] 
**IsUserGenerated** | **Boolean** | For internal use only. True iff the data source profile was manually added by a user from within Glean (aka not from the original data source) | [optional] 

## Examples

- Prepare the resource
```powershell
$DatasourceProfile = Initialize-PSOpenAPIToolsDatasourceProfile  -Datasource github `
 -Handle null `
 -Url null `
 -NativeAppUrl null `
 -IsUserGenerated null
```

- Convert the resource to JSON
```powershell
$DatasourceProfile | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

