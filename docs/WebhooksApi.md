# apivideo.WebhooksApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](WebhooksApi.md#delete) | **DELETE** /webhooks/{webhookId} | Delete a Webhook
[**get**](WebhooksApi.md#get) | **GET** /webhooks/{webhookId} | Show Webhook details
[**list**](WebhooksApi.md#list) | **GET** /webhooks | List all webhooks
[**create**](WebhooksApi.md#create) | **POST** /webhooks | Create Webhook


# **delete**
> delete(webhook_id)

Delete a Webhook

This endpoint will delete the indicated webhook.

### Example

```python
import apivideo
from apivideo.api import webhooks_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_id = "webhookId_example" # str | The webhook you wish to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Webhook
        api_instance.delete(webhook_id)
    except apivideo.ApiException as e:
        print("Exception when calling WebhooksApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook you wish to delete. |

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
> Webhook get(webhook_id)

Show Webhook details

This call provides the same JSON information provided on Webjhook creation.

### Example

```python
import apivideo
from apivideo.api import webhooks_api
from apivideo.model.webhook import Webhook
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_id = "webhookId_example" # str | The unique webhook you wish to retreive details on.

    # example passing only required values which don't have defaults set
    try:
        # Show Webhook details
        api_response = api_instance.get(webhook_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling WebhooksApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique webhook you wish to retreive details on. |

### Return type

[**Webhook**](Webhook.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> WebhooksListResponse list()

List all webhooks

Requests to this endpoint return a list of your webhooks (with all their details). You can filter what the webhook list that the API returns using the parameters described below.

### Example

```python
import apivideo
from apivideo.api import webhooks_api
from apivideo.model.webhooks_list_response import WebhooksListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    events = "video.encoding.quality.completed" # str | The webhook event that you wish to filter on. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all webhooks
        api_response = api_instance.list(events=events, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling WebhooksApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events** | **str**| The webhook event that you wish to filter on. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**WebhooksListResponse**](WebhooksListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Webhook create(webhooks_creation_payload)

Create Webhook

Webhooks can push notifications to your server, rather than polling api.video for changes. We currently offer four events: * ```video.encoding.quality.completed```  When a new video is uploaded into your account, it will be encoded into several different HLS sizes/bitrates.  When each version is encoded, your webhook will get a notification.  It will look like ```{ \\\"type\\\": \\\"video.encoding.quality.completed\\\", \\\"emittedAt\\\": \\\"2021-01-29T16:46:25.217+01:00\\\", \\\"videoId\\\": \\\"viXXXXXXXX\\\", \\\"encoding\\\": \\\"hls\\\", \\\"quality\\\": \\\"720p\\\"} ```. This request says that the 720p HLS encoding was completed. * ```live-stream.broadcast.started```  When a livestream begins broadcasting, the broadcasting parameter changes from false to true, and this webhook fires. * ```live-stream.broadcast.ended```  This event fores when the livestream has finished broadcasting, and the broadcasting parameter flips from false to true. * ```video.source.recorded```  This event is similar to ```video.encoding.quality.completed```, but tells you if a livestream has been recorded as a VOD.

### Example

```python
import apivideo
from apivideo.api import webhooks_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.webhook import Webhook
from apivideo.model.webhooks_creation_payload import WebhooksCreationPayload
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhooks_creation_payload = WebhooksCreationPayload(
        events=[
            "video.encoding.quality.completed",
        ],
        url="https://example.com/webhooks",
    ) # WebhooksCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Webhook
        api_response = api_instance.create(webhooks_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling WebhooksApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_creation_payload** | [**WebhooksCreationPayload**](WebhooksCreationPayload.md)|  |

### Return type

[**Webhook**](Webhook.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

