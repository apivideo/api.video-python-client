# Get information about video chapters for a specific language on a video.
import apivideo
from apivideo.apis import ChaptersApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

chapter_api = ChaptersApi(client)

# If you choose a language variation, for chapters it is shortened to just be the language. For example 'English Great Britain'
# which would be "en-GB" would be shortened to "en."
language = "en"

# Retrieve information about video chapters in the specified language. (If there aren't chapters the response will inform you 
# of this.)
response = chapter_api.get(video_id, language)
print(response)
