# apivideo.VideosApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](VideosApi.md#delete) | **DELETE** /videos/{videoId} | Delete a video
[**get**](VideosApi.md#get) | **GET** /videos/{videoId} | Show a video
[**get_status**](VideosApi.md#get_status) | **GET** /videos/{videoId}/status | Show video status
[**list**](VideosApi.md#list) | **GET** /videos | List all videos
[**update**](VideosApi.md#update) | **PATCH** /videos/{videoId} | Update a video
[**pick_thumbnail**](VideosApi.md#pick_thumbnail) | **PATCH** /videos/{videoId}/thumbnail | Pick a thumbnail
[**upload_with_upload_token**](VideosApi.md#upload_with_upload_token) | **POST** /upload | Upload with an upload token
[**create**](VideosApi.md#create) | **POST** /videos | Create a video
[**upload**](VideosApi.md#upload) | **POST** /videos/{videoId}/source | Upload a video
[**upload_thumbnail**](VideosApi.md#upload_thumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail


# **delete**
> delete(video_id)

Delete a video

If you do not need a video any longer, you can send a request to delete it. All you need is the videoId.

### Example
```python
#install the api.video API client library
#pip install api.video
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

This call provides the same information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL.

### Example
```python
#install the api.video API client library
#pip install api.video
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

# **get_status**
> VideoStatus get_status(video_id)

Show video status

This method provides upload status & encoding status to determine when the video is uploaded or ready to playback. Once encoding is completed, the response also lists the available stream qualities.

### Example
```python
#install the api.video API client library
#pip install api.video
import apivideo
from apivideo.api import videos_api
from apivideo.model.video_status import VideoStatus
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
        api_response = api_instance.get_status(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want the status for. |

### Return type

[**VideoStatus**](VideoStatus.md)


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

This method returns a list of your videos (with all their details). With no parameters added, the API returns the first page of all videos. You can filter videos using the parameters described below.

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
    tags = ["captions", "dialogue"] # [str] | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. (optional)
    metadata = {
        "key": "key_example",
    } # {str: (str,)} | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair. (optional)
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
 **metadata** | **{str: (str,)}**| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair. | [optional]
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
> Video update(video_id, video_update_payload)

Update a video

Updates the parameters associated with your video. The video you are updating is determined by the video ID you provide. 

NOTE: If you are updating an array, you must provide the entire array as what you provide here overwrites what is in the system rather than appending to it.


### Example
```python
#install the api.video API client library
#pip install api.video
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
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
    ) # VideoUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a video
        api_response = api_instance.update(video_id, video_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->update: %s\
" % e)              
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to delete. |
 **video_update_payload** | [**VideoUpdatePayload**](VideoUpdatePayload.md)|  |

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
> Video pick_thumbnail(video_id, video_thumbnail_pick_payload)

Pick a thumbnail

Pick a thumbnail from the given time code. 

If you'd like to upload an image for your thumbnail, use the dedicated [method](#uploadThumbnail). 

There may be a short delay for the thumbnail to update.


### Example
```python
#install the api.video API client library
#pip install api.video
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
        timecode="04:80:72",
    ) # VideoThumbnailPickPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Pick a thumbnail
        api_response = api_instance.pick_thumbnail(video_id, video_thumbnail_pick_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->pick_thumbnail: %s\
" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail. |
 **video_thumbnail_pick_payload** | [**VideoThumbnailPickPayload**](VideoThumbnailPickPayload.md)|  |

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

# **upload_with_upload_token**
> Video upload_with_upload_token(token, file)

Upload with an upload token

This method allows you to send a video using an upload token. Upload tokens are especially useful when the upload is done from the client side. If you want to upload a video from your server-side application, you'd better use the [standard upload method](#upload).

### Example
```python
#The upload will happen on the front end, and not on the backend code.  
#Our [JavaScript uploader(https://docs.api.video/docs/video-uploader) is a great place to look for uploading videos with the delegated token.
#We also have uploaders for a number of [mobile languages](https://docs.api.video/docs/flutter-uploader).
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the token you want to use to upload a video. |
 **file** | **file_type**| The path to the video you want to upload. |
 **video_id** | **str**| The video id returned by the first call to this endpoint in a large video upload scenario. | [optional]

### Return type

[**Video**](Video.md)

### Progressive uploads

Progressive uploads make it possible to upload a video source "progressively," i.e., before knowing the total size of the video. This is done by sending chunks of the video source file sequentially.
The last chunk is sent by calling a different method, so api.video knows that it is time to reassemble the different chunks that were received.


```python
token = "to1tcmSFHeYY5KzyhOqVKMKb"; // The unique identifier for the token you want to use to upload a video.;

part1 = open('10m.mp4.part.a', 'rb')
part2 = open('10m.mp4.part.b', 'rb')
part3 = open('10m.mp4.part.c', 'rb')

session = api_instance.create_upload_with_upload_token_progressive_session(token)

session.uploadPart(part1)
session.uploadPart(part2)

video = session.uploadLastPart(part3)

part1.close()
part2.close()
part3.close()

```

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Video create(video_creation_payload)

Create a video

We have tutorials on: * [Creating and uploading videos](https://api.video/blog/tutorials/video-upload-tutorial) * [Uploading large videos](https://api.video/blog/tutorials/video-upload-tutorial-large-videos) * [Using tags with videos](https://api.video/blog/tutorials/video-tagging-best-practices) * [Private videos](https://api.video/blog/tutorials/tutorial-private-videos) * [Using Dynamic Metadata](https://api.video/blog/tutorials/dynamic-metadata)  * Full list of [tutorials](https://api.video/blog/endpoints/video-create) that demonstrate this endpoint. 

### Example
```python
#install the api.video API client library
#pip install api.video
import apivideo
from apivideo.api import videos_api
from apivideo.model.video_creation_payload import VideoCreationPayload
from apivideo.model.bad_request import BadRequest
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_creation_payload = VideoCreationPayload(
        title="Maths video",
        description="A video about string theory.",
        source="https://www.myvideo.url.com/video.mp4",
        public=True,
        panoramic=False,
        mp4_support=True,
        player_id="pl45KFKdlddgk654dspkze",
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
    ) # VideoCreationPayload | video to create

    # example passing only required values which don't have defaults set
    try:
        # Create a video
        api_response = api_instance.create(video_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_creation_payload** | [**VideoCreationPayload**](VideoCreationPayload.md)| video to create |

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

To upload a video to the videoId you created. You can only upload your video to the videoId once.

We offer 2 types of upload: 
* Regular upload 
* Progressive upload
The latter allows you to split a video source into X chunks and send those chunks independently (concurrently or sequentially). The 2 main goals for our users are to
  * allow the upload of video sources > 200 MiB (200 MiB = the max. allowed file size for regular upload)
  * allow to send a video source "progressively", i.e., before before knowing the total size of the video.
  Once all chunks have been sent, they are reaggregated to one source file. The video source is considered as "completely sent" when the "last" chunk is sent (i.e., the chunk that "completes" the upload).


### Example
```python
#install the api.video API client library
#pip install api.video

import apivideo
from apivideo.api import videos_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from apivideo.configuration import Configuration
from pprint import pprint

# Enter a context with an instance of the API client
# When uploading a file you can change the chunk size (in octet)
configuration = Configuration(chunk_size=10 * 1024 * 1024)
with apivideo.AuthenticatedApiClient(__API_KEY__, configuration=configuration) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | Enter the videoId you want to use to upload your video.
    file = open('/path/to/file', 'rb') # file_type | The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the "/videos" endpoint and add the "source" parameter when you create a new video.

    # example passing only required values which don't have defaults set
    try:
        # Upload a video
        api_response = api_instance.upload(video_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Enter the videoId you want to use to upload your video. |
 **file** | **file_type**| The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\&quot;/videos\\\&quot; endpoint and add the \\\&quot;source\\\&quot; parameter when you create a new video. |

### Return type

[**Video**](Video.md)

### Progressive uploads

Progressive uploads make it possible to upload a video source "progressively," i.e., before knowing the total size of the video. This is done by sending chunks of the video source file sequentially.
The last chunk is sent by calling a different method, so api.video knows that it is time to reassemble the different chunks that were received.


```python
video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // Enter the videoId you want to use to upload your video.;

part1 = open('10m.mp4.part.a', 'rb')
part2 = open('10m.mp4.part.b', 'rb')
part3 = open('10m.mp4.part.c', 'rb')

session = api_instance.create_upload_progressive_session(video_id)

session.uploadPart(part1)
session.uploadPart(part2)

video = session.uploadLastPart(part3)

part1.close()
part2.close()
part3.close()

```

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

The thumbnail is the poster that appears in the player window before video playback begins.

This endpoint allows you to upload an image for the thumbnail.

To select a still frame from the video using a time stamp, use the [dedicated method](#pickThumbnail) to pick a time in the video.

Note: There may be a short delay before the new thumbnail is delivered to our CDN.

### Example
```python
#install the api.video API client library
#pip install api.video

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
        print("Exception when calling VideosApi->upload_thumbnail: %s\
" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the chosen video  |
 **file** | **file_type**| The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB. |

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

