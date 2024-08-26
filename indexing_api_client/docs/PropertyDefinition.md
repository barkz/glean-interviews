# PropertyDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the property in the &#x60;DocumentMetadata&#x60; (e.g. &#39;createTime&#39;, &#39;updateTime&#39;, &#39;author&#39;, &#39;container&#39;). In the future, this will support custom properties too. | [optional] 
**display\_label** | **str** | The user friendly label for the property. | [optional] 
**display\_label\_plural** | **str** | The user friendly label for the property that will be used if a plural context. | [optional] 
**property\_type** | **str** | The type of custom property - this governs the search and faceting behavior. Note that MULTIPICKLIST is not yet supported. | [optional] 
**ui\_options** | **str** |  | [optional] 
**hide\_ui\_facet** | **bool** | If true then the property will not show up as a facet in the UI. | [optional] 
**show\_ui\_facet** | **bool** | If true then the property will show up as a facet in the UI. This will be used for native datasources only. Eventually hideUiFacet will migrate to showUiFacet for custom datasources as well. | [optional] 
**ui\_facet\_order** | **int** | Will be used to set the order of facets in the UI, if present. If set for one facet, must be set for all non-hidden UI facets. Must take on an integer value from 1 (shown at the top) to N (shown last), where N is the number of non-hidden UI facets. These facets will be ordered below the built-in \&quot;Type\&quot; and \&quot;Tag\&quot; operators. | [optional] 
**skip\_indexing** | **bool** | If true then the property will not be indexed for retrieval and ranking. | [optional] 
**targetable** | **bool** | If true then the property can be used for targeting UGC like announcements. | [optional] 
**object\_property\_options** | [**[ObjectPropertyOptions]**](ObjectPropertyOptions.md) |  | [optional] 
**group** | **str** | The unique identifier of the &#x60;PropertyGroup&#x60; to which this property belongs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


