# glean\_indexing\_api\_client.DebugApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug\_datasource\_document\_post**](DebugApi.md#debug\_datasource\_document\_post) | **POST** /debug/{datasource}/document | Document status
[**debug\_datasource\_status\_post**](DebugApi.md#debug\_datasource\_status\_post) | **POST** /debug/{datasource}/status | Datasource status
[**debug\_datasource\_user\_post**](DebugApi.md#debug\_datasource\_user\_post) | **POST** /debug/{datasource}/user | User status


# **debug\_datasource\_document\_post**
> DebugDocumentResponse debug\_datasource\_document\_post(datasource, debug\_document\_request)

Document status

Gives various information that would help in debugging related to a particular document

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import debug_api
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
    api_instance = debug_api.DebugApi(api_client)
    datasource = "datasource_example" # str | The datasource to which the document belongs
    debug_document_request = DebugDocumentRequest(
        object_type="object_type_example",
        doc_id="doc_id_example",
    ) # DebugDocumentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Document status
        api_response = api_instance.debug_datasource_document_post(datasource, debug_document_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DebugApi->debug_datasource_document_post: %s\n" % e)
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

Datasource status

Get debug status for a datasource

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import debug_api
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
    api_instance = debug_api.DebugApi(api_client)
    datasource = "datasource_example" # str | The datasource to get debug status for

    # example passing only required values which don't have defaults set
    try:
        # Datasource status
        api_response = api_instance.debug_datasource_status_post(datasource)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DebugApi->debug_datasource_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The datasource to get debug status for |

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

User status

Gives various information that would help in debugging related to a particular user

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import debug_api
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
    api_instance = debug_api.DebugApi(api_client)
    datasource = "datasource_example" # str | The datasource to which the user belongs
    debug_user_request = DebugUserRequest(
        email="email_example",
    ) # DebugUserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # User status
        api_response = api_instance.debug_datasource_user_post(datasource, debug_user_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DebugApi->debug_datasource_user_post: %s\n" % e)
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

