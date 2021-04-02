# VideostatusIngest

Details about the capturing, transferring, and storing of your video for use immediately or in the future.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | There are three possible ingest statuses. missing - you are missing information required to ingest the video. uploading - the video is in the process of being uploaded. uploaded - the video is ready for use. | [optional] 
**filesize** | **int** | The size of your file in bytes. | [optional] 
**received_bytes** | [**[BytesRange]**](BytesRange.md) | The total number of bytes received, listed for each chunk of the upload. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


