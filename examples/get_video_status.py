# Check the status of a video by video ID

import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "video ID to get the status of here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

videos_api = VideosApi(client)

# Get the status of your video
response = videos_api.get_status(video_id)
print(response)
