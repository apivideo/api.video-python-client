# LiveStreamCreationPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Add a name for your live stream here. | 
**record** | **bool** | Whether you are recording or not. True for record, false for not record. | [optional]  if omitted the server will use the default value of False
**public** | **bool** | BETA FEATURE Please limit all public &#x3D; false (\&quot;private\&quot;) livestreams to 3,000 users. Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. | [optional] 
**player_id** | **str** | The unique identifier for the player. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


