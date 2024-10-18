# apivideo.SummariesApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SummariesApi.md#create) | **POST** /summaries | Generate video summary
[**get**](SummariesApi.md#get) | **GET** /summaries/{summaryId}/source | Get summary details
[**update**](SummariesApi.md#update) | **PATCH** /summaries/{summaryId}/source | Update summary details
[**delete**](SummariesApi.md#delete) | **DELETE** /summaries/{summaryId} | Delete video summary
[**list**](SummariesApi.md#list) | **GET** /summaries | List summaries


# **create**
> SummaryObject create(inline_object)

Generate video summary

Generate a title, abstract, and key takeaways for a video.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.conflict_error import ConflictError
from apivideo.model.summary_object import SummaryObject
from apivideo.model.inline_object import InlineObject
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    inline_object = InlineObject(
        video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
        origin="auto",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Generate video summary
        api_response = api_instance.create(inline_object)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**SummaryObject**](SummaryObject.md)


### HTTP request headers

 - **Content-Type**: applictaion/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**409** | Conflict |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SummarySource get(summary_id)

Get summary details

Get all details for a summary.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.summary_source import SummarySource
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary source you want to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Get summary details
        api_response = api_instance.get(summary_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary source you want to retrieve. |

### Return type

[**SummarySource**](SummarySource.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SummarySource update(summary_id, update_summary_request)

Update summary details

Update details for a summary. Note that this operation is only allowed for summary objects where `sourceStatus` is `missing`.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.conflict_error import ConflictError
from apivideo.model.summary_source import SummarySource
from apivideo.model.update_summary_request import UpdateSummaryRequest
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary source you want to update.
    update_summary_request = UpdateSummaryRequest(
        title="A short lecture on quantum theory",
        abstract="In this lecture, we discuss how complicated quantum theory is, using the famous example of Schrödingers cat. We also discuss practical applications like quantum computing.",
        takeaways=["Quantum theory is complicated.","Schrödinger's cat is neither dead, nor alive.","Quantum computers are super cool."],
    ) # UpdateSummaryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update summary details
        api_response = api_instance.update(summary_id, update_summary_request)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary source you want to update. |
 **update_summary_request** | [**UpdateSummaryRequest**](UpdateSummaryRequest.md)|  |

### Return type

[**SummarySource**](SummarySource.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**409** | Conflict |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(summary_id)

Delete video summary

Delete a summary tied to a video.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete video summary
        api_instance.delete(summary_id)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary you want to delete. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> GetSummaries list()

List summaries

List all summarries for your videos in a project.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.get_summaries import GetSummaries
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List summaries
        api_response = api_instance.list()
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSummaries**](GetSummaries.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

