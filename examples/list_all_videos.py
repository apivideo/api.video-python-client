import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you rather like to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Retrieve a list of all videos. 

videos_api = VideosApi(client)
videos = videos_api.list()

print(videos)
