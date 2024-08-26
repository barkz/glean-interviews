# glean\_indexing\_api\_client.DocumentsApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkindexdocuments\_post**](DocumentsApi.md#bulkindexdocuments\_post) | **POST** /bulkindexdocuments | Bulk index documents
[**deletedocument\_post**](DocumentsApi.md#deletedocument\_post) | **POST** /deletedocument | Delete document
[**indexdocument\_post**](DocumentsApi.md#indexdocument\_post) | **POST** /indexdocument | Index document
[**indexdocuments\_post**](DocumentsApi.md#indexdocuments\_post) | **POST** /indexdocuments | Index documents
[**processalldocuments\_post**](DocumentsApi.md#processalldocuments\_post) | **POST** /processalldocuments | Schedules the processing of uploaded documents


# **bulkindexdocuments\_post**
> bulkindexdocuments\_post(bulk\_index\_documents\_request)

Bulk index documents

Replaces the documents in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import documents_api
from glean_indexing_api_client.model.bulk_index_documents_request import BulkIndexDocumentsRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    bulk_index_documents_request = BulkIndexDocumentsRequest() # BulkIndexDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index documents
        api_instance.bulkindexdocuments_post(bulk_index_documents_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->bulkindexdocuments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_documents\_request** | [**BulkIndexDocumentsRequest**](BulkIndexDocumentsRequest.md)|  |

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

# **deletedocument\_post**
> deletedocument\_post(delete\_document\_request)

Delete document

Deletes the specified document from the index. Succeeds if document is not present.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import documents_api
from glean_indexing_api_client.model.delete_document_request import DeleteDocumentRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    delete_document_request = DeleteDocumentRequest(
        version=1,
        datasource="datasource_example",
        object_type="object_type_example",
        id="id_example",
    ) # DeleteDocumentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete document
        api_instance.deletedocument_post(delete_document_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->deletedocument_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_document\_request** | [**DeleteDocumentRequest**](DeleteDocumentRequest.md)|  |

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

# **indexdocument\_post**
> indexdocument\_post(index\_document\_request)

Index document

Adds a document to the index or updates an existing document.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import documents_api
from glean_indexing_api_client.model.index_document_request import IndexDocumentRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    index_document_request = IndexDocumentRequest(
        version=1,
        document=DocumentDefinition(
            title="title_example",
            filename="filename_example",
            container="container_example",
            container_datasource_id="container_datasource_id_example",
            container_object_type="container_object_type_example",
            datasource="datasource_example",
            object_type="object_type_example",
            view_url="view_url_example",
            id="id_example",
            summary=ContentDefinition(
                mime_type="mime_type_example",
                text_content="text_content_example",
                binary_content="binary_content_example",
            ),
            body=ContentDefinition(
                mime_type="mime_type_example",
                text_content="text_content_example",
                binary_content="binary_content_example",
            ),
            author=UserReferenceDefinition(
                email="email_example",
                datasource_user_id="datasource_user_id_example",
                name="name_example",
            ),
            owner=UserReferenceDefinition(
                email="email_example",
                datasource_user_id="datasource_user_id_example",
                name="name_example",
            ),
            permissions=DocumentPermissionsDefinition(
                allowed_users=[
                    UserReferenceDefinition(
                        email="email_example",
                        datasource_user_id="datasource_user_id_example",
                        name="name_example",
                    ),
                ],
                allowed_groups=[
                    "allowed_groups_example",
                ],
                allowed_group_intersections=[
                    PermissionsGroupIntersectionDefinition(
                        required_groups=[
                            "required_groups_example",
                        ],
                    ),
                ],
                allow_anonymous_access=True,
                allow_all_datasource_users_access=True,
            ),
            created_at=1,
            updated_at=1,
            updated_by=UserReferenceDefinition(
                email="email_example",
                datasource_user_id="datasource_user_id_example",
                name="name_example",
            ),
            tags=[
                "tags_example",
            ],
            interactions=DocumentInteractionsDefinition(
                num_views=1,
                num_likes=1,
                num_comments=1,
            ),
            status="status_example",
            additional_urls=[
                "additional_urls_example",
            ],
            comments=[
                CommentDefinition(
                    id="id_example",
                    author=UserReferenceDefinition(
                        email="email_example",
                        datasource_user_id="datasource_user_id_example",
                        name="name_example",
                    ),
                    content=ContentDefinition(
                        mime_type="mime_type_example",
                        text_content="text_content_example",
                        binary_content="binary_content_example",
                    ),
                    created_at=1,
                    updated_at=1,
                    updated_by=UserReferenceDefinition(
                        email="email_example",
                        datasource_user_id="datasource_user_id_example",
                        name="name_example",
                    ),
                ),
            ],
            custom_properties=[
                CustomProperty(
                    name="name_example",
                    value=None,
                ),
            ],
        ),
    ) # IndexDocumentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index document
        api_instance.indexdocument_post(index_document_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->indexdocument_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_document\_request** | [**IndexDocumentRequest**](IndexDocumentRequest.md)|  |

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexdocuments\_post**
> indexdocuments\_post(index\_documents\_request)

Index documents

Adds or updates multiple documents in the index.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import documents_api
from glean_indexing_api_client.model.index_documents_request import IndexDocumentsRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    index_documents_request = IndexDocumentsRequest(
        upload_id="upload_id_example",
        datasource="datasource_example",
        documents=[
            DocumentDefinition(
                title="title_example",
                filename="filename_example",
                container="container_example",
                container_datasource_id="container_datasource_id_example",
                container_object_type="container_object_type_example",
                datasource="datasource_example",
                object_type="object_type_example",
                view_url="view_url_example",
                id="id_example",
                summary=ContentDefinition(
                    mime_type="mime_type_example",
                    text_content="text_content_example",
                    binary_content="binary_content_example",
                ),
                body=ContentDefinition(
                    mime_type="mime_type_example",
                    text_content="text_content_example",
                    binary_content="binary_content_example",
                ),
                author=UserReferenceDefinition(
                    email="email_example",
                    datasource_user_id="datasource_user_id_example",
                    name="name_example",
                ),
                owner=UserReferenceDefinition(
                    email="email_example",
                    datasource_user_id="datasource_user_id_example",
                    name="name_example",
                ),
                permissions=DocumentPermissionsDefinition(
                    allowed_users=[
                        UserReferenceDefinition(
                            email="email_example",
                            datasource_user_id="datasource_user_id_example",
                            name="name_example",
                        ),
                    ],
                    allowed_groups=[
                        "allowed_groups_example",
                    ],
                    allowed_group_intersections=[
                        PermissionsGroupIntersectionDefinition(
                            required_groups=[
                                "required_groups_example",
                            ],
                        ),
                    ],
                    allow_anonymous_access=True,
                    allow_all_datasource_users_access=True,
                ),
                created_at=1,
                updated_at=1,
                updated_by=UserReferenceDefinition(
                    email="email_example",
                    datasource_user_id="datasource_user_id_example",
                    name="name_example",
                ),
                tags=[
                    "tags_example",
                ],
                interactions=DocumentInteractionsDefinition(
                    num_views=1,
                    num_likes=1,
                    num_comments=1,
                ),
                status="status_example",
                additional_urls=[
                    "additional_urls_example",
                ],
                comments=[
                    CommentDefinition(
                        id="id_example",
                        author=UserReferenceDefinition(
                            email="email_example",
                            datasource_user_id="datasource_user_id_example",
                            name="name_example",
                        ),
                        content=ContentDefinition(
                            mime_type="mime_type_example",
                            text_content="text_content_example",
                            binary_content="binary_content_example",
                        ),
                        created_at=1,
                        updated_at=1,
                        updated_by=UserReferenceDefinition(
                            email="email_example",
                            datasource_user_id="datasource_user_id_example",
                            name="name_example",
                        ),
                    ),
                ],
                custom_properties=[
                    CustomProperty(
                        name="name_example",
                        value=None,
                    ),
                ],
            ),
        ],
    ) # IndexDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index documents
        api_instance.indexdocuments_post(index_documents_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->indexdocuments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_documents\_request** | [**IndexDocumentsRequest**](IndexDocumentsRequest.md)|  |

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processalldocuments\_post**
> processalldocuments\_post()

Schedules the processing of uploaded documents

Schedules the immediate processing of documents uploaded through the indexing API. By default the uploaded documents will be processed asynchronously but this API can be used to schedule processing of all documents on demand.  If a `datasource` parameter is specified, processing is limited to that custom datasource. Without it, processing applies to all documents across all custom datasources. #### Rate Limits This endpoint is rate-limited to one usage every 3 hours. Exceeding this limit results in a 429 response code. Here's how the rate limit works: 1. Calling `/processalldocuments` for datasource `foo` prevents another call for `foo` for 3 hours. 2. Calling `/processalldocuments` for datasource `foo` doesn't affect immediate calls for `bar`. 3. Calling `/processalldocuments` for all datasources prevents any datasource calls for 3 hours. 4. Calling `/processalldocuments` for datasource `foo` doesn't affect immediate calls for all datasources.  For more frequent document processing, contact Glean support. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import documents_api
from glean_indexing_api_client.model.process_all_documents_request import ProcessAllDocumentsRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    process_all_documents_request = ProcessAllDocumentsRequest(
        datasource="datasource_example",
    ) # ProcessAllDocumentsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedules the processing of uploaded documents
        api_instance.processalldocuments_post(process_all_documents_request=process_all_documents_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->processalldocuments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process\_all\_documents\_request** | [**ProcessAllDocumentsRequest**](ProcessAllDocumentsRequest.md)|  | [optional]

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

