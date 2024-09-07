# Summary
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Text** | **String** |  | [optional] 
**FollowUpPrompts** | **String[]** | Follow-up prompts based on the summarized doc | [optional] 

## Examples

- Prepare the resource
```powershell
$Summary = Initialize-PSOpenAPIToolsSummary  -Text null `
 -FollowUpPrompts null
```

- Convert the resource to JSON
```powershell
$Summary | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

