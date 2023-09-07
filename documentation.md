---
title: "Python API client"
slug: "python-api-client"
hidden: false
metadata:
description: "The official Python client for api.video. [api.video](https://api.video) is the video infrastructure for product builders. Lightning fast video APIs for integrating, scaling, and managing on-demand & low latency live streaming features in your app."
---

Python API Client
==============

# Getting started

## Requirements

Python >= 3.6

## Installation

```sh
pip install api.video
```

## Code samples

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

If there is an issue, like you think a refresh token may have been exposed, you can manually retrieve a new one. Otherwise, authentication is handled for you.
When you retrieve a new refresh token, the old one becomes invalid. Here is the code, where you retrieve a list of videos and then refresh your token:

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

# Documentation

## API Endpoints

All URIs are relative to *https://ws.api.video*


### AnalyticsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_live_streams_plays**](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsApi.md#get_live_streams_plays) | **GET** /analytics/live-streams/plays | Get play events for live stream
[**get_videos_plays**](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsApi.md#get_videos_plays) | **GET** /analytics/videos/plays | Get play events for video


### CaptionsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#upload) | **POST** /videos/{videoId}/captions/{language} | Upload a caption
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#get) | **GET** /videos/{videoId}/captions/{language} | Retrieve a caption
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#update) | **PATCH** /videos/{videoId}/captions/{language} | Update a caption
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#delete) | **DELETE** /videos/{videoId}/captions/{language} | Delete a caption
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#list) | **GET** /videos/{videoId}/captions | List video captions


### ChaptersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#upload) | **POST** /videos/{videoId}/chapters/{language} | Upload a chapter
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#get) | **GET** /videos/{videoId}/chapters/{language} | Retrieve a chapter
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#delete) | **DELETE** /videos/{videoId}/chapters/{language} | Delete a chapter
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#list) | **GET** /videos/{videoId}/chapters | List video chapters


### LiveStreamsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#create) | **POST** /live-streams | Create live stream
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#get) | **GET** /live-streams/{liveStreamId} | Retrieve live stream
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#update) | **PATCH** /live-streams/{liveStreamId} | Update a live stream
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#delete) | **DELETE** /live-streams/{liveStreamId} | Delete a live stream
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#list) | **GET** /live-streams | List all live streams
[**upload_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#upload_thumbnail) | **POST** /live-streams/{liveStreamId}/thumbnail | Upload a thumbnail
[**delete_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#delete_thumbnail) | **DELETE** /live-streams/{liveStreamId}/thumbnail | Delete a thumbnail


### PlayerThemesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#create) | **POST** /players | Create a player
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#get) | **GET** /players/{playerId} | Retrieve a player
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#update) | **PATCH** /players/{playerId} | Update a player
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#delete) | **DELETE** /players/{playerId} | Delete a player
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#list) | **GET** /players | List all player themes
[**upload_logo**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#upload_logo) | **POST** /players/{playerId}/logo | Upload a logo
[**delete_logo**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#delete_logo) | **DELETE** /players/{playerId}/logo | Delete logo


### RawStatisticsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**list_live_stream_sessions**](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsApi.md#list_live_stream_sessions) | **GET** /analytics/live-streams/{liveStreamId} | List live stream player sessions
[**list_session_events**](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsApi.md#list_session_events) | **GET** /analytics/sessions/{sessionId}/events | List player session events
[**list_video_sessions**](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsApi.md#list_video_sessions) | **GET** /analytics/videos/{videoId} | List video player sessions


### UploadTokensApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#create_token) | **POST** /upload-tokens | Generate an upload token
[**get_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#get_token) | **GET** /upload-tokens/{uploadToken} | Retrieve upload token
[**delete_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#delete_token) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#list) | **GET** /upload-tokens | List all active upload tokens


### VideosApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#create) | **POST** /videos | Create a video object
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload) | **POST** /videos/{videoId}/source | Upload a video
[**upload_with_upload_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload_with_upload_token) | **POST** /upload | Upload with an delegated upload token
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#get) | **GET** /videos/{videoId} | Retrieve a video object
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#update) | **PATCH** /videos/{videoId} | Update a video object
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#delete) | **DELETE** /videos/{videoId} | Delete a video object
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#list) | **GET** /videos | List all video objects
[**upload_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload_thumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail
[**pick_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#pick_thumbnail) | **PATCH** /videos/{videoId}/thumbnail | Set a thumbnail
[**get_status**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#get_status) | **GET** /videos/{videoId}/status | Retrieve video status and details


### WatermarksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#upload) | **POST** /watermarks | Upload a watermark
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#delete) | **DELETE** /watermarks/{watermarkId} | Delete a watermark
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#list) | **GET** /watermarks | List all watermarks


### WebhooksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#create) | **POST** /webhooks | Create Webhook
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#get) | **GET** /webhooks/{webhookId} | Retrieve Webhook details
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#delete) | **DELETE** /webhooks/{webhookId} | Delete a Webhook
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#list) | **GET** /webhooks | List all webhooks




## Models

 - [AccessToken](https://github.com/apivideo/api.video-python-client/blob/main/docs/AccessToken.md)
 - [AdditionalBadRequestErrors](https://github.com/apivideo/api.video-python-client/blob/main/docs/AdditionalBadRequestErrors.md)
 - [AnalyticsData](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsData.md)
 - [AnalyticsPlays400Error](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsPlays400Error.md)
 - [AnalyticsPlaysResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsPlaysResponse.md)
 - [AuthenticatePayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/AuthenticatePayload.md)
 - [BadRequest](https://github.com/apivideo/api.video-python-client/blob/main/docs/BadRequest.md)
 - [BytesRange](https://github.com/apivideo/api.video-python-client/blob/main/docs/BytesRange.md)
 - [Caption](https://github.com/apivideo/api.video-python-client/blob/main/docs/Caption.md)
 - [CaptionsListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsListResponse.md)
 - [CaptionsUpdatePayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsUpdatePayload.md)
 - [Chapter](https://github.com/apivideo/api.video-python-client/blob/main/docs/Chapter.md)
 - [ChaptersListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersListResponse.md)
 - [Link](https://github.com/apivideo/api.video-python-client/blob/main/docs/Link.md)
 - [LiveStream](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStream.md)
 - [LiveStreamAssets](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamAssets.md)
 - [LiveStreamCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamCreationPayload.md)
 - [LiveStreamListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamListResponse.md)
 - [LiveStreamSession](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSession.md)
 - [LiveStreamSessionClient](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSessionClient.md)
 - [LiveStreamSessionDevice](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSessionDevice.md)
 - [LiveStreamSessionLocation](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSessionLocation.md)
 - [LiveStreamSessionReferrer](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSessionReferrer.md)
 - [LiveStreamSessionSession](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamSessionSession.md)
 - [LiveStreamUpdatePayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamUpdatePayload.md)
 - [Metadata](https://github.com/apivideo/api.video-python-client/blob/main/docs/Metadata.md)
 - [Model403ErrorSchema](https://github.com/apivideo/api.video-python-client/blob/main/docs/Model403ErrorSchema.md)
 - [NotFound](https://github.com/apivideo/api.video-python-client/blob/main/docs/NotFound.md)
 - [Pagination](https://github.com/apivideo/api.video-python-client/blob/main/docs/Pagination.md)
 - [PaginationLink](https://github.com/apivideo/api.video-python-client/blob/main/docs/PaginationLink.md)
 - [PlayerSessionEvent](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerSessionEvent.md)
 - [PlayerTheme](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerTheme.md)
 - [PlayerThemeAssets](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemeAssets.md)
 - [PlayerThemeCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemeCreationPayload.md)
 - [PlayerThemeUpdatePayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemeUpdatePayload.md)
 - [PlayerThemesListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesListResponse.md)
 - [Quality](https://github.com/apivideo/api.video-python-client/blob/main/docs/Quality.md)
 - [RawStatisticsListLiveStreamAnalyticsResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsListLiveStreamAnalyticsResponse.md)
 - [RawStatisticsListPlayerSessionEventsResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsListPlayerSessionEventsResponse.md)
 - [RawStatisticsListSessionsResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/RawStatisticsListSessionsResponse.md)
 - [RefreshTokenPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/RefreshTokenPayload.md)
 - [RestreamsRequestObject](https://github.com/apivideo/api.video-python-client/blob/main/docs/RestreamsRequestObject.md)
 - [RestreamsResponseObject](https://github.com/apivideo/api.video-python-client/blob/main/docs/RestreamsResponseObject.md)
 - [TokenCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/TokenCreationPayload.md)
 - [TokenListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/TokenListResponse.md)
 - [UploadToken](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadToken.md)
 - [Video](https://github.com/apivideo/api.video-python-client/blob/main/docs/Video.md)
 - [VideoAssets](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoAssets.md)
 - [VideoClip](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoClip.md)
 - [VideoCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoCreationPayload.md)
 - [VideoSession](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSession.md)
 - [VideoSessionClient](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionClient.md)
 - [VideoSessionDevice](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionDevice.md)
 - [VideoSessionLocation](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionLocation.md)
 - [VideoSessionOs](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionOs.md)
 - [VideoSessionReferrer](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionReferrer.md)
 - [VideoSessionSession](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSessionSession.md)
 - [VideoSource](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSource.md)
 - [VideoSourceLiveStream](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSourceLiveStream.md)
 - [VideoSourceLiveStreamLink](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoSourceLiveStreamLink.md)
 - [VideoStatus](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoStatus.md)
 - [VideoStatusEncoding](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoStatusEncoding.md)
 - [VideoStatusEncodingMetadata](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoStatusEncodingMetadata.md)
 - [VideoStatusIngest](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoStatusIngest.md)
 - [VideoStatusIngestReceivedParts](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoStatusIngestReceivedParts.md)
 - [VideoThumbnailPickPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoThumbnailPickPayload.md)
 - [VideoUpdatePayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoUpdatePayload.md)
 - [VideoWatermark](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoWatermark.md)
 - [VideosListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosListResponse.md)
 - [Watermark](https://github.com/apivideo/api.video-python-client/blob/main/docs/Watermark.md)
 - [WatermarksListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksListResponse.md)
 - [Webhook](https://github.com/apivideo/api.video-python-client/blob/main/docs/Webhook.md)
 - [WebhooksCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksCreationPayload.md)
 - [WebhooksListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksListResponse.md)



# Have you gotten use from this API client?

Please take a moment to leave a star on the client

This helps other users to find the clients and also helps us understand which clients are most popular. Thank you!

# Contribution

Since this API client is generated from an OpenAPI description, we cannot accept pull requests made directly to the repository. If you want to contribute, you can open a pull request on the repository of our [client generator](https://github.com/apivideo/api-client-generator). Otherwise, you can also simply open an issue detailing your need on this repository.