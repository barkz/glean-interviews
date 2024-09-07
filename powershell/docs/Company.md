# Company
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **String** | User-friendly display name. | 
**ProfileUrl** | **String** | Link to internal company company profile. | [optional] 
**WebsiteUrls** | **String[]** | Link to company&#39;s associated websites. | [optional] 
**LogoUrl** | **String** | The URL of the company&#39;s logo. Public, Glean-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**Location** | **String** | User facing string representing the company&#39;s location. | [optional] 
**Phone** | **String** | Phone number as a number string. | [optional] 
**Fax** | **String** | Fax number as a number string. | [optional] 
**Industry** | **String** | User facing string representing the company&#39;s industry. | [optional] 
**AnnualRevenue** | **Double** | Average company&#39;s annual revenue for reference. | [optional] 
**NumberOfEmployees** | **Int64** | Average company&#39;s number of employees for reference. | [optional] 
**StockSymbol** | **String** | Company&#39;s stock symbol if company is public. | [optional] 
**FoundedDate** | **System.DateTime** | The date when the company was founded. | [optional] 
**About** | **String** | User facing description of company. | [optional] 

## Examples

- Prepare the resource
```powershell
$Company = Initialize-PSOpenAPIToolsCompany  -Name null `
 -ProfileUrl null `
 -WebsiteUrls null `
 -LogoUrl null `
 -Location New York City `
 -Phone null `
 -Fax null `
 -Industry Finances `
 -AnnualRevenue null `
 -NumberOfEmployees null `
 -StockSymbol null `
 -FoundedDate null `
 -About Financial, software, data, and media company headquartered in Midtown Manhattan, New York City
```

- Convert the resource to JSON
```powershell
$Company | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

