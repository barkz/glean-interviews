# SocialNetwork
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | Possible values are &quot;&quot;twitter&quot;&quot;, &quot;&quot;linkedin&quot;&quot;. | 
**ProfileName** | **String** | Human-readable profile name. | [optional] 
**ProfileUrl** | **String** | Link to profile. | 

## Examples

- Prepare the resource
```powershell
$SocialNetwork = Initialize-PSOpenAPIToolsSocialNetwork  -Name null `
 -ProfileName null `
 -ProfileUrl null
```

- Convert the resource to JSON
```powershell
$SocialNetwork | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

