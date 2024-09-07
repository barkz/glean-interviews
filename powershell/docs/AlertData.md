# AlertData
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | The name of the admin alert | [optional] 
**TriggeredTime** | **System.DateTime** | The time that the alert was triggered | [optional] 
**ProjectName** | **String** | Human readable name of the project instance | [optional] 
**HelpLink** | **String** | Help link for the alert that the admin can reference | [optional] 
**Datasource** | **String** | Datasource that the alert is related to (possibly null) | [optional] 
**BannerType** | **String** | Banner type to display for this alert | [optional] 
**BannerText** | **String** | Text to display for the alert banner | [optional] 
**AlertDescription** | **String** | Text for what happened section of an admin alert. | [optional] 
**RelevanceDescription** | **String** | Text for why this matters section of an admin alert. | [optional] 
**ResolutionStepsDescription** | **String** | Text for to do section before actual steps. | [optional] 
**ResolutionSteps** | [**ResolutionStep[]**](ResolutionStep.md) | Steps to take to resolve an alert which are optionally mapped to a link for instructions (e.g. help doc) | [optional] 
**InstanceDisplayName** | **String** | datasource instance&#39;s user set display name | [optional] 
**InstanceName** | **String** | datsource instance&#39;s name e.g. confluence_0a0odwv | [optional] 

## Examples

- Prepare the resource
```powershell
$AlertData = Initialize-PSOpenAPIToolsAlertData  -Name null `
 -TriggeredTime null `
 -ProjectName null `
 -HelpLink null `
 -Datasource null `
 -BannerType null `
 -BannerText null `
 -AlertDescription null `
 -RelevanceDescription null `
 -ResolutionStepsDescription null `
 -ResolutionSteps null `
 -InstanceDisplayName null `
 -InstanceName null
```

- Convert the resource to JSON
```powershell
$AlertData | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

