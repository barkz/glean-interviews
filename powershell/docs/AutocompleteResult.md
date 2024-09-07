# AutocompleteResult
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Result** | **String** |  | 
**Keywords** | **String[]** | A list of all possible keywords for given result. | [optional] 
**ResultType** | **String** |  | [optional] 
**Score** | **Decimal** | Higher indicates a more confident match. | [optional] 
**OperatorMetadata** | [**OperatorMetadata**](OperatorMetadata.md) |  | [optional] 
**Quicklink** | [**Quicklink**](Quicklink.md) |  | [optional] 
**Document** | [**Document**](Document.md) |  | [optional] 
**Url** | **String** |  | [optional] 
**StructuredResult** | [**StructuredResult**](StructuredResult.md) |  | [optional] 
**TrackingToken** | **String** | A token to be passed in /feedback events associated with this autocomplete result. | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | Subsections of the result string to which some special formatting should be applied (eg. bold) | [optional] 

## Examples

- Prepare the resource
```powershell
$AutocompleteResult = Initialize-PSOpenAPIToolsAutocompleteResult  -Result null `
 -Keywords null `
 -ResultType null `
 -Score null `
 -OperatorMetadata null `
 -Quicklink null `
 -Document null `
 -Url null `
 -StructuredResult null `
 -TrackingToken null `
 -Ranges null
```

- Convert the resource to JSON
```powershell
$AutocompleteResult | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

