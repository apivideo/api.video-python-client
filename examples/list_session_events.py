# Retrieve all details for a session by session ID
import apivideo
from apivideo.apis import RawStatisticsApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
session_id = "your session ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()

rawstats_api = RawStatisticsApi(client)

# Retrieve session details
response = rawstats_api.list_session_events(session_id)
print(response)
