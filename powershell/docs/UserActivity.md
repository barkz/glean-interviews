# UserActivity
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Actor** | [**Person**](Person.md) |  | [optional] 
**Timestamp** | **Int32** | Unix timestamp of the activity (in seconds since epoch UTC). | [optional] 
**Action** | **String** | The action for the activity | [optional] 
**AggregateVisitCount** | [**CountInfo**](CountInfo.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$UserActivity = Initialize-PSOpenAPIToolsUserActivity  -Actor null `
 -Timestamp null `
 -Action null `
 -AggregateVisitCount null
```

- Convert the resource to JSON
```powershell
$UserActivity | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

