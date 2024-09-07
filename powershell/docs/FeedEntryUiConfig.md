# FeedEntryUiConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Format** | **String** | defines how to render this particular displayable list card | [optional] 
**AdditionalFlags** | [**DisplayableListItemUIConfig**](DisplayableListItemUIConfig.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedEntryUiConfig = Initialize-PSOpenAPIToolsFeedEntryUiConfig  -Format null `
 -AdditionalFlags null
```

- Convert the resource to JSON
```powershell
$FeedEntryUiConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

