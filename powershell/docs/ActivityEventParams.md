# ActivityEventParams
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BodyContent** | **String** | The HTML content of the page body. | [optional] 
**DatasourceInstance** | **String** | The full datasource instance name inferred from the URL of the event | [optional] 
**Datasource** | **String** | The datasource without the instance inferred from the URL of the event | [optional] 
**InstanceOnlyName** | **String** | The instance only name of the datasource instance, e.g. 1 for jira_1, inferred from the URL of the event | [optional] 
**Duration** | **Int32** | Length in seconds of the activity. For VIEWS, this represents the amount the page was visible in the foreground. | [optional] 
**Query** | **String** | The user&#39;s search query associated with a SEARCH. | [optional] 
**Referrer** | **String** | The referring URL of the VIEW or SEARCH. | [optional] 
**Title** | **String** | The page title associated with the URL of the event | [optional] 
**Truncated** | **Boolean** | Indicates that the parameters are incomplete and more parameters may be sent with the same action+timestamp+URL in the future. This is used for sending the duration when a &#x60;VIEW&#x60; is finished. | [optional] 

## Examples

- Prepare the resource
```powershell
$ActivityEventParams = Initialize-PSOpenAPIToolsActivityEventParams  -BodyContent null `
 -DatasourceInstance null `
 -Datasource null `
 -InstanceOnlyName null `
 -Duration null `
 -Query null `
 -Referrer null `
 -Title null `
 -Truncated null
```

- Convert the resource to JSON
```powershell
$ActivityEventParams | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

