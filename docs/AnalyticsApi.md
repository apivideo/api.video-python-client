# apivideo.AnalyticsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_live_streams_plays**](AnalyticsApi.md#get_live_streams_plays) | **GET** /analytics/live-streams/plays | Get play events for live stream
[**get_videos_plays**](AnalyticsApi.md#get_videos_plays) | **GET** /analytics/videos/plays | Get play events for video


# **get_live_streams_plays**
> AnalyticsPlaysResponse get_live_streams_plays(_from, dimension)

Get play events for live stream

Retrieve filtered analytics about the number of plays for your live streams in a project.

### Example

```python
import apivideo
from apivideo.api import analytics_api
from apivideo.model.model403_error_schema import Model403ErrorSchema
from apivideo.model.analytics_plays_response import AnalyticsPlaysResponse
from apivideo.model.not_found import NotFound
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    _from = dateutil_parser('2023-06-01').date() # date | Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 
    dimension = "browser" # str | Use this query parameter to define the dimension that you want analytics for. - `liveStreamId`: Returns analytics based on the public live stream identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. - `browser`: Returns analytics based on the browser used by the viewers during the play event.
    to = dateutil_parser('2023-06-10').date() # date | Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format.  (optional)
    filter = "liveStreamId:li3q7HxhApxRF1c8F8r6VeaI" # str | Use this query parameter to filter your results to a specific live stream in a project that you want analytics for. You must use the `liveStreamId:` prefix when specifying a live stream ID. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get play events for live stream
        api_response = api_instance.get_live_streams_plays(_from, dimension)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_live_streams_plays: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get play events for live stream
        api_response = api_instance.get_live_streams_plays(_from, dimension, to=to, filter=filter, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_live_streams_plays: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in &#x60;from&#x60;. - The date you set must be **within the last 30 days**. - The value you provide must follow the &#x60;YYYY-MM-DD&#x60; format.  |
 **dimension** | **str**| Use this query parameter to define the dimension that you want analytics for. - &#x60;liveStreamId&#x60;: Returns analytics based on the public live stream identifiers. - &#x60;emittedAt&#x60;: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in &#x60;from&#x60; and &#x60;to&#x60; is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - &#x60;deviceType&#x60;: Returns analytics based on the type of device used by the viewers during the play event. - &#x60;operatingSystem&#x60;: Returns analytics based on the operating system used by the viewers during the play event. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers during the play event. |
 **to** | **date**| Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a &#x60;to&#x60; date, the API returns analytics data starting from the &#x60;from&#x60; date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the &#x60;YYYY-MM-DD&#x60; format.  | [optional]
 **filter** | **str**| Use this query parameter to filter your results to a specific live stream in a project that you want analytics for. You must use the &#x60;liveStreamId:&#x60; prefix when specifying a live stream ID. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**AnalyticsPlaysResponse**](AnalyticsPlaysResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request error |  -  |
**403** | Forbidden - Disabled Analytics |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_plays**
> AnalyticsPlaysResponse get_videos_plays(_from, dimension)

Get play events for video

Retrieve filtered analytics about the number of plays for your videos in a project.

### Example

```python
import apivideo
from apivideo.api import analytics_api
from apivideo.model.model403_error_schema import Model403ErrorSchema
from apivideo.model.analytics_plays_response import AnalyticsPlaysResponse
from apivideo.model.not_found import NotFound
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    _from = dateutil_parser('2023-06-01').date() # date | Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 
    dimension = "browser" # str | Use this query parameter to define the dimension that you want analytics for. - `videoId`: Returns analytics based on the public video identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. - `browser`: Returns analytics based on the browser used by the viewers during the play event.
    to = dateutil_parser('2023-06-10').date() # date | Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format.  (optional)
    filter = "videoId:vi3q7HxhApxRF1c8F8r6VeaI" # str | Use this query parameter to filter your results to a specific video in a project that you want analytics for. You must use the `videoId:` prefix when specifying a video ID. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get play events for video
        api_response = api_instance.get_videos_plays(_from, dimension)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_videos_plays: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get play events for video
        api_response = api_instance.get_videos_plays(_from, dimension, to=to, filter=filter, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_videos_plays: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in &#x60;from&#x60;. - The date you set must be **within the last 30 days**. - The value you provide must follow the &#x60;YYYY-MM-DD&#x60; format.  |
 **dimension** | **str**| Use this query parameter to define the dimension that you want analytics for. - &#x60;videoId&#x60;: Returns analytics based on the public video identifiers. - &#x60;emittedAt&#x60;: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in &#x60;from&#x60; and &#x60;to&#x60; is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - &#x60;deviceType&#x60;: Returns analytics based on the type of device used by the viewers during the play event. - &#x60;operatingSystem&#x60;: Returns analytics based on the operating system used by the viewers during the play event. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers during the play event. |
 **to** | **date**| Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a &#x60;to&#x60; date, the API returns analytics data starting from the &#x60;from&#x60; date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the &#x60;YYYY-MM-DD&#x60; format.  | [optional]
 **filter** | **str**| Use this query parameter to filter your results to a specific video in a project that you want analytics for. You must use the &#x60;videoId:&#x60; prefix when specifying a video ID. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**AnalyticsPlaysResponse**](AnalyticsPlaysResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request error |  -  |
**403** | Forbidden - Disabled Analytics |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

