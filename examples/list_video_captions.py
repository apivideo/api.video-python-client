# List all available captions for a video ID
import apivideo
from apivideo.apis import CaptionsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here" 

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()

# Set up to use captions
captions_api = CaptionsApi(client)

# List all captions for the video ID
response = captions_api.list(video_id)
print(response)