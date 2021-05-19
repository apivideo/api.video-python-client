# You can set whether captions are automatically turned on or not and for what
# language they are turned on or not. 
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

# Set up payload to send 
language = "en-GB"
captions_update_payload = {"default": True}

response = captions_api.update(video_id, language, captions_update_payload)
print(response)