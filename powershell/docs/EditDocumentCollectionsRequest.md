# EditDocumentCollectionsRequest
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AddedCollections** | **Int32[]** | IDs of Collections to which a document is added. | [optional] 
**RemovedCollections** | **Int32[]** | IDs of Collections from which a document is removed. | [optional] 
**DocumentId** | **String** | The Glean Document ID of the item being added to or removed from Collections if it&#39;s an indexed document. | [optional] 
**Url** | **String** | The URL of the item being added to or removed from Collections. | [optional] 
**Name** | **String** | Custom title of the document if adding a non-indexed URL. | [optional] 
**Description** | **String** | The description of this CollectionItem. | [optional] 

## Examples

- Prepare the resource
```powershell
$EditDocumentCollectionsRequest = Initialize-PSOpenAPIToolsEditDocumentCollectionsRequest  -AddedCollections null `
 -RemovedCollections null `
 -DocumentId null `
 -Url null `
 -Name null `
 -Description null
```

- Convert the resource to JSON
```powershell
$EditDocumentCollectionsRequest | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

