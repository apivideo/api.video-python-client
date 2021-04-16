# apivideo.VideosDelegatedUploadApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](VideosDelegatedUploadApi.md#delete_token) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token
[**list_tokens**](VideosDelegatedUploadApi.md#list_tokens) | **GET** /upload-tokens | List all active upload tokens.
[**get_token**](VideosDelegatedUploadApi.md#get_token) | **GET** /upload-tokens/{uploadToken} | Show upload token
[**upload**](VideosDelegatedUploadApi.md#upload) | **POST** /upload | Upload with an upload token
[**create_token**](VideosDelegatedUploadApi.md#create_token) | **POST** /upload-tokens | Generate an upload token


# **delete_token**
> delete_token(upload_token)

Delete an upload token

Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

### Example

```python
import apivideo
from apivideo.api import videos_delegated_upload_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_delegated_upload_api.VideosDelegatedUploadApi(api_client)
    upload_token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication.

    # example passing only required values which don't have defaults set
    try:
        # Delete an upload token
        api_instance.delete_token(upload_token)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_token** | **str**| The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication. |

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

# **list_tokens**
> TokenListResponse list_tokens()

List all active upload tokens.

A delegated token is used to allow secure uploads without exposing your API key. Use this endpoint to retrieve a list of all currently active delegated tokens.

### Example

```python
import apivideo
from apivideo.api import videos_delegated_upload_api
from apivideo.model.token_list_response import TokenListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_delegated_upload_api.VideosDelegatedUploadApi(api_client)
    sort_by = "ttl" # str | Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all active upload tokens.
        api_response = api_instance.list_tokens(sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->list_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**TokenListResponse**](TokenListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> UploadToken get_token(upload_token)

Show upload token

You can retrieve details about a specific upload token if you have the unique identifier for the upload token. Add it in the path of the endpoint. Details include time-to-live (ttl), when the token was created, and when it will expire.

### Example

```python
import apivideo
from apivideo.api import videos_delegated_upload_api
from apivideo.model.not_found import NotFound
from apivideo.model.upload_token import UploadToken
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_delegated_upload_api.VideosDelegatedUploadApi(api_client)
    upload_token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the token you want information about.

    # example passing only required values which don't have defaults set
    try:
        # Show upload token
        api_response = api_instance.get_token(upload_token)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->get_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_token** | **str**| The unique identifier for the token you want information about. |

### Return type

[**UploadToken**](UploadToken.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> Video upload(token, file)

Upload with an upload token

When given a token, anyone can upload a file to the URI `https://ws.api.video/upload?token=<tokenId>`.  Example with cURL:  ```curl $ curl  --request POST --url 'https://ws.api.video/upload?token=toXXX'  --header 'content-type: multipart/form-data'  -F file=@video.mp4 ```  Or in an HTML form, with a little JavaScript to convert the form into JSON: ```html <!--form for user interaction--> <form name=\"videoUploadForm\" >   <label for=video>Video:</label>   <input type=file name=source/><br/>   <input value=\"Submit\" type=\"submit\"> </form> <div></div> <!--JS takes the form data      uses FormData to turn the response into JSON.     then uses POST to upload the video file.     Update the token parameter in the url to your upload token.     --> <script>    var form = document.forms.namedItem(\"videoUploadForm\");     form.addEventListener('submit', function(ev) {   ev.preventDefault();      var oOutput = document.querySelector(\"div\"),          oData = new FormData(form);      var oReq = new XMLHttpRequest();         oReq.open(\"POST\", \"https://ws.api.video/upload?token=toXXX\", true);      oReq.send(oData);   oReq.onload = function(oEvent) {        if (oReq.status ==201) {          oOutput.innerHTML = \"Your video is uploaded!<br/>\"  + oReq.response;        } else {          oOutput.innerHTML = \"Error \" + oReq.status + \" occurred when trying to upload your file.<br />\";        }      };    }, false);  </script> ```   ### Dealing with large files  We have created a <a href='https://api.video/blog/tutorials/uploading-large-files-with-javascript'>tutorial</a> to walk through the steps required.

### Example

```python
import apivideo
from apivideo.api import videos_delegated_upload_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.video import Video
from apivideo.configuration import Configuration
from pprint import pprint

# Enter a context with an instance of the API client
# When uploading a file you can change the chunk size (in octet)
configuration = Configuration(chunk_size=10 * 1024 * 1024)
with apivideo.AuthenticatedApiClient(__API_KEY__, configuration=configuration) as api_client:
    # Create an instance of the API class
    api_instance = videos_delegated_upload_api.VideosDelegatedUploadApi(api_client)
    token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the token you want to use to upload a video.
    file = open('/path/to/file', 'rb') # file_type | The path to the video you want to upload.
    video_id = "video_id_example" # str | The video id returned by the first call to this endpoint in a large video upload scenario. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload with an upload token
        api_response = api_instance.upload(token, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload with an upload token
        api_response = api_instance.upload(token, file, video_id=video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the token you want to use to upload a video. |
 **file** | **file_type**| The path to the video you want to upload. |
 **video_id** | **str**| The video id returned by the first call to this endpoint in a large video upload scenario. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> UploadToken create_token()

Generate an upload token

Use this endpoint to generate an upload token. You can use this token to authenticate video uploads while keeping your API key safe.

### Example

```python
import apivideo
from apivideo.api import videos_delegated_upload_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.token_create_payload import TokenCreatePayload
from apivideo.model.upload_token import UploadToken
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_delegated_upload_api.VideosDelegatedUploadApi(api_client)
    token_create_payload = TokenCreatePayload(
        ttl=0,
    ) # TokenCreatePayload |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate an upload token
        api_response = api_instance.create_token(token_create_payload=token_create_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosDelegatedUploadApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_create_payload** | [**TokenCreatePayload**](TokenCreatePayload.md)|  | [optional]

### Return type

[**UploadToken**](UploadToken.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

