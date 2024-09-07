# EmailRequestFeedbackPayload
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comments** | **String** | Additional freeform comments provided by the reporter. | [optional] 
**CustomJson** | **String** | Arbitrary email param payloads from 3P-customer widgets. Prefer the structured fields when possible. | [optional] 
**ImageUrls** | **String[]** | Images uploaded by the user when submitting feedback | [optional] 
**IssueType** | **String** | The type of issue being reported, e.g. RESULT_MISSING or OTHER for search feedback. | [optional] 
**Query** | **String** | The query the reporter tried when feedback was sent. | [optional] 
**TrackingToken** | **String** | The tracking token of the feedback that admins can provide Glean Support to debug | [optional] 
**Url** | **String** | The URL the reporter was on when feedback was sent. | [optional] 
**RatingKey** | **String** | The label of the rating that was selected when feedback was sent. | [optional] 

## Examples

- Prepare the resource
```powershell
$EmailRequestFeedbackPayload = Initialize-PSOpenAPIToolsEmailRequestFeedbackPayload  -Comments null `
 -CustomJson {&quot;comment&quot;: &quot;glean is awesome!&quot;, &quot;sender&quot;: &quot;happycustomer@customer.com&quot;} `
 -ImageUrls null `
 -IssueType null `
 -Query null `
 -TrackingToken null `
 -Url null `
 -RatingKey null
```

- Convert the resource to JSON
```powershell
$EmailRequestFeedbackPayload | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

