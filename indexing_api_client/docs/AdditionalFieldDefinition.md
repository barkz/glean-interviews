# AdditionalFieldDefinition

Additional information about the employee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key to reference this field, e.g. \&quot;languages\&quot;. Note that the key should be all lowercase alphabetic characters with no numbers, spaces, hyphens or underscores. | [optional] 
**value** | **[{str: (bool, date, datetime, dict, float, int, list, str, none\_type)}]** | List of type string or HypertextField.  HypertextField is defined as &#x60;&#x60;&#x60; {   anchor: string,    // Anchor text for the hypertext field.   hyperlink: string, // URL for the hypertext field. } &#x60;&#x60;&#x60; Example: &#x60;&#x60;&#x60;{\&quot;anchor\&quot;:\&quot;Glean\&quot;,\&quot;hyperlink\&quot;:\&quot;https://glean.com\&quot;}&#x60;&#x60;&#x60;  When OpenAPI Generator supports oneOf, we will semantically enforce this in the docs.  **Note**: If using the Python SDK to pass in a list of strings, the value may need to be a list of dictionaries. In that case, the key in that dictionary will be ignored. Example: &#x60;&#x60;&#x60;\&quot;languages\&quot;: [{\&quot;lang\&quot;:\&quot;English\&quot;,\&quot;lang\&quot;:\&quot;Spanish\&quot;,...}]&#x60;&#x60;&#x60;. In this case, the key \&quot;lang\&quot; will be ignored and can even be passed in as an empty string.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


