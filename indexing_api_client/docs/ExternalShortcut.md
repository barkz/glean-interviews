# ExternalShortcut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input\_alias** | **str** | link text following the viewPrefix as entered by the user. For example, if the view prefix is &#x60;go/&#x60; and the shortened URL is &#x60;go/abc&#x60;, then &#x60;abc&#x60; is the inputAlias. | 
**destination\_url** | **str** | destination URL for the shortcut. | 
**created\_by** | **str** | Email of the user who created this shortcut. | 
**title** | **str** | Title of the golink | [optional] 
**intermediate\_url** | **str** | The URL from which the user is then redirected to the destination URL. | [optional] 
**decayed\_visit\_score** | **float** | decayed visits score for ranking | [optional] 
**edit\_url** | **str** | The URL using which the user can access the edit page of the shortcut. | [optional] 
**description** | **str** | A short, plain text blurb to help people understand the intent of the shortcut. | [optional] 
**create\_time** | **int** | The time the shortcut was created in epoch seconds. | [optional] 
**updated\_by** | **str** | Email of the user who last updated this shortcut. | [optional] 
**update\_time** | **int** | The time the shortcut was updated in epoch seconds. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


