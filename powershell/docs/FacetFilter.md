# FacetFilter
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FieldName** | **String** |  | [optional] 
**Values** | [**FacetFilterValue[]**](FacetFilterValue.md) | Within a single FacetFilter, the values are to be treated like an OR. For example, fieldName type with values [EQUALS Presentation, EQUALS Spreadsheet] means we want to show a document if it&#39;s a Presentation OR a Spreadsheet. | [optional] 
**GroupName** | **String** | Indicates the value of a facet, if any, that the given facet is grouped under. This is only used for nested facets, for example, fieldName could be owner and groupName would be Spreadsheet if showing all owners for spreadsheets as a nested facet. | [optional] 

## Examples

- Prepare the resource
```powershell
$FacetFilter = Initialize-PSOpenAPIToolsFacetFilter  -FieldName owner `
 -Values null `
 -GroupName Spreadsheet
```

- Convert the resource to JSON
```powershell
$FacetFilter | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

