# AnswerLikes
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LikedBy** | [**AnswerLike[]**](AnswerLike.md) |  | 
**LikedByUser** | **Boolean** | Whether the user in context liked the answer. | 
**NumLikes** | **Int32** | The total number of likes for the answer. | 

## Examples

- Prepare the resource
```powershell
$AnswerLikes = Initialize-PSOpenAPIToolsAnswerLikes  -LikedBy null `
 -LikedByUser null `
 -NumLikes null
```

- Convert the resource to JSON
```powershell
$AnswerLikes | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

