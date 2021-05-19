# Pick a thumbnail from your video's timeline to use instead of uploading an image
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

# Set variables, you need the video ID for the video you want to add a thumbnail to.
api_key = "your api key here"
video_id = "video ID for video to pick thumbnail for here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

videos_api = VideosApi(client)

# Choose a time from your video to use as the thumbnail. 
video_thumbnail_pick_payload = {
    "timecode": "00:00:10:000"
}

response = videos_api.pick_thumbnail(video_id, video_thumbnail_pick_payload)
print(response)
