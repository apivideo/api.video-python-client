# Update details about how your player looks. 
import apivideo
from apivideo.apis import PlayerThemesApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

player_api = PlayerThemesApi(client)

player_id = "your player ID here"

player_theme_update_payload = {
    "track_unplayed": "rgba(240, 255, 255, .1)",
    "track_played": "rgba(255, 240, 255, .95)"    
}

response = player_api.update(player_id, player_theme_update_payload)
print(response)