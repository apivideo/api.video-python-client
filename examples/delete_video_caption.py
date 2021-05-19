# Delete a caption in a specified language.
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

language = "en-GB"

# List all captions for the video ID
response = captions_api.delete(video_id, language)
print(response)