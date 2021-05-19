# Get details about a live stream using its ID 
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
live_stream_id = "your live stream ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use live streams
live_stream_api = LiveStreamsApi(client)

# Retrieve live stream details
response = live_stream_api.get(live_stream_id)
print(response)