# List all live streams 
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
live_stream = "your live stream ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

live_stream_api = LiveStreamsApi(client)

# Delete live stream thumbnail
response = live_stream_api.delete_thumbnail(live_stream)
print(response)
