# Upload an image to be a thumbnail for your live stream.
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
live_stream_id = "your live stream ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

live_stream_api = LiveStreamsApi(client)

# Open image to use as thumbnail, should be in same directory as your code 
file = open("image1.jpg", "rb")

# Upload the thumbnail
response = live_stream_api.upload_thumbnail(live_stream_id, file)
print(response)
