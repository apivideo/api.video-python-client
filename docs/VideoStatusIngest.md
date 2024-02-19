# VideoStatusIngest

Details about the capturing, transferring, and storing of your video for use immediately or in the future.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | There are four possible statuses depending on how you provide a video file: - &#x60;uploading&#x60; - the API is gathering the video source file from an upload. - &#x60;uploaded&#x60; - the video file is fully uploaded. - &#x60;ingesting&#x60; - the API is gathering the video source file from either a URL, or from cloning. - &#x60;ingested&#x60; - the video file is fully stored.  | [optional] 
**filesize** | **int, none_type** | The size of your file in bytes. | [optional] 
**received_bytes** | [**[BytesRange]**](BytesRange.md) | The total number of bytes received, listed for each chunk of the upload. | [optional] 
**received_parts** | [**VideoStatusIngestReceivedParts**](VideoStatusIngestReceivedParts.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


