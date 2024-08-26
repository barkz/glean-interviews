# glean\_indexing\_api\_client.PeopleApi

All URIs are relative to *https://domain-be.glean.com/api/index/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkindexemployees\_post**](PeopleApi.md#bulkindexemployees\_post) | **POST** /bulkindexemployees | Bulk index employees
[**bulkindexteams\_post**](PeopleApi.md#bulkindexteams\_post) | **POST** /bulkindexteams | Bulk index teams
[**deleteemployee\_post**](PeopleApi.md#deleteemployee\_post) | **POST** /deleteemployee | Delete employee
[**deleteteam\_post**](PeopleApi.md#deleteteam\_post) | **POST** /deleteteam | Delete team
[**indexemployee\_post**](PeopleApi.md#indexemployee\_post) | **POST** /indexemployee | Index employee
[**indexemployeelist\_post**](PeopleApi.md#indexemployeelist\_post) | **POST** /indexemployeelist | Bulk index employees
[**indexteam\_post**](PeopleApi.md#indexteam\_post) | **POST** /indexteam | Index team
[**processallemployeesandteams\_post**](PeopleApi.md#processallemployeesandteams\_post) | **POST** /processallemployeesandteams | Schedules the processing of uploaded employees and teams


# **bulkindexemployees\_post**
> bulkindexemployees\_post(bulk\_index\_employees\_request)

Bulk index employees

Replaces all the currently indexed employees using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.bulk_index_employees_request import BulkIndexEmployeesRequest
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
    api_instance = people_api.PeopleApi(api_client)
    bulk_index_employees_request = BulkIndexEmployeesRequest() # BulkIndexEmployeesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index employees
        api_instance.bulkindexemployees_post(bulk_index_employees_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->bulkindexemployees_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_employees\_request** | [**BulkIndexEmployeesRequest**](BulkIndexEmployeesRequest.md)|  |

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

# **bulkindexteams\_post**
> bulkindexteams\_post(bulk\_index\_teams\_request)

Bulk index teams

Replaces all the currently indexed teams using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing\_api\_bulk\_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.bulk_index_teams_request import BulkIndexTeamsRequest
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
    api_instance = people_api.PeopleApi(api_client)
    bulk_index_teams_request = BulkIndexTeamsRequest() # BulkIndexTeamsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index teams
        api_instance.bulkindexteams_post(bulk_index_teams_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->bulkindexteams_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk\_index\_teams\_request** | [**BulkIndexTeamsRequest**](BulkIndexTeamsRequest.md)|  |

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

# **deleteemployee\_post**
> deleteemployee\_post(delete\_employee\_request)

Delete employee

Delete an employee. Silently succeeds if employee is not present.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.delete_employee_request import DeleteEmployeeRequest
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
    api_instance = people_api.PeopleApi(api_client)
    delete_employee_request = DeleteEmployeeRequest(
        version=1,
        employee_email="employee_email_example",
    ) # DeleteEmployeeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete employee
        api_instance.deleteemployee_post(delete_employee_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->deleteemployee_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_employee\_request** | [**DeleteEmployeeRequest**](DeleteEmployeeRequest.md)|  |

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

# **deleteteam\_post**
> deleteteam\_post(delete\_team\_request)

Delete team

Delete a team based on provided id.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.delete_team_request import DeleteTeamRequest
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
    api_instance = people_api.PeopleApi(api_client)
    delete_team_request = DeleteTeamRequest(
        id="id_example",
    ) # DeleteTeamRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete team
        api_instance.deleteteam_post(delete_team_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->deleteteam_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete\_team\_request** | [**DeleteTeamRequest**](DeleteTeamRequest.md)|  |

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

# **indexemployee\_post**
> indexemployee\_post(index\_employee\_request)

Index employee

Adds an employee or updates information about an employee

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.index_employee_request import IndexEmployeeRequest
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
    api_instance = people_api.PeopleApi(api_client)
    index_employee_request = IndexEmployeeRequest(
        employee=EmployeeInfoDefinition(
            email="email_example",
            first_name="first_name_example",
            last_name="last_name_example",
            preferred_name="preferred_name_example",
            id="id_example",
            phone_number="phone_number_example",
            location="location_example",
            structured_location=StructuredLocation(
                desk_location="desk_location_example",
                timezone="timezone_example",
                address="address_example",
                city="city_example",
                state="state_example",
                region="region_example",
                zip_code="zip_code_example",
                country="country_example",
                country_code="country_code_example",
            ),
            title="title_example",
            photo_url="photo_url_example",
            business_unit="business_unit_example",
            department="department_example",
            datasource_profiles=[
                DatasourceProfile(None),
            ],
            teams=[
                EmployeeTeamInfo(
                    id="id_example",
                    name="name_example",
                    url="url_example",
                ),
            ],
            start_date=dateutil_parser('1970-01-01').date(),
            end_date=dateutil_parser('1970-01-01').date(),
            bio="bio_example",
            pronoun="pronoun_example",
            also_known_as=[
                "also_known_as_example",
            ],
            profile_url="profile_url_example",
            social_networks=[
                SocialNetworkDefinition(
                    name="name_example",
                    profile_name="profile_name_example",
                    profile_url="profile_url_example",
                ),
            ],
            manager_email="manager_email_example",
            manager_id="manager_id_example",
            type="FULL_TIME",
            relationships=[
                EntityRelationship(
                    name="name_example",
                    email="email_example",
                ),
            ],
            status="CURRENT",
            additional_fields=[
                AdditionalFieldDefinition(
                    key="key_example",
                    value=[
                        {},
                    ],
                ),
            ],
        ),
        version=1,
    ) # IndexEmployeeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index employee
        api_instance.indexemployee_post(index_employee_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->indexemployee_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_employee\_request** | [**IndexEmployeeRequest**](IndexEmployeeRequest.md)|  |

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

# **indexemployeelist\_post**
> indexemployeelist\_post(index\_employee\_list\_request)

Bulk index employees

Bulk upload details of all the employees. This deletes all employees uploaded in the prior batch. SOON TO BE DEPRECATED in favor of /bulkindexemployees.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.index_employee_list_request import IndexEmployeeListRequest
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
    api_instance = people_api.PeopleApi(api_client)
    index_employee_list_request = IndexEmployeeListRequest(
        employees=[
            IndexEmployeeRequest(
                employee=EmployeeInfoDefinition(
                    email="email_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    preferred_name="preferred_name_example",
                    id="id_example",
                    phone_number="phone_number_example",
                    location="location_example",
                    structured_location=StructuredLocation(
                        desk_location="desk_location_example",
                        timezone="timezone_example",
                        address="address_example",
                        city="city_example",
                        state="state_example",
                        region="region_example",
                        zip_code="zip_code_example",
                        country="country_example",
                        country_code="country_code_example",
                    ),
                    title="title_example",
                    photo_url="photo_url_example",
                    business_unit="business_unit_example",
                    department="department_example",
                    datasource_profiles=[
                        DatasourceProfile(None),
                    ],
                    teams=[
                        EmployeeTeamInfo(
                            id="id_example",
                            name="name_example",
                            url="url_example",
                        ),
                    ],
                    start_date=dateutil_parser('1970-01-01').date(),
                    end_date=dateutil_parser('1970-01-01').date(),
                    bio="bio_example",
                    pronoun="pronoun_example",
                    also_known_as=[
                        "also_known_as_example",
                    ],
                    profile_url="profile_url_example",
                    social_networks=[
                        SocialNetworkDefinition(
                            name="name_example",
                            profile_name="profile_name_example",
                            profile_url="profile_url_example",
                        ),
                    ],
                    manager_email="manager_email_example",
                    manager_id="manager_id_example",
                    type="FULL_TIME",
                    relationships=[
                        EntityRelationship(
                            name="name_example",
                            email="email_example",
                        ),
                    ],
                    status="CURRENT",
                    additional_fields=[
                        AdditionalFieldDefinition(
                            key="key_example",
                            value=[
                                {},
                            ],
                        ),
                    ],
                ),
                version=1,
            ),
        ],
    ) # IndexEmployeeListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk index employees
        api_instance.indexemployeelist_post(index_employee_list_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->indexemployeelist_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_employee\_list\_request** | [**IndexEmployeeListRequest**](IndexEmployeeListRequest.md)|  |

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

# **indexteam\_post**
> indexteam\_post(index\_team\_request)

Index team

Adds a team or updates information about a team

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
from glean_indexing_api_client.model.index_team_request import IndexTeamRequest
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
    api_instance = people_api.PeopleApi(api_client)
    index_team_request = IndexTeamRequest(
        team=TeamInfoDefinition(
            id="id_example",
            name="name_example",
            description="description_example",
            business_unit="business_unit_example",
            department="department_example",
            photo_url="photo_url_example",
            external_link="external_link_example",
            emails=[
                TeamEmail(
                    email="email_example",
                    type="OTHER",
                ),
            ],
            datasource_profiles=[
                DatasourceProfile(None),
            ],
            members=[
                TeamMember(
                    email="email_example",
                    relationship="MEMBER",
                    join_date=dateutil_parser('1970-01-01').date(),
                ),
            ],
        ),
        version=1,
    ) # IndexTeamRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Index team
        api_instance.indexteam_post(index_team_request)
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->indexteam_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index\_team\_request** | [**IndexTeamRequest**](IndexTeamRequest.md)|  |

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

# **processallemployeesandteams\_post**
> processallemployeesandteams\_post()

Schedules the processing of uploaded employees and teams

Schedules the immediate processing of employees and teams uploaded through the indexing API. By default all uploaded people data will be processed asynchronously but this API can be used to schedule its processing on demand. 

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import glean_indexing_api_client
from glean_indexing_api_client.api import people_api
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
    api_instance = people_api.PeopleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Schedules the processing of uploaded employees and teams
        api_instance.processallemployeesandteams_post()
    except glean_indexing_api_client.ApiException as e:
        print("Exception when calling PeopleApi->processallemployeesandteams_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

