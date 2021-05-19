# List all sessions for a live stream ID
import apivideo
from apivideo.apis import RawStatisticsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
live_stream = "your live stream ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use raw statistics
rawstats_api = RawStatisticsApi(client)

# Send the request for session information
response = rawstats_api.list_live_stream_sessions(live_stream)
print(response)
