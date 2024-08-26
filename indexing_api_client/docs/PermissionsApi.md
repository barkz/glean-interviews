# glean\_indexing\_api\_client.PermissionsApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**betausers\_post**](PermissionsApi.md#betausers\_post) | **POST** /betausers | Beta users
[**bulkindexgroups\_post**](PermissionsApi.md#bulkindexgroups\_post) | **POST** /bulkindexgroups | Bulk index groups
[**bulkindexmemberships\_post**](PermissionsApi.md#bulkindexmemberships\_post) | **POST** /bulkindexmemberships | Bulk index memberships for a group
[**bulkindexusers\_post**](PermissionsApi.md#bulkindexusers\_post) | **POST** /bulkindexusers | Bulk index users
[**deletegroup\_post**](PermissionsApi.md#deletegroup\_post) | **POST** /deletegroup | Delete group
[**deletemembership\_post**](PermissionsApi.md#deletemembership\_post) | **POST** /deletemembership | Delete membership
[**deleteuser\_post**](PermissionsApi.md#deleteuser\_post) | **POST** /deleteuser | Delete user
[**indexgroup\_post**](PermissionsApi.md#indexgroup\_post) | **POST** /indexgroup | Index group
[**indexmembership\_post**](PermissionsApi.md#indexmembership\_post) | **POST** /indexmembership | Index membership
[**indexuser\_post**](PermissionsApi.md#indexuser\_post) | **POST** /indexuser | Index user
[**processallmemberships\_post**](PermissionsApi.md#processallmemberships\_post) | **POST** /processallmemberships | Schedules the processing of group memberships


# **betausers\_post**
> betausers\_post(greenlist\_users\_request)

Beta users

Allow the datasource be visible to the specified beta users. The default behaviour is datasource being visible to all users if it is enabled and not visible to any user if it is not enabled.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.greenlist_users_request import GreenlistUsersRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    greenlist_users_request = GreenlistUsersRequest(
        datasource="datasource_example",
        emails=[
            "emails_example",
        ],
    ) # GreenlistUsersRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Beta users
        api_instance.betausers_post(greenlist_users_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->betausers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **greenlist\_users\_request** | [**GreenlistUsersRequest**](GreenlistUsersRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulkindexgroups\_post**
> bulkindexgroups\_post(bulk\_index\_groups\_request)

Bulk index groups

Replaces the groups in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.bulk_index_groups_request import BulkIndexGroupsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    bulk_index_groups_request = BulkIndexGroupsRequest(
        upload_id="upload_id_example",
        is_first_page=True,
        is_last_page=True,
        force_restart_upload=True,
        datasource="datasource_example",
        groups=[
            DatasourceGroupDefinition(
                name="name_example",
            ),
        ],
        disable_stale_data_deletion_check=True,
    ) # BulkIndexGroupsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index groups
        api_instance.bulkindexgroups_post(bulk_index_groups_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->bulkindexgroups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_groups\_request** | [**BulkIndexGroupsRequest**](BulkIndexGroupsRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulkindexmemberships\_post**
> bulkindexmemberships\_post(bulk\_index\_memberships\_request)

Bulk index memberships for a group

Replaces the memberships for a group in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.bulk_index_memberships_request import BulkIndexMembershipsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    bulk_index_memberships_request = BulkIndexMembershipsRequest(
        upload_id="upload_id_example",
        is_first_page=True,
        is_last_page=True,
        force_restart_upload=True,
        datasource="datasource_example",
        group="group_example",
        memberships=[
            DatasourceBulkMembershipDefinition(
                member_user_id="member_user_id_example",
                member_group_name="member_group_name_example",
            ),
        ],
    ) # BulkIndexMembershipsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index memberships for a group
        api_instance.bulkindexmemberships_post(bulk_index_memberships_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->bulkindexmemberships_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_memberships\_request** | [**BulkIndexMembershipsRequest**](BulkIndexMembershipsRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulkindexusers\_post**
> bulkindexusers\_post(bulk\_index\_users\_request)

Bulk index users

Replaces the users in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.bulk_index_users_request import BulkIndexUsersRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    bulk_index_users_request = BulkIndexUsersRequest(
        upload_id="upload_id_example",
        is_first_page=True,
        is_last_page=True,
        force_restart_upload=True,
        datasource="datasource_example",
        users=[
            DatasourceUserDefinition(
                email="email_example",
                user_id="user_id_example",
                name="name_example",
                is_active=True,
            ),
        ],
        disable_stale_data_deletion_check=True,
    ) # BulkIndexUsersRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index users
        api_instance.bulkindexusers_post(bulk_index_users_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->bulkindexusers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_users\_request** | [**BulkIndexUsersRequest**](BulkIndexUsersRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletegroup\_post**
> deletegroup\_post(delete\_group\_request)

Delete group

Delete group from the datasource. Silently succeeds if group is not present.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.delete_group_request import DeleteGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    delete_group_request = DeleteGroupRequest(
        version=1,
        datasource="datasource_example",
        group_name="group_name_example",
    ) # DeleteGroupRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete group
        api_instance.deletegroup_post(delete_group_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->deletegroup_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_group\_request** | [**DeleteGroupRequest**](DeleteGroupRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletemembership\_post**
> deletemembership\_post(delete\_membership\_request)

Delete membership

Delete membership to a group in the specified datasource. Silently succeeds if membership is not present.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.delete_membership_request import DeleteMembershipRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    delete_membership_request = DeleteMembershipRequest(
        version=1,
        datasource="datasource_example",
        membership=DatasourceMembershipDefinition(
            group_name="group_name_example",
            member_user_id="member_user_id_example",
            member_group_name="member_group_name_example",
        ),
    ) # DeleteMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete membership
        api_instance.deletemembership_post(delete_membership_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->deletemembership_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_membership\_request** | [**DeleteMembershipRequest**](DeleteMembershipRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteuser\_post**
> deleteuser\_post(delete\_user\_request)

Delete user

Delete the user from the datasource. Silently succeeds if user is not present.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.delete_user_request import DeleteUserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    delete_user_request = DeleteUserRequest(
        version=1,
        datasource="datasource_example",
        email="email_example",
    ) # DeleteUserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.deleteuser_post(delete_user_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->deleteuser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_user\_request** | [**DeleteUserRequest**](DeleteUserRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexgroup\_post**
> indexgroup\_post(index\_group\_request)

Index group

Add or update a group in the datasource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.index_group_request import IndexGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    index_group_request = IndexGroupRequest(
        version=1,
        datasource="datasource_example",
        group=DatasourceGroupDefinition(
            name="name_example",
        ),
    ) # IndexGroupRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index group
        api_instance.indexgroup_post(index_group_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->indexgroup_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_group\_request** | [**IndexGroupRequest**](IndexGroupRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexmembership\_post**
> indexmembership\_post(index\_membership\_request)

Index membership

Add the memberships of a group in the datasource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.index_membership_request import IndexMembershipRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    index_membership_request = IndexMembershipRequest(
        version=1,
        datasource="datasource_example",
        membership=DatasourceMembershipDefinition(
            group_name="group_name_example",
            member_user_id="member_user_id_example",
            member_group_name="member_group_name_example",
        ),
    ) # IndexMembershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index membership
        api_instance.indexmembership_post(index_membership_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->indexmembership_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_membership\_request** | [**IndexMembershipRequest**](IndexMembershipRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexuser\_post**
> indexuser\_post(index\_user\_request)

Index user

Adds a datasource user or updates an existing user.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.index_user_request import IndexUserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    index_user_request = IndexUserRequest(
        version=1,
        datasource="datasource_example",
        user=DatasourceUserDefinition(
            email="email_example",
            user_id="user_id_example",
            name="name_example",
            is_active=True,
        ),
    ) # IndexUserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index user
        api_instance.indexuser_post(index_user_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->indexuser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_user\_request** | [**IndexUserRequest**](IndexUserRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processallmemberships\_post**
> processallmemberships\_post()

Schedules the processing of group memberships

Schedules the immediate processing of all group memberships uploaded through the indexing API. By default the uploaded group memberships will be processed asynchronously but this API can be used to schedule processing of all memberships on demand. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import permissions_api
from glean_indexing_api_client.model.process_all_memberships_request import ProcessAllMembershipsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://domain-be.glean.com/api/index/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = glean_indexing_api_client.Configuration(
    host = "https://domain-be.glean.com/api/index/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = glean_indexing_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with glean_indexing_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permissions_api.PermissionsApi(api_client)
    process_all_memberships_request = ProcessAllMembershipsRequest(
        datasource="datasource_example",
    ) # ProcessAllMembershipsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedules the processing of group memberships
        api_instance.processallmemberships_post(process_all_memberships_request=process_all_memberships_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PermissionsApi->processallmemberships_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process\_all\_memberships\_request** | [**ProcessAllMembershipsRequest**](ProcessAllMembershipsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

