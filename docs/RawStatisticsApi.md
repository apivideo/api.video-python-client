# apivideo.RawStatisticsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_live_stream_sessions**](RawStatisticsApi.md#list_live_stream_sessions) | **GET** /analytics/live-streams/{liveStreamId} | List live stream player sessions
[**list_session_events**](RawStatisticsApi.md#list_session_events) | **GET** /analytics/sessions/{sessionId}/events | List player session events
[**list_video_sessions**](RawStatisticsApi.md#list_video_sessions) | **GET** /analytics/videos/{videoId} | List video player sessions


# **list_live_stream_sessions**
> RawStatisticsListLiveStreamAnalyticsResponse list_live_stream_sessions(live_stream_id)

List live stream player sessions

### Example

```python
import apivideo
from apivideo.api import raw_statistics_api
from apivideo.model.raw_statistics_list_live_stream_analytics_response import RawStatisticsListLiveStreamAnalyticsResponse
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = raw_statistics_api.RawStatisticsApi(api_client)
    live_stream_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the live stream you want to retrieve analytics for.
    period = "2019-01-01" # str | Period must have one of the following formats:   - For a day : \"2018-01-01\", - For a week: \"2018-W01\",  - For a month: \"2018-01\" - For a year: \"2018\"  For a range period:  -  Date range: \"2018-01-01/2018-01-15\"  (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List live stream player sessions
        api_response = api_instance.list_live_stream_sessions(live_stream_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_live_stream_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List live stream player sessions
        api_response = api_instance.list_live_stream_sessions(live_stream_id, period=period, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_live_stream_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The unique identifier for the live stream you want to retrieve analytics for. |
 **period** | **str**| Period must have one of the following formats:   - For a day : \&quot;2018-01-01\&quot;, - For a week: \&quot;2018-W01\&quot;,  - For a month: \&quot;2018-01\&quot; - For a year: \&quot;2018\&quot;  For a range period:  -  Date range: \&quot;2018-01-01/2018-01-15\&quot;  | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**RawStatisticsListLiveStreamAnalyticsResponse**](RawStatisticsListLiveStreamAnalyticsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_session_events**
> RawStatisticsListPlayerSessionEventsResponse list_session_events(session_id)

List player session events

Useful to track and measure video's engagement.

### Example

```python
import apivideo
from apivideo.api import raw_statistics_api
from apivideo.model.not_found import NotFound
from apivideo.model.raw_statistics_list_player_session_events_response import RawStatisticsListPlayerSessionEventsResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = raw_statistics_api.RawStatisticsApi(api_client)
    session_id = "psEmFwGQUAXR2lFHj5nDOpy" # str | A unique identifier you can use to reference and track a session with.
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List player session events
        api_response = api_instance.list_session_events(session_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_session_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List player session events
        api_response = api_instance.list_session_events(session_id, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_session_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| A unique identifier you can use to reference and track a session with. |
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**RawStatisticsListPlayerSessionEventsResponse**](RawStatisticsListPlayerSessionEventsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_video_sessions**
> RawStatisticsListSessionsResponse list_video_sessions(video_id)

List video player sessions

Retrieve all available user sessions for a specific video.

### Example

```python
import apivideo
from apivideo.api import raw_statistics_api
from apivideo.model.not_found import NotFound
from apivideo.model.raw_statistics_list_sessions_response import RawStatisticsListSessionsResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = raw_statistics_api.RawStatisticsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklg" # str | The unique identifier for the video you want to retrieve session information for.
    period = "period_example" # str | Period must have one of the following formats:   - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018  For a range period:  -  Date range: 2018-01-01/2018-01-15  (optional)
    metadata = [{"key": "Author", "value": "John Doe"}, {"key": "Format", "value": "Tutorial"}] # [str] | Metadata and Dynamic Metadata filter. Send an array of key value pairs you want to filter sessios with. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List video player sessions
        api_response = api_instance.list_video_sessions(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_video_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List video player sessions
        api_response = api_instance.list_video_sessions(video_id, period=period, metadata=metadata, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling RawStatisticsApi->list_video_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to retrieve session information for. |
 **period** | **str**| Period must have one of the following formats:   - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018  For a range period:  -  Date range: 2018-01-01/2018-01-15  | [optional]
 **metadata** | **[str]**| Metadata and Dynamic Metadata filter. Send an array of key value pairs you want to filter sessios with. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**RawStatisticsListSessionsResponse**](RawStatisticsListSessionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

