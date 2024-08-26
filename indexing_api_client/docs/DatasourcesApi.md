# glean\_indexing\_api\_client.DatasourcesApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adddatasource\_post**](DatasourcesApi.md#adddatasource\_post) | **POST** /adddatasource | Add or update datasource
[**getdatasourceconfig\_post**](DatasourcesApi.md#getdatasourceconfig\_post) | **POST** /getdatasourceconfig | Get datasource config


# **adddatasource\_post**
> adddatasource\_post(custom\_datasource\_config)

Add or update datasource

Add or update a custom datasource and its schema.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import datasources_api
from glean_indexing_api_client.model.custom_datasource_config import CustomDatasourceConfig
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
    api_instance = datasources_api.DatasourcesApi(api_client)
    custom_datasource_config = CustomDatasourceConfig(None) # CustomDatasourceConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Add or update datasource
        api_instance.adddatasource_post(custom_datasource_config)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DatasourcesApi->adddatasource_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom\_datasource\_config** | [**CustomDatasourceConfig**](CustomDatasourceConfig.md)|  |

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

# **getdatasourceconfig\_post**
> CustomDatasourceConfig getdatasourceconfig\_post(get\_datasource\_config\_request)

Get datasource config

Fetches the datasource config for the specified custom datasource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import datasources_api
from glean_indexing_api_client.model.get_datasource_config_request import GetDatasourceConfigRequest
from glean_indexing_api_client.model.custom_datasource_config import CustomDatasourceConfig
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
    api_instance = datasources_api.DatasourcesApi(api_client)
    get_datasource_config_request = GetDatasourceConfigRequest(
        datasource="datasource_example",
    ) # GetDatasourceConfigRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get datasource config
        api_response = api_instance.getdatasourceconfig_post(get_datasource_config_request)
        pprint(api_response)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DatasourcesApi->getdatasourceconfig_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get\_datasource\_config\_request** | [**GetDatasourceConfigRequest**](GetDatasourceConfigRequest.md)|  |

### Return type

[**CustomDatasourceConfig**](CustomDatasourceConfig.md)

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

