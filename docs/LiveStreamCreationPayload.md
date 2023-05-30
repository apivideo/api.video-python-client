# LiveStreamCreationPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Add a name for your live stream here. | 
**record** | **bool** | Whether you are recording or not. True for record, false for not record. | [optional]  if omitted the server will use the default value of False
**public** | **bool** | Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/docs/private-videos). | [optional] 
**player_id** | **str** | The unique identifier for the player. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


