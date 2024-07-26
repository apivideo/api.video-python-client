<!--<documentation_excluded>-->
[![badge](https://img.shields.io/twitter/follow/api_video?style=social)](https://twitter.com/intent/follow?screen_name=api_video) &nbsp; [![badge](https://img.shields.io/github/stars/apivideo/api.video-python-client?style=social)](https://github.com/apivideo/api.video-python-client) &nbsp; [![badge](https://img.shields.io/discourse/topics?server=https%3A%2F%2Fcommunity.api.video)](https://community.api.video)
![](https://github.com/apivideo/.github/blob/main/assets/apivideo_banner.png)
<h1 align="center">api.video Python client</h1>

[api.video](https://api.video) is the video infrastructure for product builders. Lightning fast video APIs for integrating, scaling, and managing on-demand & low latency live streaming features in your app.

## Table of contents

- [Table of contents](#table-of-contents)
- [Project description](#project-description)
- [Getting started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Code samples](#code-samples)
    - [Automatic authentication](#automatic-authentication)
    - [Manual authentication](#manual-authentication)
- [Documentation](#documentation)
  - [API Endpoints](#api-endpoints)
    - [AnalyticsApi](#)
    - [CaptionsApi](#)
    - [ChaptersApi](#)
    - [LiveStreamsApi](#)
    - [PlayerThemesApi](#)
    - [UploadTokensApi](#)
    - [VideosApi](#)
    - [WatermarksApi](#)
    - [WebhooksApi](#)
  - [Models](#models)
- [Have you gotten use from this API client?](#have-you-gotten-use-from-this-api-client-)
- [Contribution](#contribution)
<!--</documentation_excluded>-->
<!--<documentation_only>
---
title: Python API client
meta: 
  description: The official Python API client for api.video. [api.video](https://api.video/) is the video infrastructure for product builders. Lightning fast video APIs for integrating, scaling, and managing on-demand & low latency live streaming features in your app.
---

# api.video Python API client

[api.video](https://api.video/) is the video infrastructure for product builders. Lightning fast video APIs for integrating, scaling, and managing on-demand & low latency live streaming features in your app.
</documentation_only>-->

## Project description

api.video's Python API client streamlines the coding process. Chunking files is handled for you, as is pagination and refreshing your tokens.

## Getting started

### Requirements

Python >= 3.6

### Installation

```sh
pip install api.video
```

### Code samples

#### Automatic authentication

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

#### Manual authentication

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

## Documentation

### API Endpoints

All URIs are relative to *https://ws.api.video*


### AnalyticsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_metrics**](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsApi.md#get_aggregated_metrics) | **GET** `/data/metrics/{metric}/{aggregation}` | Retrieve aggregated metrics
[**get_metrics_breakdown**](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsApi.md#get_metrics_breakdown) | **GET** `/data/buckets/{metric}/{breakdown}` | Retrieve metrics in a breakdown of dimensions
[**get_metrics_over_time**](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsApi.md#get_metrics_over_time) | **GET** `/data/timeseries/{metric}` | Retrieve metrics over time


### CaptionsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#upload) | **POST** `/videos/{videoId}/captions/{language}` | Upload a caption
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#get) | **GET** `/videos/{videoId}/captions/{language}` | Retrieve a caption
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#update) | **PATCH** `/videos/{videoId}/captions/{language}` | Update a caption
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#delete) | **DELETE** `/videos/{videoId}/captions/{language}` | Delete a caption
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/CaptionsApi.md#list) | **GET** `/videos/{videoId}/captions` | List video captions


### ChaptersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#upload) | **POST** `/videos/{videoId}/chapters/{language}` | Upload a chapter
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#get) | **GET** `/videos/{videoId}/chapters/{language}` | Retrieve a chapter
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#delete) | **DELETE** `/videos/{videoId}/chapters/{language}` | Delete a chapter
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/ChaptersApi.md#list) | **GET** `/videos/{videoId}/chapters` | List video chapters


### LiveStreamsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#create) | **POST** `/live-streams` | Create live stream
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#get) | **GET** `/live-streams/{liveStreamId}` | Retrieve live stream
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#update) | **PATCH** `/live-streams/{liveStreamId}` | Update a live stream
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#delete) | **DELETE** `/live-streams/{liveStreamId}` | Delete a live stream
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#list) | **GET** `/live-streams` | List all live streams
[**upload_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#upload_thumbnail) | **POST** `/live-streams/{liveStreamId}/thumbnail` | Upload a thumbnail
[**delete_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#delete_thumbnail) | **DELETE** `/live-streams/{liveStreamId}/thumbnail` | Delete a thumbnail
[**complete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamsApi.md#complete) | **PUT** `/live-streams/{liveStreamId}/complete` | Complete a live stream


### PlayerThemesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#create) | **POST** `/players` | Create a player
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#get) | **GET** `/players/{playerId}` | Retrieve a player
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#update) | **PATCH** `/players/{playerId}` | Update a player
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#delete) | **DELETE** `/players/{playerId}` | Delete a player
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#list) | **GET** `/players` | List all player themes
[**upload_logo**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#upload_logo) | **POST** `/players/{playerId}/logo` | Upload a logo
[**delete_logo**](https://github.com/apivideo/api.video-python-client/blob/main/docs/PlayerThemesApi.md#delete_logo) | **DELETE** `/players/{playerId}/logo` | Delete logo


### UploadTokensApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#create_token) | **POST** `/upload-tokens` | Generate an upload token
[**get_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#get_token) | **GET** `/upload-tokens/{uploadToken}` | Retrieve upload token
[**delete_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#delete_token) | **DELETE** `/upload-tokens/{uploadToken}` | Delete an upload token
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadTokensApi.md#list) | **GET** `/upload-tokens` | List all active upload tokens


### VideosApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#create) | **POST** `/videos` | Create a video object
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload) | **POST** `/videos/{videoId}/source` | Upload a video
[**upload_with_upload_token**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload_with_upload_token) | **POST** `/upload` | Upload with an delegated upload token
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#get) | **GET** `/videos/{videoId}` | Retrieve a video object
[**update**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#update) | **PATCH** `/videos/{videoId}` | Update a video object
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#delete) | **DELETE** `/videos/{videoId}` | Delete a video object
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#list) | **GET** `/videos` | List all video objects
[**upload_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#upload_thumbnail) | **POST** `/videos/{videoId}/thumbnail` | Upload a thumbnail
[**pick_thumbnail**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#pick_thumbnail) | **PATCH** `/videos/{videoId}/thumbnail` | Set a thumbnail
[**get_status**](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideosApi.md#get_status) | **GET** `/videos/{videoId}/status` | Retrieve video status and details


### WatermarksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#upload) | **POST** `/watermarks` | Upload a watermark
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#delete) | **DELETE** `/watermarks/{watermarkId}` | Delete a watermark
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WatermarksApi.md#list) | **GET** `/watermarks` | List all watermarks


### WebhooksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#create) | **POST** `/webhooks` | Create Webhook
[**get**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#get) | **GET** `/webhooks/{webhookId}` | Retrieve Webhook details
[**delete**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#delete) | **DELETE** `/webhooks/{webhookId}` | Delete a Webhook
[**list**](https://github.com/apivideo/api.video-python-client/blob/main/docs/WebhooksApi.md#list) | **GET** `/webhooks` | List all webhooks




### Models

 - [AccessToken](https://github.com/apivideo/api.video-python-client/blob/main/docs/AccessToken.md)
 - [AdditionalBadRequestErrors](https://github.com/apivideo/api.video-python-client/blob/main/docs/AdditionalBadRequestErrors.md)
 - [AnalyticsAggregatedMetricsResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsAggregatedMetricsResponse.md)
 - [AnalyticsAggregatedMetricsResponseContext](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsAggregatedMetricsResponseContext.md)
 - [AnalyticsAggregatedMetricsResponseContextTimeframe](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsAggregatedMetricsResponseContextTimeframe.md)
 - [AnalyticsData](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsData.md)
 - [AnalyticsMetricsBreakdownResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsBreakdownResponse.md)
 - [AnalyticsMetricsBreakdownResponseContext](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsBreakdownResponseContext.md)
 - [AnalyticsMetricsBreakdownResponseData](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsBreakdownResponseData.md)
 - [AnalyticsMetricsOverTimeResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsOverTimeResponse.md)
 - [AnalyticsMetricsOverTimeResponseContext](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsOverTimeResponseContext.md)
 - [AnalyticsMetricsOverTimeResponseData](https://github.com/apivideo/api.video-python-client/blob/main/docs/AnalyticsMetricsOverTimeResponseData.md)
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
 - [FilterBy](https://github.com/apivideo/api.video-python-client/blob/main/docs/FilterBy.md)
 - [FilterBy1](https://github.com/apivideo/api.video-python-client/blob/main/docs/FilterBy1.md)
 - [FilterBy2](https://github.com/apivideo/api.video-python-client/blob/main/docs/FilterBy2.md)
 - [Link](https://github.com/apivideo/api.video-python-client/blob/main/docs/Link.md)
 - [LiveStream](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStream.md)
 - [LiveStreamAssets](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamAssets.md)
 - [LiveStreamCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamCreationPayload.md)
 - [LiveStreamListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/LiveStreamListResponse.md)
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
 - [RefreshTokenPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/RefreshTokenPayload.md)
 - [RestreamsRequestObject](https://github.com/apivideo/api.video-python-client/blob/main/docs/RestreamsRequestObject.md)
 - [RestreamsResponseObject](https://github.com/apivideo/api.video-python-client/blob/main/docs/RestreamsResponseObject.md)
 - [TokenCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/TokenCreationPayload.md)
 - [TokenListResponse](https://github.com/apivideo/api.video-python-client/blob/main/docs/TokenListResponse.md)
 - [TooManyRequests](https://github.com/apivideo/api.video-python-client/blob/main/docs/TooManyRequests.md)
 - [UnrecognizedRequestUrl](https://github.com/apivideo/api.video-python-client/blob/main/docs/UnrecognizedRequestUrl.md)
 - [UploadToken](https://github.com/apivideo/api.video-python-client/blob/main/docs/UploadToken.md)
 - [Video](https://github.com/apivideo/api.video-python-client/blob/main/docs/Video.md)
 - [VideoAssets](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoAssets.md)
 - [VideoClip](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoClip.md)
 - [VideoCreationPayload](https://github.com/apivideo/api.video-python-client/blob/main/docs/VideoCreationPayload.md)
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



## Have you gotten use from this API client?

Please take a moment to leave a star on the client

This helps other users to find the clients and also helps us understand which clients are most popular. Thank you!

## Contribution

Since this API client is generated from an OpenAPI description, we cannot accept pull requests made directly to the repository. If you want to contribute, you can open a pull request on the repository of our [client generator](https://github.com/apivideo/api-client-generator). Otherwise, you can also simply open an issue detailing your need on this repository.