# RotateTokenResponse

Describes the response body of the /rotatetoken API call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw\_secret** | **str** | New raw secret | [optional] 
**created\_at** | **int** | Unix timestamp in seconds when the new secret value is assigned to the token. The token needs to be rotated before &#x60;rotationPeriodMinutes&#x60; past the createdAt timestamp otherwise it would be rendered unusable. | [optional] 
**rotation\_period\_minutes** | **int** | Refers to the time period in minutes before which this token needs to be rotated. It is required to rotate the token within the specified &#x60;rotationPeriodMinutes&#x60; after each &#x60;/rotatetoken&#x60; call, otherwise the tokens would expire. Note that the token would still expire at &#x60;expiresAt&#x60; timestamp provided during token creation even if the token is being regularly rotated. &#x60;rotationPeriodMinutes&#x60; property is inherited from the parent token being rotated | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


