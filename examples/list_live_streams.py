# List all live streams 
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use live streams
live_stream_api = LiveStreamsApi(client)

# List all live stream details
response = live_stream_api.list()
print(response)