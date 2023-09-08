# apivideo.UploadTokensApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](UploadTokensApi.md#create_token) | **POST** /upload-tokens | Generate an upload token
[**get_token**](UploadTokensApi.md#get_token) | **GET** /upload-tokens/{uploadToken} | Retrieve upload token
[**delete_token**](UploadTokensApi.md#delete_token) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token
[**list**](UploadTokensApi.md#list) | **GET** /upload-tokens | List all active upload tokens


# **create_token**
> UploadToken create_token(token_creation_payload)

Generate an upload token

Generates an upload token that can be used to replace the API Key. More information can be found [here](https://docs.api.video/reference/upload-tokens)

### Example

```python
import apivideo
from apivideo.api import upload_tokens_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.upload_token import UploadToken
from apivideo.model.token_creation_payload import TokenCreationPayload
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = upload_tokens_api.UploadTokensApi(api_client)
    token_creation_payload = TokenCreationPayload(
        ttl=0,
    ) # TokenCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Generate an upload token
        api_response = api_instance.create_token(token_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling UploadTokensApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_creation_payload** | [**TokenCreationPayload**](TokenCreationPayload.md)|  |

### Return type

[**UploadToken**](UploadToken.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> UploadToken get_token(upload_token)

Retrieve upload token

Retrieve details about a specific upload token by id.

### Example

```python
import apivideo
from apivideo.api import upload_tokens_api
from apivideo.model.not_found import NotFound
from apivideo.model.upload_token import UploadToken
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = upload_tokens_api.UploadTokensApi(api_client)
    upload_token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the token you want information about.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve upload token
        api_response = api_instance.get_token(upload_token)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling UploadTokensApi->get_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_token** | **str**| The unique identifier for the token you want information about. |

### Return type

[**UploadToken**](UploadToken.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token(upload_token)

Delete an upload token

Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

### Example

```python
import apivideo
from apivideo.api import upload_tokens_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = upload_tokens_api.UploadTokensApi(api_client)
    upload_token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication.

    # example passing only required values which don't have defaults set
    try:
        # Delete an upload token
        api_instance.delete_token(upload_token)
    except apivideo.ApiException as e:
        print("Exception when calling UploadTokensApi->delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_token** | **str**| The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> TokenListResponse list()

List all active upload tokens

Retrieve a list of all currently active delegated tokens.

### Example

```python
import apivideo
from apivideo.api import upload_tokens_api
from apivideo.model.token_list_response import TokenListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = upload_tokens_api.UploadTokensApi(api_client)
    sort_by = "ttl" # str | Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all active upload tokens
        api_response = api_instance.list(sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling UploadTokensApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**TokenListResponse**](TokenListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

