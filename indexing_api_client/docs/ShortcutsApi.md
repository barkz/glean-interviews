# glean\_indexing\_api\_client.ShortcutsApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkindexshortcuts\_post**](ShortcutsApi.md#bulkindexshortcuts\_post) | **POST** /bulkindexshortcuts | Bulk index external shortcuts
[**uploadshortcuts\_post**](ShortcutsApi.md#uploadshortcuts\_post) | **POST** /uploadshortcuts | Upload shortcuts


# **bulkindexshortcuts\_post**
> bulkindexshortcuts\_post(bulk\_index\_shortcuts\_request)

Bulk index external shortcuts

Replaces all the currently indexed shortcuts using paginated batch API calls. Note that this endpoint is used for indexing shortcuts not hosted by Glean. If you want to upload shortcuts that would be hosted by Glean, please use the `/uploadshortcuts` endpoint. For information on what you can do with Golinks, which are Glean-hosted shortcuts, please refer to [this](https://help.glean.com/en/articles/5628838-how-go-links-work) page.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import shortcuts_api
from glean_indexing_api_client.model.bulk_index_shortcuts_request import BulkIndexShortcutsRequest
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
    api_instance = shortcuts_api.ShortcutsApi(api_client)
    bulk_index_shortcuts_request = BulkIndexShortcutsRequest() # BulkIndexShortcutsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index external shortcuts
        api_instance.bulkindexshortcuts_post(bulk_index_shortcuts_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling ShortcutsApi->bulkindexshortcuts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_shortcuts\_request** | [**BulkIndexShortcutsRequest**](BulkIndexShortcutsRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploadshortcuts\_post**
> uploadshortcuts\_post(upload\_shortcuts\_request)

Upload shortcuts

Creates glean shortcuts for uploaded shortcuts info. Glean would host the shortcuts, and they can be managed in the knowledge tab once uploaded.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import shortcuts_api
from glean_indexing_api_client.model.upload_shortcuts_request import UploadShortcutsRequest
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
    api_instance = shortcuts_api.ShortcutsApi(api_client)
    upload_shortcuts_request = UploadShortcutsRequest() # UploadShortcutsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Upload shortcuts
        api_instance.uploadshortcuts_post(upload_shortcuts_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling ShortcutsApi->uploadshortcuts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload\_shortcuts\_request** | [**UploadShortcutsRequest**](UploadShortcutsRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

