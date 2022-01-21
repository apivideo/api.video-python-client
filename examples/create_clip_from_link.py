import apivideo
from apivideo.apis import VideosApi
from apivideo.model.bad_request import BadRequest
from pprint import pprint

client = apivideo.AuthenticatedApiClient("your API key here")

client.connect()

videos_api = VideosApi(client)

video_create_payload = {
    "title": "source_download_with_clip",
    "description": "source_download_with_clip",
    "source": "http://techslides.com/demos/sample-videos/small.mp4",
    "public": True,
    "panoramic": False,
    "clip": {
        "start_timecode": "00:00:02",
        "end_timecode": "00:00:05"
    }
}

# Create the container for your video and print the response
response = videos_api.create(video_create_payload)
print("Video Container", response)
