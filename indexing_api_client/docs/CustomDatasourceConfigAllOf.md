# CustomDatasourceConfigAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity\_datasource\_name** | **str** | If the datasource uses another datasource for identity info, then the name of the datasource. The identity datasource must exist already. | [optional] 
**product\_access\_group** | **str** | If the datasource uses a specific product access group, then the name of that group. | [optional] 
**is\_user\_referenced\_by\_email** | **bool** | whether email is used to reference users in document ACLs and in group memberships. | [optional] 
**is\_entity\_datasource** | **bool** | True if this datasource is used to push custom entities. | [optional]  if omitted the server will use the default value of False
**is\_test\_datasource** | **bool** | True if this datasource will be used for testing purpose only. Documents from such a datasource wouldn&#39;t have any effect on search rankings. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none\_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


