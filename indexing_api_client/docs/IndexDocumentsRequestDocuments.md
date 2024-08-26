# IndexDocumentsRequestDocuments

Batch of documents being added/updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Document title, in plain text, if present. If not present, the title would be attempted to be extracted from the content. | [optional] 
**filename** | **str** | Source filename, in plain text, for the document. May be used as a fallback title for the document, if the title is not provided and cannot be extracted from the content. Populate this if there is no explicit title for the document and the content is sourced from a file. | [optional] 
**container** | **str** | The container name for the content (Folder for example for file content). | [optional] 
**container\_datasource\_id** | **str** | This represents the datasource sepcific id of the container. | [optional] 
**container\_object\_type** | **str** | This represents the object type of the container. It cannot have spaces or \_ | [optional] 
**object\_type** | **str** | The type of the document (Case, KnowledgeArticle for Salesforce for example). It cannot have spaces or \_ | [optional] 
**view\_url** | **str** | The permalink for viewing the document. **Note: viewURL is a required field for non-entity datasources, but not required if the datasource is used to push custom entities (ie. datasources where isEntityDatasource is false).**&#39;  | [optional] 
**id** | **str** | The datasource specific id for the document. This field is case insensitive and should not be more than 200 characters in length. | [optional] 
**summary** | [**ContentDefinition**](ContentDefinition.md) |  | [optional] 
**body** | [**ContentDefinition**](ContentDefinition.md) |  | [optional] 
**author** | [**UserReferenceDefinition**](UserReferenceDefinition.md) |  | [optional] 
**owner** | [**UserReferenceDefinition**](UserReferenceDefinition.md) |  | [optional] 
**permissions** | [**DocumentPermissionsDefinition**](DocumentPermissionsDefinition.md) |  | [optional] 
**created\_at** | **int** | The creation time, in epoch seconds. | [optional] 
**updated\_at** | **int** | The last update time, in epoch seconds. | [optional] 
**updated\_by** | [**UserReferenceDefinition**](UserReferenceDefinition.md) |  | [optional] 
**tags** | **[str]** | Labels associated with the document. | [optional] 
**interactions** | [**DocumentInteractionsDefinition**](DocumentInteractionsDefinition.md) |  | [optional] 
**status** | **str** |  | [optional] 
**additional\_urls** | **[str]** | Additional variations of the URL that this document points to. | [optional] 
**comments** | [**[CommentDefinition]**](CommentDefinition.md) | Comments associated with the document. | [optional] 
**custom\_properties** | [**[CustomProperty]**](CustomProperty.md) | Additional metadata properties of the document. These can surface as [facets and operators](https://developers.glean.com/docs/facets\_and\_operators\_for\_custom\_datasources/). | [optional] 
**datasource** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


