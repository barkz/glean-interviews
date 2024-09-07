# GetCollectionResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Collection** | [**Collection**](Collection.md) |  | [optional] 
**RootCollection** | [**Collection**](Collection.md) |  | [optional] 
**TrackingToken** | **String** | An opaque token that represents this particular Collection. To be used for &#x60;/feedback&#x60; reporting. | [optional] 
**VarError** | [**CollectionError**](CollectionError.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$GetCollectionResponse = Initialize-PSOpenAPIToolsGetCollectionResponse  -Collection null `
 -RootCollection null `
 -TrackingToken null `
 -VarError null
```

- Convert the resource to JSON
```powershell
$GetCollectionResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

