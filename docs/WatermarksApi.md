# apivideo.WatermarksApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](WatermarksApi.md#delete) | **DELETE** /watermarks/{watermarkId} | Delete a watermark
[**list**](WatermarksApi.md#list) | **GET** /watermarks | List all watermarks
[**upload**](WatermarksApi.md#upload) | **POST** /watermarks | Upload a watermark


# **delete**
> delete(watermark_id)

Delete a watermark

Delete a watermark. A watermark is a static image, directly burnt-into a video.

### Example

```python
import apivideo
from apivideo.api import watermarks_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = watermarks_api.WatermarksApi(api_client)
    watermark_id = "watermark_1BWr2L5MTQwxGkuxKjzh6i" # str | The watermark ID for the watermark you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a watermark
        api_instance.delete(watermark_id)
    except apivideo.ApiException as e:
        print("Exception when calling WatermarksApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watermark_id** | **str**| The watermark ID for the watermark you want to delete. |

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
> WatermarksListResponse list()

List all watermarks

List all watermarks. A watermark is a static image, directly burnt into a video. After you have created your watermark, you can define its placement and aspect when you [create a video](https://docs.api.video/reference/post-video).

### Example

```python
import apivideo
from apivideo.api import watermarks_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.watermarks_list_response import WatermarksListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = watermarks_api.WatermarksApi(api_client)
    sort_by = "createdAt" # str | Allowed: createdAt. You can search by the time watermark were created at. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all watermarks
        api_response = api_instance.list(sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling WatermarksApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Allowed: createdAt. You can search by the time watermark were created at. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**WatermarksListResponse**](WatermarksListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> Watermark upload(file)

Upload a watermark

Create a new watermark by uploading a `JPG` or a `PNG` image. A watermark is a static image, directly burnt into a video. After you have created your watermark, you can define its placement and aspect when you [create a video](https://docs.api.video/reference/post-video).

### Example
```python
#install the api.video API client library
#pip install api.video

import apivideo
from apivideo.api import videos_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.WatermarksApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | The watermark image.

    # example passing only required values which don't have defaults set
    try:
        # Upload a watermark
        api_response = api_instance.upload(file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling WatermarksApi->upload: %s\
" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| The &#x60;.jpg&#x60; or &#x60;.png&#x60; image to be added as a watermark. |

### Return type

[**Watermark**](Watermark.md)


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

