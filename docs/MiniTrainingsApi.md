# osis_education_group_sdk.MiniTrainingsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/education_group*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mini_training_prerequisites_official**](MiniTrainingsApi.md#mini_training_prerequisites_official) | **GET** /mini_trainings/{year}/{acronym}/prerequisites | 
[**mini_training_version**](MiniTrainingsApi.md#mini_training_version) | **GET** /mini_trainings/{year}/{acronym}/versions/{version_name} | 
[**minitraining_tree**](MiniTrainingsApi.md#minitraining_tree) | **GET** /mini_trainings/{year}/{acronym}/tree | 
[**minitraining_version_tree**](MiniTrainingsApi.md#minitraining_version_tree) | **GET** /mini_trainings/{year}/{acronym}/versions/{version_name}/tree | 
[**minitrainings_list**](MiniTrainingsApi.md#minitrainings_list) | **GET** /mini_trainings/ | 
[**minitrainings_offer_roots**](MiniTrainingsApi.md#minitrainings_offer_roots) | **GET** /mini_trainings/{year}/{acronym}/offer_roots | 
[**minitrainings_read**](MiniTrainingsApi.md#minitrainings_read) | **GET** /mini_trainings/{year}/{acronym} | 
[**minitrainings_title_version_read**](MiniTrainingsApi.md#minitrainings_title_version_read) | **GET** /mini_trainings/{year}/{acronym}/versions/{version_name}/title | 
[**minitrainingstitle_read**](MiniTrainingsApi.md#minitrainingstitle_read) | **GET** /mini_trainings/{year}/{acronym}/title | 


# **mini_training_prerequisites_official**
> ArrayOfProgramTreePrerequisites mini_training_prerequisites_official(year, acronym)



Return the prerequisites of the learning units of the mini-training (standard version)

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mini_training_prerequisites_official(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->mini_training_prerequisites_official: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.mini_training_prerequisites_official(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->mini_training_prerequisites_official: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ArrayOfProgramTreePrerequisites**](ArrayOfProgramTreePrerequisites.md)

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

# **mini_training_version**
> MiniTrainingDetailed mini_training_version(year, acronym, version_name)



Return the detail of the mini training version

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
from osis_education_group_sdk.model.mini_training_detailed import MiniTrainingDetailed
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    version_name = "version_name_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mini_training_version(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->mini_training_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.mini_training_version(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->mini_training_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **version_name** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**MiniTrainingDetailed**](MiniTrainingDetailed.md)

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

# **minitraining_tree**
> Tree minitraining_tree(year, acronym)



Return the tree of the mini-training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitraining_tree(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitraining_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitraining_tree(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitraining_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
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

# **minitraining_version_tree**
> Tree minitraining_version_tree(year, acronym, version_name)



Return the tree of the version

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    version_name = "version_name_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitraining_version_tree(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitraining_version_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitraining_version_tree(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitraining_version_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **version_name** | **str**|  |
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

# **minitrainings_list**
> PaginatedMiniTraining minitrainings_list()



Return a list of all the mini_trainings with optional filtering.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.error import Error
from osis_education_group_sdk.model.paginated_mini_training import PaginatedMiniTraining
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    acronym = "acronym_example" # str |  (optional)
    code = "code_example" # str |  (optional)
    title = "title_example" # str |  (optional)
    from_year = 1 # int |  (optional)
    to_year = 1 # int |  (optional)
    year = 1 # int |  (optional)
    education_group_type = [
        "education_group_type_example",
    ] # [str] |  (optional)
    active = [
        "active_example",
    ] # [str] |  (optional)
    campus = "campus_example" # str |  (optional)
    ordering = "ordering_example" # str |  (optional)
    search = "search_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitrainings_list(limit=limit, offset=offset, acronym=acronym, code=code, title=title, from_year=from_year, to_year=to_year, year=year, education_group_type=education_group_type, active=active, campus=campus, ordering=ordering, search=search, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **acronym** | **str**|  | [optional]
 **code** | **str**|  | [optional]
 **title** | **str**|  | [optional]
 **from_year** | **int**|  | [optional]
 **to_year** | **int**|  | [optional]
 **year** | **int**|  | [optional]
 **education_group_type** | **[str]**|  | [optional]
 **active** | **[str]**|  | [optional]
 **campus** | **str**|  | [optional]
 **ordering** | **str**|  | [optional]
 **search** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PaginatedMiniTraining**](PaginatedMiniTraining.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minitrainings_offer_roots**
> PaginatedTraining minitrainings_offer_roots(year, acronym)



Return the list of offer roots for a mini training.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
from osis_education_group_sdk.model.paginated_training import PaginatedTraining
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitrainings_offer_roots(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_offer_roots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitrainings_offer_roots(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_offer_roots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PaginatedTraining**](PaginatedTraining.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minitrainings_read**
> MiniTrainingDetailed minitrainings_read(year, acronym)



Return the detail of the mini-training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
from osis_education_group_sdk.model.mini_training_detailed import MiniTrainingDetailed
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitrainings_read(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitrainings_read(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**MiniTrainingDetailed**](MiniTrainingDetailed.md)

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

# **minitrainings_title_version_read**
> InlineResponse200 minitrainings_title_version_read(year, acronym, version_name)



Return the title of the mini training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    version_name = "version_name_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitrainings_title_version_read(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_title_version_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitrainings_title_version_read(year, acronym, version_name, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainings_title_version_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **version_name** | **str**|  |
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

# **minitrainingstitle_read**
> InlineResponse200 minitrainingstitle_read(year, acronym)



Return the title of the mini training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import mini_trainings_api
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
    api_instance = mini_trainings_api.MiniTrainingsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.minitrainingstitle_read(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainingstitle_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.minitrainingstitle_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling MiniTrainingsApi->minitrainingstitle_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
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

