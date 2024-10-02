# apivideo.TagsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](TagsApi.md#list) | **GET** /tags | List all video tags


# **list**
> ListTagsResponse list()

List all video tags

This endpoint enables you to search for video tags in a project and see how many videos are tagged with them. If you do not define any query parameters, the endpoint lists all video tags and the numbers of times they are used in a project.

### Example

```python
import apivideo
from apivideo.api import tags_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.list_tags_response import ListTagsResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)
    value = "value_example" # str | Use this parameter to search for specific video tags. The API filters results even on partial values, and ignores accents, uppercase, and lowercase.  (optional)
    sort_by = "value" # str | Use this parameter to choose which field the API will use to sort the response data. The default is `value`.  These are the available fields to sort by:  - `value`: Sorts the results based on tag values in alphabetic order. - `videoCount`: Sorts the results based on the number of times a video tag is used.  (optional)
    sort_order = "asc" # str | Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all video tags
        api_response = api_instance.list(value=value, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling TagsApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Use this parameter to search for specific video tags. The API filters results even on partial values, and ignores accents, uppercase, and lowercase.  | [optional]
 **sort_by** | **str**| Use this parameter to choose which field the API will use to sort the response data. The default is &#x60;value&#x60;.  These are the available fields to sort by:  - &#x60;value&#x60;: Sorts the results based on tag values in alphabetic order. - &#x60;videoCount&#x60;: Sorts the results based on the number of times a video tag is used.  | [optional]
 **sort_order** | **str**| Use this parameter to sort results. &#x60;asc&#x60; is ascending and sorts from A to Z. &#x60;desc&#x60; is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**ListTagsResponse**](ListTagsResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

