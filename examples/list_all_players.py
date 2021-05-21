# List all players.
import apivideo
from apivideo.apis import PlayerThemesApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

player_api = PlayerThemesApi(client)

# Retrieve a list of all players
response = player_api.list()
print(response)