# ListPinsResponse
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Pins** | [**PinDocument[]**](PinDocument.md) | List of pinned documents. | 

## Examples

- Prepare the resource
```powershell
$ListPinsResponse = Initialize-PSOpenAPIToolsListPinsResponse  -Pins null
```

- Convert the resource to JSON
```powershell
$ListPinsResponse | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

