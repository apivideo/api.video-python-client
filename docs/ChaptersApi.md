# apivideo.ChaptersApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](ChaptersApi.md#upload) | **POST** /videos/{videoId}/chapters/{language} | Upload a chapter
[**get**](ChaptersApi.md#get) | **GET** /videos/{videoId}/chapters/{language} | Retrieve a chapter
[**delete**](ChaptersApi.md#delete) | **DELETE** /videos/{videoId}/chapters/{language} | Delete a chapter
[**list**](ChaptersApi.md#list) | **GET** /videos/{videoId}/chapters | List video chapters


# **upload**
> Chapter upload(video_id, language, file)

Upload a chapter

Upload a VTT file to add chapters to your video. Chapters help break the video into sections. Read our [tutorial](https://api.video/blog/tutorials/adding-chapters-to-your-videos) for more details.

### Example

```python
import apivideo
from apivideo.api import chapters_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.chapter import Chapter
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = chapters_api.ChaptersApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want to upload a chapter for.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    file = open('/path/to/file', 'rb') # file_type | The VTT file describing the chapters you want to upload.

    # example passing only required values which don't have defaults set
    try:
        # Upload a chapter
        api_response = api_instance.upload(video_id, language, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling ChaptersApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to upload a chapter for. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. |
 **file** | **file_type**| The VTT file describing the chapters you want to upload. |

### Return type

[**Chapter**](Chapter.md)


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Chapter get(video_id, language)

Retrieve a chapter

Retrieve a chapter for by video id in a specific language. 

### Example

```python
import apivideo
from apivideo.api import chapters_api
from apivideo.model.not_found import NotFound
from apivideo.model.chapter import Chapter
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = chapters_api.ChaptersApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want to show a chapter for.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a chapter
        api_response = api_instance.get(video_id, language)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling ChaptersApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to show a chapter for. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. |

### Return type

[**Chapter**](Chapter.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(video_id, language)

Delete a chapter

Delete a chapter in a specific language by providing the video ID for the video you want to delete the chapter from and the language the chapter is in.

### Example

```python
import apivideo
from apivideo.api import chapters_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = chapters_api.ChaptersApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want to delete a chapter from.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

    # example passing only required values which don't have defaults set
    try:
        # Delete a chapter
        api_instance.delete(video_id, language)
    except apivideo.ApiException as e:
        print("Exception when calling ChaptersApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to delete a chapter from. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. |

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
> ChaptersListResponse list(video_id)

List video chapters

Retrieve a list of all chapters for by video id.

### Example

```python
import apivideo
from apivideo.api import chapters_api
from apivideo.model.not_found import NotFound
from apivideo.model.chapters_list_response import ChaptersListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = chapters_api.ChaptersApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want to retrieve a list of chapters for.
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List video chapters
        api_response = api_instance.list(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling ChaptersApi->list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List video chapters
        api_response = api_instance.list(video_id, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling ChaptersApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to retrieve a list of chapters for. |
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**ChaptersListResponse**](ChaptersListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

