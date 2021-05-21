# Create chapters for your video
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

# Choose language your chapters will be listed in and prepare file for upload
language = "en-GB"
file = open("chapters.vtt", "rb")

# Create chapters for your video
response = chapter_api.upload(video_id, language, file)
print(response)

