# Update information about your live stream. For example you can change whether you record it, or have it presented publicly. 
import apivideo
from apivideo.apis import LiveStreamsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
live_stream_id = "your live stream id here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use live streams
live_stream_api = LiveStreamsApi(client)

# Add the details you want to update to a dictionary
live_stream_update_payload = {
    "public": True,
    "record": True,
    "name": "Bob III"    
}

# Update the live stream
response = live_stream_api.update(live_stream_id, live_stream_update_payload)
print(response)
