# apivideo.VideosApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](VideosApi.md#delete) | **DELETE** /videos/{videoId} | Delete a video
[**get**](VideosApi.md#get) | **GET** /videos/{videoId} | Show a video
[**get_video_status**](VideosApi.md#get_video_status) | **GET** /videos/{videoId}/status | Show video status
[**list**](VideosApi.md#list) | **GET** /videos | List all videos
[**update**](VideosApi.md#update) | **PATCH** /videos/{videoId} | Update a video
[**pick_thumbnail**](VideosApi.md#pick_thumbnail) | **PATCH** /videos/{videoId}/thumbnail | Pick a thumbnail
[**create**](VideosApi.md#create) | **POST** /videos | Create a video
[**upload**](VideosApi.md#upload) | **POST** /videos/{videoId}/source | Upload a video
[**upload_thumbnail**](VideosApi.md#upload_thumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail


# **delete**
> delete(video_id)

Delete a video

If you do not need a video any longer, you can send a request to delete it. All you need is the videoId.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.not_found import NotFound
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The video ID for the video you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a video
        api_instance.delete(video_id)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to delete. |

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

# **get**
> Video get(video_id)

Show a video

This call provides the same JSON information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "videoId_example" # str | The unique identifier for the video you want details about.

    # example passing only required values which don't have defaults set
    try:
        # Show a video
        api_response = api_instance.get(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want details about. |

### Return type

[**Video**](Video.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_status**
> Videostatus get_video_status(video_id)

Show video status

This API provides upload status & encoding status to determine when the video is uploaded or ready to playback.  Once encoding is completed, the response also lists the available stream qualities.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.videostatus import Videostatus
from apivideo.model.not_found import NotFound
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want the status for.

    # example passing only required values which don't have defaults set
    try:
        # Show video status
        api_response = api_instance.get_video_status(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get_video_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want the status for. |

### Return type

[**Videostatus**](Videostatus.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> VideosListResponse list()

List all videos

Requests to this endpoint return a list of your videos (with all their details). With no parameters added to this query, the API returns all videos. You can filter what videos the API returns using the parameters described below.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.videos_list_response import VideosListResponse
from apivideo.model.bad_request import BadRequest
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    title = "My Video.mp4" # str | The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. (optional)
    tags = [
        ""tags": ["captions", "dialogue"]",
    ] # [str] | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. (optional)
    metadata = [
        "[{"key":"Author", "value":"John Doe"}, {"key":"Format", "value":"Tutorial"}]",
    ] # [str] | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. (optional)
    description = "New Zealand" # str | If you described a video with a term or sentence, you can add it here to return videos containing this string. (optional)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here. (optional)
    sort_by = "publishedAt" # str | Allowed: publishedAt, title. You can search by the time videos were published at, or by title. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all videos
        api_response = api_instance.list(title=title, tags=tags, metadata=metadata, description=description, live_stream_id=live_stream_id, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. | [optional]
 **tags** | **[str]**| A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. | [optional]
 **metadata** | **[str]**| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. | [optional]
 **description** | **str**| If you described a video with a term or sentence, you can add it here to return videos containing this string. | [optional]
 **live_stream_id** | **str**| If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here. | [optional]
 **sort_by** | **str**| Allowed: publishedAt, title. You can search by the time videos were published at, or by title. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**VideosListResponse**](VideosListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Video update(video_id)

Update a video

Use this endpoint to update the parameters associated with your video. The video you are updating is determined by the video ID you provide in the path. For each parameter you want to update, include the update in the request body. NOTE: If you are updating an array, you must provide the entire array as what you provide here overwrites what is in the system rather than appending to it.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.video_update_payload import VideoUpdatePayload
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The video ID for the video you want to delete.
    video_update_payload = VideoUpdatePayload(
        player_id="pl4k0jvEUuaTdRAEjQ4Jfrgz",
        title="title_example",
        description="A film about good books.",
        public=True,
        panoramic=False,
        mp4_support=True,
        tags=[
            "["maths", "string theory", "video"]",
        ],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
    ) # VideoUpdatePayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a video
        api_response = api_instance.update(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a video
        api_response = api_instance.update(video_id, video_update_payload=video_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to delete. |
 **video_update_payload** | [**VideoUpdatePayload**](VideoUpdatePayload.md)|  | [optional]

### Return type

[**Video**](Video.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_thumbnail**
> Video pick_thumbnail(video_id)

Pick a thumbnail

Pick a thumbnail from the given time code. If you'd like to upload an image for your thumbnail, use the [Upload a Thumbnail](https://docs.api.video/reference#post_videos-videoid-thumbnail) endpoint. There may be a short delay for the thumbnail to update.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail.
    video_thumbnail_pick_payload = VideoThumbnailPickPayload(
        timecode="00:00:00/0",
    ) # VideoThumbnailPickPayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Pick a thumbnail
        api_response = api_instance.pick_thumbnail(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->pick_thumbnail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pick a thumbnail
        api_response = api_instance.pick_thumbnail(video_id, video_thumbnail_pick_payload=video_thumbnail_pick_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->pick_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail. |
 **video_thumbnail_pick_payload** | [**VideoThumbnailPickPayload**](VideoThumbnailPickPayload.md)|  | [optional]

### Return type

[**Video**](Video.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Video create()

Create a video

To create a video, you create its metadata first, before adding the video file (exception - when using an existing HTTP source).  Videos are public by default. Mp4 encoded versions are created at the highest quality (max 1080p) by default.  ```shell $ curl https://ws.api.video/videos \\ -H 'Authorization: Bearer {access_token} \\ -d '{\"title\":\"My video\",       \"description\":\"so many details\",      \"mp4Support\":true }' ```  ### Creating a hosted video   You can also create a video directly from one hosted on a third-party server by giving its URI in `source` parameter:  ```shell $ curl https://ws.api.video/videos \\ -H 'Authorization: Bearer {access_token} \\ -d '{\"source\":\"http://uri/to/video.mp4\", \"title\":\"My video\"}' ```  In this case, the service will respond `202 Accepted` and download the video asynchronously.   We have tutorials on: * [Creating and uploading videos](https://api.video/blog/tutorials/video-upload-tutorial) * [Uploading large videos](https://api.video/blog/tutorials/video-upload-tutorial-large-videos) * [Using tags with videos](https://api.video/blog/tutorials/video-tagging-best-practices) * [Private videos](https://api.video/blog/tutorials/tutorial-private-videos) 

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.video_create_payload import VideoCreatePayload
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_create_payload = VideoCreatePayload(
        title="Maths video",
        description="A video about string theory.",
        source="https://www.myvideo.url.com/video.mp4",
        public=True,
        panoramic=False,
        mp4_support=True,
        player_id="pl45KFKdlddgk654dspkze",
        tags=[
            "["maths", "string theory", "video"]",
        ],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
        published_at=dateutil_parser('2020-07-14T23:36:18.598Z'),
    ) # VideoCreatePayload | video to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a video
        api_response = api_instance.create(video_create_payload=video_create_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_create_payload** | [**VideoCreatePayload**](VideoCreatePayload.md)| video to create | [optional]

### Return type

[**Video**](Video.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> Video upload(video_id, file)

Upload a video

To upload a video to the videoId you created. Replace {videoId} with the id you'd like to use, {access_token} with your token, and /path/to/video.mp4 with the path to the video you'd like to upload. You can only upload your video to the videoId once.  ```bash curl https://ws.api.video/videos/{videoId}/source \\   -H 'Authorization: Bearer {access_token}' \\   -F file=@/path/to/video.mp4   ```

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | Enter the videoId you want to use to upload your video.
    file = open('/path/to/file', 'rb') # file_type | The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\"/videos\\\" endpoint and add the \\\"source\\\" parameter when you create a new video.
    content_range = "Content-Range: bytes 200-100/5000" # str | Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a video
        api_response = api_instance.upload(video_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a video
        api_response = api_instance.upload(video_id, file, content_range=content_range)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Enter the videoId you want to use to upload your video. |
 **file** | **file_type**| The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\&quot;/videos\\\&quot; endpoint and add the \\\&quot;source\\\&quot; parameter when you create a new video. |
 **content_range** | **str**| Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object. | [optional]

### Return type

[**Video**](Video.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_thumbnail**
> Video upload_thumbnail(video_id, file)

Upload a thumbnail

In creating a thumbnail, you may either upload an image, or you can pick a time in the video to be used as thumbnail. This endpoint is for uploading an image. Use [Pick a Thumbnail](https://docs.api.video/reference#patch_videos-videoid-thumbnail) to pick a time in the video. There may be a short delay before the new thumbnail is delivered to our CDN.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint
# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "videoId_example" # str | Unique identifier of the chosen video 
    file = open('/path/to/file', 'rb') # file_type | The image to be added as a thumbnail.

    # example passing only required values which don't have defaults set
    try:
        # Upload a thumbnail
        api_response = api_instance.upload_thumbnail(video_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the chosen video  |
 **file** | **file_type**| The image to be added as a thumbnail. |

### Return type

[**Video**](Video.md)

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

