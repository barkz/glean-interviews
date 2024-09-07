# Customer
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **String** | Unique identifier. | 
**Domains** | **String[]** | Link to company&#39;s associated website domains. | [optional] 
**Company** | [**Company**](Company.md) |  | 
**DocumentCounts** | **System.Collections.Hashtable** | A map of {string, int} pairs representing counts of each document type associated with this customer. | [optional] 
**Poc** | [**Person[]**](Person.md) | A list of POC for company. | [optional] 
**Metadata** | [**CustomerMetadata**](CustomerMetadata.md) |  | [optional] 
**MergedCustomers** | [**Customer[]**](Customer.md) | A list of Customers. | [optional] 
**StartDate** | **System.DateTime** | The date when the interaction with customer started. | [optional] 
**ContractAnnualRevenue** | **Double** | Average contract annual revenue with that customer. | [optional] 
**Notes** | **String** | User facing (potentially generated) notes about company. | [optional] 

## Examples

- Prepare the resource
```powershell
$Customer = Initialize-PSOpenAPIToolsCustomer  -Id null `
 -Domains null `
 -Company null `
 -DocumentCounts null `
 -Poc null `
 -Metadata null `
 -MergedCustomers null `
 -StartDate null `
 -ContractAnnualRevenue null `
 -Notes CIO is interested in trying out the product.
```

- Convert the resource to JSON
```powershell
$Customer | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

