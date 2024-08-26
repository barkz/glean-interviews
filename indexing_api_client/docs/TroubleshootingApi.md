# glean\_indexing\_api\_client.TroubleshootingApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkdocumentaccess\_post**](TroubleshootingApi.md#checkdocumentaccess\_post) | **POST** /checkdocumentaccess | Check document access
[**debug\_datasource\_document\_post**](TroubleshootingApi.md#debug\_datasource\_document\_post) | **POST** /debug/{datasource}/document | Beta: Get document information 
[**debug\_datasource\_status\_post**](TroubleshootingApi.md#debug\_datasource\_status\_post) | **POST** /debug/{datasource}/status | Beta: Get datasource status 
[**debug\_datasource\_user\_post**](TroubleshootingApi.md#debug\_datasource\_user\_post) | **POST** /debug/{datasource}/user | Beta: Get user information 
[**getdocumentcount\_post**](TroubleshootingApi.md#getdocumentcount\_post) | **POST** /getdocumentcount | Get document count
[**getdocumentstatus\_post**](TroubleshootingApi.md#getdocumentstatus\_post) | **POST** /getdocumentstatus | Get document upload and indexing status
[**getusercount\_post**](TroubleshootingApi.md#getusercount\_post) | **POST** /getusercount | Get user count
[**update\_datasource\_extenddeletionpaused\_post**](TroubleshootingApi.md#update\_datasource\_extenddeletionpaused\_post) | **POST** /update/{datasource}/extenddeletionpaused | Extends a deletion paused event for a datasource
[**update\_datasource\_resolvedeletionpaused\_post**](TroubleshootingApi.md#update\_datasource\_resolvedeletionpaused\_post) | **POST** /update/{datasource}/resolvedeletionpaused | Resolves a deletion paused event


# **checkdocumentaccess\_post**
> CheckDocumentAccessResponse checkdocumentaccess\_post(check\_document\_access\_request)

Check document access

Check if a given user has access to access a document in a custom datasource  Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/) for more information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.check_document_access_request import CheckDocumentAccessRequest
from glean_indexing_api_client.model.check_document_access_response import CheckDocumentAccessResponse
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    check_document_access_request = CheckDocumentAccessRequest(
        datasource="datasource_example",
        object_type="object_type_example",
        doc_id="doc_id_example",
        user_email="user_email_example",
    ) # CheckDocumentAccessRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Check document access
        api_response = api_instance.checkdocumentaccess_post(check_document_access_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->checkdocumentaccess_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check\_document\_access\_request** | [**CheckDocumentAccessRequest**](CheckDocumentAccessRequest.md)|  |

### Return type

[**CheckDocumentAccessResponse**](CheckDocumentAccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug\_datasource\_document\_post**
> DebugDocumentResponse debug\_datasource\_document\_post(datasource, debug\_document\_request)

Beta: Get document information 

Gives various information that would help in debugging related to a particular document. Currently in beta, might undergo breaking changes without prior notice.  Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/) for more information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.debug_document_response import DebugDocumentResponse
from glean_indexing_api_client.model.debug_document_request import DebugDocumentRequest
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    datasource = "datasource_example" # str | The datasource to which the document belongs
    debug_document_request = DebugDocumentRequest(
        object_type="Article",
        doc_id="art123",
    ) # DebugDocumentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Beta: Get document information 
        api_response = api_instance.debug_datasource_document_post(datasource, debug_document_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->debug_datasource_document_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource to which the document belongs |
 **debug\_document\_request** | [**DebugDocumentRequest**](DebugDocumentRequest.md)|  |

### Return type

[**DebugDocumentResponse**](DebugDocumentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug\_datasource\_status\_post**
> DebugDatasourceStatusResponse debug\_datasource\_status\_post(datasource)

Beta: Get datasource status 

Gather information about the datasource's overall status. Currently in beta, might undergo breaking changes without prior notice.  Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/) for more information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.debug_datasource_status_response import DebugDatasourceStatusResponse
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    datasource = "datasource_example" # str | The datasource to get debug status for.

    # example passing only required values which don't have defaults set
    try:
        # Beta: Get datasource status 
        api_response = api_instance.debug_datasource_status_post(datasource)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->debug_datasource_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource to get debug status for. |

### Return type

[**DebugDatasourceStatusResponse**](DebugDatasourceStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug\_datasource\_user\_post**
> DebugUserResponse debug\_datasource\_user\_post(datasource, debug\_user\_request)

Beta: Get user information 

Gives various information that would help in debugging related to a particular user. Currently in beta, might undergo breaking changes without prior notice.  Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/) for more information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.debug_user_request import DebugUserRequest
from glean_indexing_api_client.model.debug_user_response import DebugUserResponse
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    datasource = "datasource_example" # str | The datasource to which the user belongs
    debug_user_request = DebugUserRequest(
        email="u1@foo.com",
    ) # DebugUserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Beta: Get user information 
        api_response = api_instance.debug_datasource_user_post(datasource, debug_user_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->debug_datasource_user_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource to which the user belongs |
 **debug\_user\_request** | [**DebugUserRequest**](DebugUserRequest.md)|  |

### Return type

[**DebugUserResponse**](DebugUserResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdocumentcount\_post**
> GetDocumentCountResponse getdocumentcount\_post(get\_document\_count\_request)

Get document count

Fetches document count for the specified custom datasource.  Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/#debug-datasource-status) for richer information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.get_document_count_request import GetDocumentCountRequest
from glean_indexing_api_client.model.get_document_count_response import GetDocumentCountResponse
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    get_document_count_request = GetDocumentCountRequest(
        datasource="datasource_example",
    ) # GetDocumentCountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get document count
        api_response = api_instance.getdocumentcount_post(get_document_count_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->getdocumentcount_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get\_document\_count\_request** | [**GetDocumentCountRequest**](GetDocumentCountRequest.md)|  |

### Return type

[**GetDocumentCountResponse**](GetDocumentCountResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdocumentstatus\_post**
> GetDocumentStatusResponse getdocumentstatus\_post(get\_document\_status\_request)

Get document upload and indexing status

Intended for debugging/validation. Fetches the current upload and indexing status of documents.  Tip: Use [/debug/{datasource}/document](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/#debug-datasource-document) for richer information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.get_document_status_response import GetDocumentStatusResponse
from glean_indexing_api_client.model.get_document_status_request import GetDocumentStatusRequest
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    get_document_status_request = GetDocumentStatusRequest(
        datasource="datasource_example",
        object_type="object_type_example",
        doc_id="doc_id_example",
    ) # GetDocumentStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get document upload and indexing status
        api_response = api_instance.getdocumentstatus_post(get_document_status_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->getdocumentstatus_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get\_document\_status\_request** | [**GetDocumentStatusRequest**](GetDocumentStatusRequest.md)|  |

### Return type

[**GetDocumentStatusResponse**](GetDocumentStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getusercount\_post**
> GetUserCountResponse getusercount\_post(get\_user\_count\_request)

Get user count

Fetches user count for the specified custom datasource.  Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing\_api/indexing\_api\_troubleshooting/#debug-datasource-status) for richer information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.get_user_count_request import GetUserCountRequest
from glean_indexing_api_client.model.get_user_count_response import GetUserCountResponse
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    get_user_count_request = GetUserCountRequest(
        datasource="datasource_example",
    ) # GetUserCountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get user count
        api_response = api_instance.getusercount_post(get_user_count_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->getusercount_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get\_user\_count\_request** | [**GetUserCountRequest**](GetUserCountRequest.md)|  |

### Return type

[**GetUserCountResponse**](GetUserCountResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update\_datasource\_extenddeletionpaused\_post**
> update\_datasource\_extenddeletionpaused\_post(datasource)

Extends a deletion paused event for a datasource

After an upload completes, if indexing detects that more than 20% of existing documents would be deleted, we pause the deletion processes. This is referred to as a 'deletion pause event.' These events normally expire after a period of 7 days. You can use this endpoint to extend this period by up to an additional specified number of days.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
from glean_indexing_api_client.model.index_extend_deletion_paused_request import IndexExtendDeletionPausedRequest
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    datasource = "datasource_example" # str | The datasource instance
    index_extend_deletion_paused_request = IndexExtendDeletionPausedRequest(
        days=1,
    ) # IndexExtendDeletionPausedRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Extends a deletion paused event for a datasource
        api_instance.update_datasource_extenddeletionpaused_post(datasource)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->update_datasource_extenddeletionpaused_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extends a deletion paused event for a datasource
        api_instance.update_datasource_extenddeletionpaused_post(datasource, index_extend_deletion_paused_request=index_extend_deletion_paused_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->update_datasource_extenddeletionpaused_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource instance |
 **index\_extend\_deletion\_paused\_request** | [**IndexExtendDeletionPausedRequest**](IndexExtendDeletionPausedRequest.md)|  | [optional]

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

# **update\_datasource\_resolvedeletionpaused\_post**
> update\_datasource\_resolvedeletionpaused\_post(datasource)

Resolves a deletion paused event

After an upload completes, if indexing detects that more than 20% of existing documents would be deleted, we pause the deletion processes. This is referred to as a \"deletion pause event.\" These events normally expire after a period of 7 days. You can use this endpoint to resolve the \"deletion pause event\" and allow indexing and deletion to continue immediately.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import troubleshooting_api
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
    api_instance = troubleshooting_api.TroubleshootingApi(api_client)
    datasource = "datasource_example" # str | The datasource instance
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resolves a deletion paused event
        api_instance.update_datasource_resolvedeletionpaused_post(datasource)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->update_datasource_resolvedeletionpaused_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resolves a deletion paused event
        api_instance.update_datasource_resolvedeletionpaused_post(datasource, body=body)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling TroubleshootingApi->update_datasource_resolvedeletionpaused_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource instance |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none\_type)}**|  | [optional]

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

