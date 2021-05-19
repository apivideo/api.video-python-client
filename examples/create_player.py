# Create a player 
import apivideo
from apivideo.apis import PlayerThemesApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)
webhook_id = "webhook_1BZbMTJbngrkH5Rfn9DiV6"

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use webhooks
player_api = PlayerThemesApi(client)

# Create player payload. To use the parameters in the client, change them to have 
# the common structure for a Python parameter. For example enableApi becomes enable_api. 
# enableControls becomes enable_controls, and so on. 

player_theme_creation_payload = {
    "enable_api": True,
    "enable_controls": True,
    "force_autoplay": False,
    "hide_title": False,
    "force_loop": False,
    "text": "rgba(255, 255, 255, .95)",
    "link": "rgba(255, 0, 0, .95)",
    "link_hover": "rgba(255, 255, 255, .75)",
    "track_played": "rgba(255, 255, 255, .95)",
    "track_unplayed": "rgba(255, 255, 255, .1)",
    "track_background": "rgba(0, 0, 0, 0)",
    "background_top": "rgba(72, 4, 45, 1)",
    "background_text": "rgba(255, 255, 255, .95)"
}

# Create a webhook
response = player_api.create(player_theme_creation_payload)
print(response)