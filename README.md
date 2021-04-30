![](https://raw.githubusercontent.com/apivideo/API_OAS_file/master/apivideo_banner.png)

# api.video Python api client

api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

## Requirements.

Python >= 3.6

## Installation

```sh
pip install api.video
```

## Examples

### Automatic authentication

list all videos:

```python
import apivideo
from apivideo.apis import VideosApi

api_key = "__API_KEY__"

with apivideo.AuthenticatedApiClient(api_key) as client:
    # if you rather like to use the sandbox environment:
    # with apivideo.AuthenticatedApiClient(api_key, production=False) as client:

    videos_api = VideosApi(client)
    videos = videos_api.list()
```

In this context the client will keep its authentication updated.

### Manual authentication

If you rather update the access token manually:

```python
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "__API_KEY__"

client = apivideo.AuthenticatedApiClient(api_key)
# if you rather like to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()
videos_api = VideosApi(client)
videos = videos_api.list()

try:
    client.refresh_token()
except ApiAuthException:
    print("cannot refresh token !")

...
```

## Documentation for API Endpoints

All URIs are relative to *https://ws.api.video*


### CaptionsApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsApi.md#delete) | **DELETE** /videos/{videoId}/captions/{language} | Delete a caption
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsApi.md#list) | **GET** /videos/{videoId}/captions | List video captions
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsApi.md#get) | **GET** /videos/{videoId}/captions/{language} | Show a caption
[**update**](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsApi.md#update) | **PATCH** /videos/{videoId}/captions/{language} | Update caption
[**upload**](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsApi.md#upload) | **POST** /videos/{videoId}/captions/{language} | Upload a caption


### ChaptersApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/ChaptersApi.md#delete) | **DELETE** /videos/{videoId}/chapters/{language} | Delete a chapter
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/ChaptersApi.md#list) | **GET** /videos/{videoId}/chapters | List video chapters
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/ChaptersApi.md#get) | **GET** /videos/{videoId}/chapters/{language} | Show a chapter
[**upload**](https://github.com/apivideo/python-api-client/blob/master/docs/ChaptersApi.md#upload) | **POST** /videos/{videoId}/chapters/{language} | Upload a chapter


### LiveStreamsApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#delete) | **DELETE** /live-streams/{liveStreamId} | Delete a live stream
[**delete_thumbnail**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#delete_thumbnail) | **DELETE** /live-streams/{liveStreamId}/thumbnail | Delete a thumbnail
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#list) | **GET** /live-streams | List all live streams
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#get) | **GET** /live-streams/{liveStreamId} | Show live stream
[**update**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#update) | **PATCH** /live-streams/{liveStreamId} | Update a live stream
[**create**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#create) | **POST** /live-streams | Create live stream
[**upload_thumbnail**](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamsApi.md#upload_thumbnail) | **POST** /live-streams/{liveStreamId}/thumbnail | Upload a thumbnail


### PlayerThemesApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#delete) | **DELETE** /players/{playerId} | Delete a player
[**delete_logo**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#delete_logo) | **DELETE** /players/{playerId}/logo | Delete logo
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#list) | **GET** /players | List all players
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#get) | **GET** /players/{playerId} | Show a player
[**update**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#update) | **PATCH** /players/{playerId} | Update a player
[**create**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#create) | **POST** /players | Create a player
[**upload_logo**](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerThemesApi.md#upload_logo) | **POST** /players/{playerId}/logo | Upload a logo


### RawStatisticsApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**list_live_stream_sessions**](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsApi.md#list_live_stream_sessions) | **GET** /analytics/live-streams/{liveStreamId} | List live stream player sessions
[**list_session_events**](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsApi.md#list_session_events) | **GET** /analytics/sessions/{sessionId}/events | List player session events
[**list_video_sessions**](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsApi.md#list_video_sessions) | **GET** /analytics/videos/{videoId} | List video player sessions


### UploadTokensApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](https://github.com/apivideo/python-api-client/blob/master/docs/UploadTokensApi.md#delete_token) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/UploadTokensApi.md#list) | **GET** /upload-tokens | List all active upload tokens.
[**get_token**](https://github.com/apivideo/python-api-client/blob/master/docs/UploadTokensApi.md#get_token) | **GET** /upload-tokens/{uploadToken} | Show upload token
[**create_token**](https://github.com/apivideo/python-api-client/blob/master/docs/UploadTokensApi.md#create_token) | **POST** /upload-tokens | Generate an upload token


### VideosApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#delete) | **DELETE** /videos/{videoId} | Delete a video
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#get) | **GET** /videos/{videoId} | Show a video
[**get_status**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#get_status) | **GET** /videos/{videoId}/status | Show video status
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#list) | **GET** /videos | List all videos
[**update**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#update) | **PATCH** /videos/{videoId} | Update a video
[**pick_thumbnail**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#pick_thumbnail) | **PATCH** /videos/{videoId}/thumbnail | Pick a thumbnail
[**upload_with_upload_token**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#upload_with_upload_token) | **POST** /upload | Upload with an upload token
[**create**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#create) | **POST** /videos | Create a video
[**upload**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#upload) | **POST** /videos/{videoId}/source | Upload a video
[**upload_thumbnail**](https://github.com/apivideo/python-api-client/blob/master/docs/VideosApi.md#upload_thumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail


### WebhooksApi API endpoints


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksApi.md#delete) | **DELETE** /webhooks/{webhookId} | Delete a Webhook
[**get**](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksApi.md#get) | **GET** /webhooks/{webhookId} | Show Webhook details
[**list**](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksApi.md#list) | **GET** /webhooks | List all webhooks
[**create**](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksApi.md#create) | **POST** /webhooks | Create Webhook




## Documentation For Models

 - [AccessToken](https://github.com/apivideo/python-api-client/blob/master/docs/AccessToken.md)
 - [Account](https://github.com/apivideo/python-api-client/blob/master/docs/Account.md)
 - [AccountQuota](https://github.com/apivideo/python-api-client/blob/master/docs/AccountQuota.md)
 - [AuthenticatePayload](https://github.com/apivideo/python-api-client/blob/master/docs/AuthenticatePayload.md)
 - [BadRequest](https://github.com/apivideo/python-api-client/blob/master/docs/BadRequest.md)
 - [BytesRange](https://github.com/apivideo/python-api-client/blob/master/docs/BytesRange.md)
 - [CaptionsListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsListResponse.md)
 - [CaptionsUpdatePayload](https://github.com/apivideo/python-api-client/blob/master/docs/CaptionsUpdatePayload.md)
 - [Chapter](https://github.com/apivideo/python-api-client/blob/master/docs/Chapter.md)
 - [ChaptersListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/ChaptersListResponse.md)
 - [Link](https://github.com/apivideo/python-api-client/blob/master/docs/Link.md)
 - [LiveStream](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStream.md)
 - [LiveStreamAssets](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamAssets.md)
 - [LiveStreamCreationPayload](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamCreationPayload.md)
 - [LiveStreamListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamListResponse.md)
 - [LiveStreamSession](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSession.md)
 - [LiveStreamSessionClient](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSessionClient.md)
 - [LiveStreamSessionDevice](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSessionDevice.md)
 - [LiveStreamSessionLocation](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSessionLocation.md)
 - [LiveStreamSessionReferrer](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSessionReferrer.md)
 - [LiveStreamSessionSession](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamSessionSession.md)
 - [LiveStreamUpdatePayload](https://github.com/apivideo/python-api-client/blob/master/docs/LiveStreamUpdatePayload.md)
 - [Metadata](https://github.com/apivideo/python-api-client/blob/master/docs/Metadata.md)
 - [NotFound](https://github.com/apivideo/python-api-client/blob/master/docs/NotFound.md)
 - [Pagination](https://github.com/apivideo/python-api-client/blob/master/docs/Pagination.md)
 - [PaginationLink](https://github.com/apivideo/python-api-client/blob/master/docs/PaginationLink.md)
 - [Player](https://github.com/apivideo/python-api-client/blob/master/docs/Player.md)
 - [PlayerAssets](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerAssets.md)
 - [PlayerCreationPayload](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerCreationPayload.md)
 - [PlayerSessionEvent](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerSessionEvent.md)
 - [PlayerUpdatePayload](https://github.com/apivideo/python-api-client/blob/master/docs/PlayerUpdatePayload.md)
 - [PlayersListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/PlayersListResponse.md)
 - [Quality](https://github.com/apivideo/python-api-client/blob/master/docs/Quality.md)
 - [RawStatisticsListLiveStreamAnalyticsResponse](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsListLiveStreamAnalyticsResponse.md)
 - [RawStatisticsListPlayerSessionEventsResponse](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsListPlayerSessionEventsResponse.md)
 - [RawStatisticsListSessionsResponse](https://github.com/apivideo/python-api-client/blob/master/docs/RawStatisticsListSessionsResponse.md)
 - [RefreshTokenPayload](https://github.com/apivideo/python-api-client/blob/master/docs/RefreshTokenPayload.md)
 - [Subtitle](https://github.com/apivideo/python-api-client/blob/master/docs/Subtitle.md)
 - [TokenCreationPayload](https://github.com/apivideo/python-api-client/blob/master/docs/TokenCreationPayload.md)
 - [TokenListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/TokenListResponse.md)
 - [UploadToken](https://github.com/apivideo/python-api-client/blob/master/docs/UploadToken.md)
 - [Video](https://github.com/apivideo/python-api-client/blob/master/docs/Video.md)
 - [VideoAssets](https://github.com/apivideo/python-api-client/blob/master/docs/VideoAssets.md)
 - [VideoCreationPayload](https://github.com/apivideo/python-api-client/blob/master/docs/VideoCreationPayload.md)
 - [VideoSession](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSession.md)
 - [VideoSessionClient](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionClient.md)
 - [VideoSessionDevice](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionDevice.md)
 - [VideoSessionLocation](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionLocation.md)
 - [VideoSessionOs](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionOs.md)
 - [VideoSessionReferrer](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionReferrer.md)
 - [VideoSessionSession](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSessionSession.md)
 - [VideoSource](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSource.md)
 - [VideoSourceLiveStream](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSourceLiveStream.md)
 - [VideoSourceLiveStreamLink](https://github.com/apivideo/python-api-client/blob/master/docs/VideoSourceLiveStreamLink.md)
 - [VideoStatus](https://github.com/apivideo/python-api-client/blob/master/docs/VideoStatus.md)
 - [VideoStatusEncoding](https://github.com/apivideo/python-api-client/blob/master/docs/VideoStatusEncoding.md)
 - [VideoStatusEncodingMetadata](https://github.com/apivideo/python-api-client/blob/master/docs/VideoStatusEncodingMetadata.md)
 - [VideoStatusIngest](https://github.com/apivideo/python-api-client/blob/master/docs/VideoStatusIngest.md)
 - [VideoThumbnailPickPayload](https://github.com/apivideo/python-api-client/blob/master/docs/VideoThumbnailPickPayload.md)
 - [VideoUpdatePayload](https://github.com/apivideo/python-api-client/blob/master/docs/VideoUpdatePayload.md)
 - [VideosListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/VideosListResponse.md)
 - [Webhook](https://github.com/apivideo/python-api-client/blob/master/docs/Webhook.md)
 - [WebhooksCreationPayload](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksCreationPayload.md)
 - [WebhooksListResponse](https://github.com/apivideo/python-api-client/blob/master/docs/WebhooksListResponse.md)
