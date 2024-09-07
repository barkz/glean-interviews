# SearchResultSnippet
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Snippet** | **String** | A matching snippet from the document. Query term matches are marked by the unicode characters uE006 and uE007. | 
**MimeType** | **String** | The mime type of the snippets, currently either text/plain or text/html. | [optional] 
**Text** | **String** | A matching snippet from the document with no highlights. | [optional] 
**SnippetTextOrdering** | **Int32** | Used for sorting based off the snippet&#39;s location within all_snippetable_text | [optional] 
**Ranges** | [**TextRange[]**](TextRange.md) | The bolded ranges within text. | [optional] 
**Url** | **String** | A URL, generated based on availability, that links to the position of the snippet text or to the nearest header above the snippet text. | [optional] 

## Examples

- Prepare the resource
```powershell
$SearchResultSnippet = Initialize-PSOpenAPIToolsSearchResultSnippet  -Snippet null `
 -MimeType null `
 -Text null `
 -SnippetTextOrdering null `
 -Ranges null `
 -Url null
```

- Convert the resource to JSON
```powershell
$SearchResultSnippet | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

