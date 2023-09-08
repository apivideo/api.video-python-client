# apivideo.LiveStreamsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](LiveStreamsApi.md#create) | **POST** /live-streams | Create live stream
[**get**](LiveStreamsApi.md#get) | **GET** /live-streams/{liveStreamId} | Retrieve live stream
[**update**](LiveStreamsApi.md#update) | **PATCH** /live-streams/{liveStreamId} | Update a live stream
[**delete**](LiveStreamsApi.md#delete) | **DELETE** /live-streams/{liveStreamId} | Delete a live stream
[**list**](LiveStreamsApi.md#list) | **GET** /live-streams | List all live streams
[**upload_thumbnail**](LiveStreamsApi.md#upload_thumbnail) | **POST** /live-streams/{liveStreamId}/thumbnail | Upload a thumbnail
[**delete_thumbnail**](LiveStreamsApi.md#delete_thumbnail) | **DELETE** /live-streams/{liveStreamId}/thumbnail | Delete a thumbnail


# **create**
> LiveStream create(live_stream_creation_payload)

Create live stream

Creates a livestream object.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.live_stream_creation_payload import LiveStreamCreationPayload
from apivideo.model.live_stream import LiveStream
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_creation_payload = LiveStreamCreationPayload(
        name="My Live Stream Video",
        record=True,
        public=True,
        player_id="pl4f4ferf5erfr5zed4fsdd",
        restreams=[
            RestreamsRequestObject(
                name="My RTMP server",
                server_url="rtmp://my.broadcast.example.com/app",
                stream_key="dw-dew8-q6w9-k67w-1ws8",
            ),
        ],
    ) # LiveStreamCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create live stream
        api_response = api_instance.create(live_stream_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_creation_payload** | [**LiveStreamCreationPayload**](LiveStreamCreationPayload.md)|  |

### Return type

[**LiveStream**](LiveStream.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> LiveStream get(live_stream_id)

Retrieve live stream

Get a livestream by id.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.live_stream import LiveStream
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | The unique ID for the live stream you want to watch.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve live stream
        api_response = api_instance.get(live_stream_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique ID for the live stream you want to watch. |

### Return type

[**LiveStream**](LiveStream.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> LiveStream update(live_stream_id, live_stream_update_payload)

Update a live stream

Updates the livestream object.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.live_stream_update_payload import LiveStreamUpdatePayload
from apivideo.model.live_stream import LiveStream
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | The unique ID for the live stream that you want to update information for such as player details, or whether you want the recording on or off.
    live_stream_update_payload = LiveStreamUpdatePayload(
        name="My Live Stream Video",
        public=True,
        record=True,
        player_id="pl45KFKdlddgk654dspkze",
        restreams=[
            RestreamsRequestObject(
                name="My RTMP server",
                server_url="rtmp://my.broadcast.example.com/app",
                stream_key="dw-dew8-q6w9-k67w-1ws8",
            ),
        ],
    ) # LiveStreamUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a live stream
        api_response = api_instance.update(live_stream_id, live_stream_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique ID for the live stream that you want to update information for such as player details, or whether you want the recording on or off. |
 **live_stream_update_payload** | [**LiveStreamUpdatePayload**](LiveStreamUpdatePayload.md)|  |

### Return type

[**LiveStream**](LiveStream.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(live_stream_id)

Delete a live stream

If you do not need a live stream any longer, you can send a request to delete it. All you need is the liveStreamId.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | The unique ID for the live stream that you want to remove.

    # example passing only required values which don't have defaults set
    try:
        # Delete a live stream
        api_instance.delete(live_stream_id)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique ID for the live stream that you want to remove. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> LiveStreamListResponse list()

List all live streams

Get the list of livestreams on the workspace.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.live_stream_list_response import LiveStreamListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    stream_key = "dw-dew8-q6w9-k67w-1ws8" # str | The unique stream key that allows you to stream videos. (optional)
    name = "My Video" # str | You can filter live streams by their name or a part of their name. (optional)
    sort_by = "createdAt" # str | Allowed: createdAt, publishedAt, name. createdAt - the time a livestream was created using the specified streamKey. publishedAt - the time a livestream was published using the specified streamKey. name - the name of the livestream. If you choose one of the time based options, the time is presented in ISO-8601 format. (optional)
    sort_order = "desc" # str | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all live streams
        api_response = api_instance.list(stream_key=stream_key, name=name, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_key** | **str**| The unique stream key that allows you to stream videos. | [optional]
 **name** | **str**| You can filter live streams by their name or a part of their name. | [optional]
 **sort_by** | **str**| Allowed: createdAt, publishedAt, name. createdAt - the time a livestream was created using the specified streamKey. publishedAt - the time a livestream was published using the specified streamKey. name - the name of the livestream. If you choose one of the time based options, the time is presented in ISO-8601 format. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**LiveStreamListResponse**](LiveStreamListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_thumbnail**
> LiveStream upload_thumbnail(live_stream_id, file)

Upload a thumbnail

Upload the thumbnail for the livestream.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.live_stream import LiveStream
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique ID for the live stream you want to upload.
    file = open('/path/to/file', 'rb') # file_type | The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB.

    # example passing only required values which don't have defaults set
    try:
        # Upload a thumbnail
        api_response = api_instance.upload_thumbnail(live_stream_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->upload_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique ID for the live stream you want to upload. |
 **file** | **file_type**| The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB. |

### Return type

[**LiveStream**](LiveStream.md)


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

# **delete_thumbnail**
> LiveStream delete_thumbnail(live_stream_id)

Delete a thumbnail

Send the unique identifier for a live stream to delete its thumbnail.

### Example

```python
import apivideo
from apivideo.api import live_streams_api
from apivideo.model.not_found import NotFound
from apivideo.model.live_stream import LiveStream
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = live_streams_api.LiveStreamsApi(api_client)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | The unique identifier of the live stream whose thumbnail you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a thumbnail
        api_response = api_instance.delete_thumbnail(live_stream_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique identifier of the live stream whose thumbnail you want to delete. |

### Return type

[**LiveStream**](LiveStream.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

