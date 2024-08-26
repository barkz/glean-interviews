# ObjectDefinition

The definition for an `DocumentMetadata.objectType` within a datasource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier for this &#x60;DocumentMetadata.objectType&#x60;. If omitted, this definition is used as a default for all unmatched &#x60;DocumentMetadata.objectType&#x60;s in this datasource. | [optional] 
**display\_label** | **str** | The user-friendly name of the object for display. | [optional] 
**doc\_category** | **str** | The document category of this object type. | [optional] 
**is\_container** | **bool** | Indicates whether the object type serves as a container (i.e parent to other objects), such as Channels in Slack or Folders in Google Drive. Defaults to false. | [optional] 
**property\_definitions** | [**[PropertyDefinition]**](PropertyDefinition.md) |  | [optional] 
**property\_groups** | [**[PropertyGroup]**](PropertyGroup.md) | A list of &#x60;PropertyGroup&#x60;s belonging to this object type, which will group properties to be displayed together in the UI. | [optional] 
**summarizable** | **bool** | Whether or not the object is summarizable | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


