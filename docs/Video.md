# Video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** | The unique identifier of the video object. | [optional] 
**title** | **str** | The title of the video content.  | [optional] 
**description** | **str** | A description for the video content.  | [optional] 
**published_at** | **str** | The date and time the API created the video. Date and time are provided using ISO-8601 UTC format. | [optional] 
**updated_at** | **datetime** | The date and time the video was updated. Date and time are provided using ISO-8601 UTC format. | [optional] 
**tags** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | One array of tags (each tag is a string) in order to categorize a video. Tags may include spaces.   | [optional] 
**metadata** | [**[Metadata]**](Metadata.md) | Metadata you can use to categorise and filter videos. Metadata is a list of dictionaries, where each dictionary represents a key value pair for categorising a video.   | [optional] 
**source** | [**VideoSource**](VideoSource.md) |  | [optional] 
**assets** | [**VideoAssets**](VideoAssets.md) |  | [optional] 
**player_id** | **str** | The id of the player that will be applied on the video.  | [optional] 
**public** | **bool** | Defines if the content is publicly reachable or if a unique token is needed for each play session.  | [optional] 
**panoramic** | **bool** | Defines if video is panoramic.  | [optional] 
**mp4_support** | **bool** | This lets you know whether mp4 is supported. If enabled, an mp4 URL will be provided in the response for the video.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


