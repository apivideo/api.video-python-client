
# Create a live stream. 
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

live_stream_api = LiveStreamsApi(client)

live_stream_creation_payload = {
    "record": False,
    "name": "Bob"
}

# Create the live stream
response = live_stream_api.create(live_stream_creation_payload)
print(response)
