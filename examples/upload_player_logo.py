# Upload a logo for your player and add a link the user navigates to when they click your logo.
import apivideo
from apivideo.apis import PlayerThemesApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

player_api = PlayerThemesApi(client)

# Add the file you want to use as a logo. 
# It must be no bigger than h: 100px, w: 200px, no larger than 200KB. 

file = open("image2.jpg", "rb")

# Optionally, you can add a link that the player will send the viewer to if they click on
# your logo. 
link = "https://google.com"

# ID for the player you want to add a logo to.
player_id = "your player ID here"

response = player_api.upload_logo(player_id, file, link)
print(response)
