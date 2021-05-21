# You can retrieve details about captions available for an ID.
import apivideo
from apivideo.apis import CaptionsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here" 

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()

captions_api = CaptionsApi(client)

# Set up language you want to see captions for
language = "en-GB"

response = captions_api.get(video_id, language)
print(response)