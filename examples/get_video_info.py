# Get details about a single video using its video ID
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "video ID for video you want info about here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

videos_api = VideosApi(client)

# Get details about a single video by video ID
response = videos_api.get(video_id)
print(response)
