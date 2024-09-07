# FeedResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | **String** | Category of the result, one of the requested categories in incoming request. | 
**PrimaryEntry** | [**FeedEntry**](FeedEntry.md) |  | 
**SecondaryEntries** | [**FeedEntry[]**](FeedEntry.md) | Secondary entries for the result e.g. suggested docs for the calendar, carousel. | [optional] 
**Rank** | **Int32** | Rank of the result. Rank is suggested by server. Client side rank may differ. | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedResult = Initialize-PSOpenAPIToolsFeedResult  -Category null `
 -PrimaryEntry null `
 -SecondaryEntries null `
 -Rank null
```

- Convert the resource to JSON
```powershell
$FeedResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

