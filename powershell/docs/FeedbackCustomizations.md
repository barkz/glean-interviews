# FeedbackCustomizations
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DefaultChannels** | [**FeedbackChannel[]**](FeedbackChannel.md) | The channels to which feedback will be sent for any feature that does not have specific configuration. | [optional] 
**FeatureChannels** | [**System.Collections.Hashtable**](Array.md) | The channels to which feedback will be sent for individual features. The keys of the map will match the values in FeedbackFeature. Features not present in the map should use defaultChannels. | [optional] 
**Disclaimer** | **String** | A custom message shown to users during the in-product feedback flow, e.g. to warn users against sending sensitive or personally-identifying information. | [optional] 
**CompanyPrivacyPolicyLink** | **String** | An optional link to a privacy policy provided by the users&#39; company that will be shown to them during the in-product feedback flow if their company will receive their feedback. Glean&#39;s policy will also be shown if Glean is receiving the feedback. | [optional] 
**SupportMessage** | **String** | User visible text shown when seeking support to guide them to their company&#39;s internal support page when appropriate | [optional] 
**SupportLinkText** | **String** | User visible text that will link to the user&#39;s company&#39;s internal support page | [optional] 
**SupportLink** | **String** | URL to the user&#39;s company&#39;s internal suport page | [optional] 

## Examples

- Prepare the resource
```powershell
$FeedbackCustomizations = Initialize-PSOpenAPIToolsFeedbackCustomizations  -DefaultChannels null `
 -FeatureChannels null `
 -Disclaimer null `
 -CompanyPrivacyPolicyLink null `
 -SupportMessage null `
 -SupportLinkText null `
 -SupportLink null
```

- Convert the resource to JSON
```powershell
$FeedbackCustomizations | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

