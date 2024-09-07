# Reaction
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **String** |  | [optional] 
**Count** | **Int32** | The count of the reaction type on the document. | [optional] 
**Reactors** | [**Person[]**](Person.md) |  | [optional] 
**ReactedByViewer** | **Boolean** | Whether the user in context reacted with this type to the document. | [optional] 

## Examples

- Prepare the resource
```powershell
$Reaction = Initialize-PSOpenAPIToolsReaction  -Type null `
 -Count null `
 -Reactors null `
 -ReactedByViewer null
```

- Convert the resource to JSON
```powershell
$Reaction | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

