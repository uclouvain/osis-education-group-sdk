# osis_education_group_sdk.GroupsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/education_group*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_read**](GroupsApi.md#groups_read) | **GET** /groups/{year}/{partial_acronym} | 
[**groups_tree**](GroupsApi.md#groups_tree) | **GET** /groups/{year}/{partial_acronym}/tree | 
[**groupstitle_read**](GroupsApi.md#groupstitle_read) | **GET** /groups/{year}/{partial_acronym}/title | 


# **groups_read**
> GroupDetailed groups_read(year, partial_acronym)



Return the detail of the group

### Example

* Api Key Authentication (Token):

```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import groups_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.group_detailed import GroupDetailed
from osis_education_group_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/education_group
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_education_group_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/education_group"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_education_group_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    year = "year_example" # str | 
    partial_acronym = "partial_acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.groups_read(year, partial_acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groups_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.groups_read(year, partial_acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groups_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **partial_acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**GroupDetailed**](GroupDetailed.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_tree**
> Tree groups_tree(year, partial_acronym)



Return the tree of the group

### Example

* Api Key Authentication (Token):

```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import groups_api
from osis_education_group_sdk.model.tree import Tree
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/education_group
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_education_group_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/education_group"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_education_group_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    year = "year_example" # str | 
    partial_acronym = "partial_acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.groups_tree(year, partial_acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groups_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.groups_tree(year, partial_acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groups_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **partial_acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Tree**](Tree.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupstitle_read**
> InlineResponse200 groupstitle_read(year, partial_acronym)



Return the title of the group

### Example

* Api Key Authentication (Token):

```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import groups_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.inline_response200 import InlineResponse200
from osis_education_group_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/education_group
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_education_group_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/education_group"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_education_group_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    year = 1 # int | 
    partial_acronym = "partial_acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.groupstitle_read(year, partial_acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groupstitle_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.groupstitle_read(year, partial_acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling GroupsApi->groupstitle_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **partial_acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

