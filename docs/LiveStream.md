# LiveStream

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_stream_id** | **str** | The unique identifier for the live stream. Live stream IDs begin with \&quot;li.\&quot; | 
**restreams** | [**[RestreamsResponseObject]**](RestreamsResponseObject.md) | Returns the list of RTMP restream destinations. | 
**name** | **str** | The name of your live stream. | [optional] 
**stream_key** | **str** | The unique, private stream key that you use to begin streaming. | [optional] 
**record** | **bool** | Whether you are recording or not. | [optional] 
**public** | **bool** | Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/docs/private-videos). | [optional] 
**assets** | [**LiveStreamAssets**](LiveStreamAssets.md) |  | [optional] 
**player_id** | **str** | The unique identifier for the player. | [optional] 
**broadcasting** | **bool** | Whether or not you are broadcasting the live video you recorded for others to see. True means you are broadcasting to viewers, false means you are not. | [optional] 
**created_at** | **datetime** | When the player was created, presented in ISO-8601 format. | [optional] 
**updated_at** | **datetime** | When the player was last updated, presented in ISO-8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


