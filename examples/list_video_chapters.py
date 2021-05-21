# List details about all sets of chapters for a video.
import apivideo
from apivideo.apis import ChaptersApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

chapter_api = ChaptersApi(client)

# Retrieve details about sets of chapters for a video.
response = chapter_api.list(video_id)
print(response)
