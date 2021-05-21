# List all sessions for a video ID
import apivideo
from apivideo.apis import RawStatisticsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

rawstats_api = RawStatisticsApi(client)

# Retrieve all sessions for your video ID
response = rawstats_api.list_video_sessions(video_id)
print(response)