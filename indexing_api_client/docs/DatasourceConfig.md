# DatasourceConfig

Structure describing shared config properties of the datasource (including multi-instance support)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier of datasource instance to which this config applies. | 
**display\_name** | **str** | The user-friendly instance label to display. If omitted, falls back to the title-cased &#x60;name&#x60;. | [optional] 
**datasource\_category** | **str** | The type of this datasource. It is an important signal for relevance and must be specified and cannot be UNCATEGORIZED. Please refer to [this](https://developers.glean.com/docs/indexing\_api\_datasource\_category/) for more details. | [optional]  if omitted the server will use the default value of "UNCATEGORIZED"
**url\_regex** | **str** | Regular expression that matches URLs of documents of the datasource instance. The behavior for multiple matches is non-deterministic. **Note: &#x60;urlRegex&#x60; is a required field for non-entity datasources, but not required if the datasource is used to push custom entities (ie. datasources where isEntityDatasource is false). Please add a regex as specific as possible to this datasource instance.** | [optional] 
**icon\_url** | **str** | The URL to an image to be displayed as an icon for this datasource instance. Must have a transparency mask. SVG are recommended over PNG. Public, scio-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**object\_definitions** | [**[ObjectDefinition]**](ObjectDefinition.md) | The list of top-level &#x60;objectType&#x60;s for the datasource. | [optional] 
**suggestion\_text** | **str** | Example text for what to search for in this datasource | [optional] 
**home\_url** | **str** | The URL of the landing page for this datasource instance. Should point to the most useful page for users, not the company marketing page. | [optional] 
**crawler\_seed\_urls** | **[str]** | This only applies to WEB\_CRAWL and BROWSER\_CRAWL datasources. Defines the seed URLs for crawling. | [optional] 
**icon\_dark\_url** | **str** | The URL to an image to be displayed as an icon for this datasource instance in dark mode. Must have a transparency mask. SVG are recommended over PNG. Public, scio-authenticated and Base64 encoded data URLs are all valid (but not third-party-authenticated URLs). | [optional] 
**hide\_built\_in\_facets** | **[str]** | List of built-in facet types that should be hidden for the datasource. | [optional] 
**canonicalizing\_url\_regex** | [**[CanonicalizingRegexType]**](CanonicalizingRegexType.md) | A list of regular expressions to apply to an arbitrary URL to transform it into a canonical URL for this datasource instance. Regexes are to be applied in the order specified in this list. | [optional] 
**canonicalizing\_title\_regex** | [**[CanonicalizingRegexType]**](CanonicalizingRegexType.md) | A list of regular expressions to apply to an arbitrary title to transform it into a title that will be displayed in the search results | [optional] 
**redlist\_title\_regex** | **str** | A regex that identifies titles that should not be indexed | [optional] 
**connector\_type** | [**ConnectorType**](ConnectorType.md) |  | [optional] 
**quicklinks** | [**[Quicklink]**](Quicklink.md) | List of actions for this datasource instance that will show up in autocomplete and app card, e.g. \&quot;Create new issue\&quot; for jira | [optional] 
**render\_config\_preset** | **str** | The name of a render config to use for displaying results from this datasource. Any well known datasource name may be used to render the same as that source, e.g. &#x60;web&#x60; or &#x60;gdrive&#x60;. Please refer to [this](https://developers.glean.com/docs/rendering\_search\_results/) for more details | [optional] 
**aliases** | **[str]** | Aliases that can be used as &#x60;app&#x60; operator-values. | [optional] 
**is\_on\_prem** | **bool** | Whether or not this datasource is hosted on-premise. | [optional] 
**trust\_url\_regex\_for\_view\_activity** | **bool** | True if browser activity is able to report the correct URL for VIEW events. Set this to true if the URLs reported by Chrome are constant throughout each page load. Set this to false if the page has Javascript that modifies the URL during or after the load. | [optional]  if omitted the server will use the default value of True
**include\_utm\_source** | **bool** | If true, a utm\_source query param will be added to outbound links to this datasource within Glean. | [optional] 
**strip\_fragment\_in\_canonical\_url** | **bool** | If true, the fragment part of the URL will be stripped when converting to a canonical url. | [optional]  if omitted the server will use the default value of True
**datasource\_name** | **str** | The (non-unique) name of the datasource of which this config is an instance, e.g. \&quot;jira\&quot;. | [optional] 
**instance\_only\_name** | **str** | The instance of the datasource for this particular config, e.g. \&quot;onprem\&quot;. | [optional] 
**instance\_description** | **str** | A human readable string identifying this instance as compared to its peers, e.g. \&quot;github.com/askscio\&quot; or \&quot;github.askscio.com\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


