# osis_education_group_sdk.TrainingsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/education_group*

Method | HTTP request | Description
------------- | ------------- | -------------
[**training_prerequisites_official**](TrainingsApi.md#training_prerequisites_official) | **GET** /trainings/{year}/{acronym}/prerequisites | 
[**training_version**](TrainingsApi.md#training_version) | **GET** /trainings/{year}/{acronym}/versions/{version_name} | 
[**trainings_list**](TrainingsApi.md#trainings_list) | **GET** /trainings/ | 
[**trainings_offer_roots**](TrainingsApi.md#trainings_offer_roots) | **GET** /trainings/{year}/{acronym}/offer_roots | 
[**trainings_read**](TrainingsApi.md#trainings_read) | **GET** /trainings/{year}/{acronym} | 
[**trainings_tree**](TrainingsApi.md#trainings_tree) | **GET** /trainings/{year}/{acronym}/tree | 
[**trainingstitle_read**](TrainingsApi.md#trainingstitle_read) | **GET** /trainings/{year}/{acronym}/title | 
[**trainingsversiontitle_read**](TrainingsApi.md#trainingsversiontitle_read) | **GET** /trainings/{year}/{acronym}/versions/{version_name}/title | 
[**versions_tree**](TrainingsApi.md#versions_tree) | **GET** /trainings/{year}/{acronym}/versions/{version_name}/tree | 


# **training_prerequisites_official**
> ArrayOfProgramTreePrerequisites training_prerequisites_official(year, acronym)



Return the prerequisites of the learning units of the training (standard version)

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.training_prerequisites_official(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_official: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_prerequisites_official(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_official: %s\n" % e)
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

# **training_version**
> TrainingDetailed training_version(year, acronym, version_name)



Return the detail of the training version

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.training_detailed import TrainingDetailed
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
    api_instance = trainings_api.TrainingsApi(api_client)
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
        api_response = api_instance.training_version(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_version(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_version: %s\n" % e)
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

[**TrainingDetailed**](TrainingDetailed.md)

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

# **trainings_list**
> PaginatedTraining trainings_list()



Return a list of all the training with optional filtering.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    acronym = "acronym_example" # str |  (optional)
    partial_acronym = "partial_acronym_example" # str |  (optional)
    title = "title_example" # str |  (optional)
    education_group_type = [
        "education_group_type_example",
    ] # [str] |  (optional)
    active = [
        "active_example",
    ] # [str] |  (optional)
    from_year = 1 # int |  (optional)
    to_year = 1 # int |  (optional)
    title_english = "title_english_example" # str |  (optional)
    campus = "campus_example" # str |  (optional)
    ares_ability = 1 # int |  (optional)
    year = 1 # int |  (optional)
    ordering = "ordering_example" # str |  (optional)
    search = "search_example" # str |  (optional)
    study_domain = "study_domain_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainings_list(limit=limit, offset=offset, acronym=acronym, partial_acronym=partial_acronym, title=title, education_group_type=education_group_type, active=active, from_year=from_year, to_year=to_year, title_english=title_english, campus=campus, ares_ability=ares_ability, year=year, ordering=ordering, search=search, study_domain=study_domain, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **acronym** | **str**|  | [optional]
 **partial_acronym** | **str**|  | [optional]
 **title** | **str**|  | [optional]
 **education_group_type** | **[str]**|  | [optional]
 **active** | **[str]**|  | [optional]
 **from_year** | **int**|  | [optional]
 **to_year** | **int**|  | [optional]
 **title_english** | **str**|  | [optional]
 **campus** | **str**|  | [optional]
 **ares_ability** | **int**|  | [optional]
 **year** | **int**|  | [optional]
 **ordering** | **str**|  | [optional]
 **search** | **str**|  | [optional]
 **study_domain** | **str**|  | [optional]
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

# **trainings_offer_roots**
> PaginatedTraining trainings_offer_roots(year, acronym)



Return the list of offer roots for a training.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trainings_offer_roots(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_offer_roots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainings_offer_roots(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_offer_roots: %s\n" % e)
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

# **trainings_read**
> TrainingDetailed trainings_read(year, acronym)



Return the detail of the training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
from osis_education_group_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_education_group_sdk.model.training_detailed import TrainingDetailed
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
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trainings_read(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainings_read(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_read: %s\n" % e)
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

[**TrainingDetailed**](TrainingDetailed.md)

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

# **trainings_tree**
> Tree trainings_tree(year, acronym)



Return the tree of the training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trainings_tree(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainings_tree(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainings_tree: %s\n" % e)
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

# **trainingstitle_read**
> InlineResponse200 trainingstitle_read(year, acronym)



Return the title of the training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
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
        api_response = api_instance.trainingstitle_read(year, acronym)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainingstitle_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainingstitle_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainingstitle_read: %s\n" % e)
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

# **trainingsversiontitle_read**
> InlineResponse200 trainingsversiontitle_read(year, acronym, version_name)



Return the title of the training

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
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
        api_response = api_instance.trainingsversiontitle_read(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainingsversiontitle_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trainingsversiontitle_read(year, acronym, version_name, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->trainingsversiontitle_read: %s\n" % e)
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

# **versions_tree**
> Tree versions_tree(year, acronym, version_name)



Return the tree of the version

### Example

* Api Key Authentication (Token):
```python
import time
import osis_education_group_sdk
from osis_education_group_sdk.api import trainings_api
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
    api_instance = trainings_api.TrainingsApi(api_client)
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
        api_response = api_instance.versions_tree(year, acronym, version_name)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->versions_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.versions_tree(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_education_group_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->versions_tree: %s\n" % e)
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

