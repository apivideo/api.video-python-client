# apivideo.UploadTokensApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](UploadTokensApi.md#delete_token) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token
[**list**](UploadTokensApi.md#list) | **GET** /upload-tokens | List all active upload tokens.
[**get_token**](UploadTokensApi.md#get_token) | **GET** /upload-tokens/{uploadToken} | Show upload token
[**create_token**](UploadTokensApi.md#create_token) | **POST** /upload-tokens | Generate an upload token


# **delete_token**
> delete_token(upload_token)

Delete an upload token

Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

### Example
```python
#install the api.video API client library
#pip install api.video
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

List all active upload tokens.

A delegated token is used to allow secure uploads without exposing your API key. Use this endpoint to retrieve a list of all currently active delegated tokens. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

### Example
```python
#install the api.video API client library
#pip install api.video
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
        # Show upload token
        api_response = api_instance.get_token(upload_token)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling UploadTokensApi->get_token: %s\n" % e)
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

# **get_token**
> UploadToken get_token(upload_token)

Show upload token

You can retrieve details about a specific upload token if you have the unique identifier for the upload token. Add it in the path of the endpoint. Details include time-to-live (ttl), when the token was created, and when it will expire.

### Example
```python
#install the api.video API client library
#pip install api.video
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
        # Show upload token
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

# **create_token**
> UploadToken create_token(token_creation_payload)

Generate an upload token

Use this endpoint to generate an upload token. You can use this token to authenticate video uploads while keeping your API key safe. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

### Example
```python
#install the api.video API client library
#pip install api.video
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
        print("Exception when calling UploadTokensApi->create_token: %s\
" % e)
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

