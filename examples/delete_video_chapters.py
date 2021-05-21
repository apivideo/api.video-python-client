# Delete a set of chapters for a specific language on a video
import apivideo
from apivideo.apis import ChaptersApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
video_id = "your video ID here"
language = "valid BCP 47 representation of language you want to delete (ex. 'en')"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

chapter_api = ChaptersApi(client)

# Delete the chapter set 
response = chapter_api.delete(video_id, language)
print(response)
