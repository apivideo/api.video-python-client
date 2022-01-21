import apivideo
from apivideo.apis import WatermarksApi
from apivideo.apis import VideosApi
from apivideo.model.video import Video
from apivideo.model.bad_request import BadRequest
from pprint import pprint

client = apivideo.AuthenticatedApiClient("your API key here")

client.connect()

watermarks_api = WatermarksApi(client)

file = open('your_watermark_here.png', 'rb') # file_type | The .jpg or .png image to be added as a watermark.

api_response = watermarks_api.upload(file)        
pprint(api_response)
pprint(api_response['watermark_id'])

watermark_id = api_response['watermark_id']

videos_api = VideosApi(client)

video_creation_payload = {
    "title":"Sample video",
    "description": "Show a watermarked video",
    "watermark": {
        "id": watermark_id,
        "top":"20px",
        "left":"20px",
        "opacity":"70%",
    },
}
api_response = videos_api.create(video_creation_payload)
video_id = api_response["video_id"]

file = open("video_to_watermark.mp4", "rb")

video_response = videos_api.upload(video_id, file)
print("Uploaded Video", video_response)
