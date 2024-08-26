# CommentDefinition

Describes a comment on a document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The document specific id for the comment. This field is case insensitive and should not be more than 200 characters in length. | 
**author** | [**UserReferenceDefinition**](UserReferenceDefinition.md) |  | [optional] 
**content** | [**ContentDefinition**](ContentDefinition.md) |  | [optional] 
**created\_at** | **int** | The creation time, in epoch seconds. | [optional] 
**updated\_at** | **int** | The last updated time, in epoch seconds. | [optional] 
**updated\_by** | [**UserReferenceDefinition**](UserReferenceDefinition.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


