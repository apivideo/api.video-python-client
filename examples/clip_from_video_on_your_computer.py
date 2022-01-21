import apivideo
from apivideo.apis import VideosApi
from apivideo.model.bad_request import BadRequest
from pprint import pprint

client = apivideo.AuthenticatedApiClient("your API key here")

client.connect()

videos_api = VideosApi(client)

video_create_payload = {
    "title": "Clip from a video on your computer",
    "description": "Clip from video you are uploading for the first time",
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

# Retrieve the video ID, you can upload once to a video ID
video_id = response["video_id"]

# Prepare the file you want to upload. Place the file in the same folder as your code.
file = open("video_you_want_a_clip_from.mp4", "rb")

# Upload your video. This handles videos of any size. The video must be in the same folder as your code. 
# If you want to upload from a link online, you need to add the source parameter when you create a new video.
video_response = videos_api.upload(video_id, file)

print("Uploaded Video", video_response)
