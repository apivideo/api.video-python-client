# Update details about your video
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "video ID for the video you want to update"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

videos_api = VideosApi(client)

# Set up payload with details you want to change. For a complete list of what's available
# see https://docs.api.video

video_update_payload = {
    'title': 'Sample AVI Video',
    'description': 'This video is for demo purposes.'
}

# Send data you want to update your video with
response = videos_api.update(video_id, video_update_payload)
print(response)
