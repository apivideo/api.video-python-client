# Add a caption VTT file to your video. The file should be in the same folder as your code.
import apivideo
from apivideo.apis import CaptionsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "video ID for the video you want to add a caption to"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use captions
captions_api = CaptionsApi(client)

# Set up payload to send 
language = "en-GB"
file = open("doug_en-GB.vtt", "rb")

response = captions_api.upload(video_id, language, file)
print(response)