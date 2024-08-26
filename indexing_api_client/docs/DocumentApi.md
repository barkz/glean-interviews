# glean\_indexing\_api\_client.DocumentApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update\_datasource\_extenddeletionpaused\_post**](DocumentApi.md#update\_datasource\_extenddeletionpaused\_post) | **POST** /update/{datasource}/extenddeletionpaused | Extends a deletion paused event for a datasource
[**update\_datasource\_resolvedeletionpaused\_post**](DocumentApi.md#update\_datasource\_resolvedeletionpaused\_post) | **POST** /update/{datasource}/resolvedeletionpaused | Resolves a deletion paused event


# **update\_datasource\_extenddeletionpaused\_post**
> update\_datasource\_extenddeletionpaused\_post(datasource)

Extends a deletion paused event for a datasource

Extends a deletion paused event to prevent document deletion.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import document_api
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
    api_instance = document_api.DocumentApi(api_client)
    datasource = "datasource_example" # str | The datasource instance
    index_extend_deletion_paused_request = IndexExtendDeletionPausedRequest(
        days=1,
    ) # IndexExtendDeletionPausedRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Extends a deletion paused event for a datasource
        api_instance.update_datasource_extenddeletionpaused_post(datasource)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentApi->update_datasource_extenddeletionpaused_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extends a deletion paused event for a datasource
        api_instance.update_datasource_extenddeletionpaused_post(datasource, index_extend_deletion_paused_request=index_extend_deletion_paused_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentApi->update_datasource_extenddeletionpaused_post: %s\n" % e)
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

Resolves a deletion paused event and allows document deletion and publishing to continue.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import document_api
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
    api_instance = document_api.DocumentApi(api_client)
    datasource = "datasource_example" # str | The datasource instance
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resolves a deletion paused event
        api_instance.update_datasource_resolvedeletionpaused_post(datasource)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentApi->update_datasource_resolvedeletionpaused_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resolves a deletion paused event
        api_instance.update_datasource_resolvedeletionpaused_post(datasource, body=body)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentApi->update_datasource_resolvedeletionpaused_post: %s\n" % e)
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

