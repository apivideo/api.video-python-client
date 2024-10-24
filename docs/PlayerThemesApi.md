# apivideo.PlayerThemesApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PlayerThemesApi.md#create) | **POST** /players | Create a player
[**get**](PlayerThemesApi.md#get) | **GET** /players/{playerId} | Retrieve a player
[**update**](PlayerThemesApi.md#update) | **PATCH** /players/{playerId} | Update a player
[**delete**](PlayerThemesApi.md#delete) | **DELETE** /players/{playerId} | Delete a player
[**list**](PlayerThemesApi.md#list) | **GET** /players | List all player themes
[**upload_logo**](PlayerThemesApi.md#upload_logo) | **POST** /players/{playerId}/logo | Upload a logo
[**delete_logo**](PlayerThemesApi.md#delete_logo) | **DELETE** /players/{playerId}/logo | Delete logo


# **create**
> PlayerTheme create(player_theme_creation_payload)

Create a player

Create a player for your video, and customise it.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.player_theme_creation_payload import PlayerThemeCreationPayload
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.player_theme import PlayerTheme
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_theme_creation_payload = PlayerThemeCreationPayload(
        name="name_example",
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        link_active="link_active_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=False,
        hide_title=False,
        force_loop=False,
    ) # PlayerThemeCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create a player
        api_response = api_instance.create(player_theme_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_theme_creation_payload** | [**PlayerThemeCreationPayload**](PlayerThemeCreationPayload.md)|  |

### Return type

[**PlayerTheme**](PlayerTheme.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> PlayerTheme get(player_id)

Retrieve a player

Retreive a player theme by player id.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from apivideo.model.player_theme import PlayerTheme
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player you want to retrieve. 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a player
        api_response = api_instance.get(player_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player you want to retrieve.  |

### Return type

[**PlayerTheme**](PlayerTheme.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> PlayerTheme update(player_id, player_theme_update_payload)

Update a player

Use a player ID to update specific details for a player.  NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from apivideo.model.player_theme import PlayerTheme
from apivideo.model.player_theme_update_payload import PlayerThemeUpdatePayload
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player.
    player_theme_update_payload = PlayerThemeUpdatePayload(
        name="name_example",
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        link_active="link_active_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=True,
        hide_title=True,
        force_loop=True,
    ) # PlayerThemeUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a player
        api_response = api_instance.update(player_id, player_theme_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |
 **player_theme_update_payload** | [**PlayerThemeUpdatePayload**](PlayerThemeUpdatePayload.md)|  |

### Return type

[**PlayerTheme**](PlayerTheme.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(player_id)

Delete a player

Delete a player if you no longer need it. You can delete any player that you have the player ID for.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a player
        api_instance.delete(player_id)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player you want to delete. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PlayerThemesListResponse list()

List all player themes

Retrieve a list of all the player themes you created, as well as details about each one.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.player_themes_list_response import PlayerThemesListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    sort_by = "createdAt" # str | createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ATOM UTC format. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all player themes
        api_response = api_instance.list(sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ATOM UTC format. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**PlayerThemesListResponse**](PlayerThemesListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_logo**
> PlayerTheme upload_logo(player_id, file)

Upload a logo

Upload an image file as a logo for your player. The image should fit within these constraints: - The image mime type must be `image/jpeg` or `image/png`. api.video recommends using `png` images with transparent background. - The image size should be a maximum of 200px width x 100px. - The file size should be a maximum of 100 KiB. 

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.player_theme import PlayerTheme
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl14Db6oMJRH6SRVoOwORacK" # str | The unique identifier for the player.
    file = open('/path/to/file', 'rb') # file_type | The name of the file you want to use for your logo.
    link = "https://my-company.com" # str | A public link that you want to advertise in your player. For example, you could add a link to your company. When a viewer clicks on your logo, they will be taken to this address. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a logo
        api_response = api_instance.upload_logo(player_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->upload_logo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a logo
        api_response = api_instance.upload_logo(player_id, file, link=link)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->upload_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |
 **file** | **file_type**| The name of the file you want to use for your logo. |
 **link** | **str**| A public link that you want to advertise in your player. For example, you could add a link to your company. When a viewer clicks on your logo, they will be taken to this address. | [optional]

### Return type

[**PlayerTheme**](PlayerTheme.md)


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logo**
> delete_logo(player_id)

Delete logo

Delete the logo associated to a player.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl14Db6oMJRH6SRVoOwORacK" # str | The unique identifier for the player.

    # example passing only required values which don't have defaults set
    try:
        # Delete logo
        api_instance.delete_logo(player_id)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->delete_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

