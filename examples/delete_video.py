# Delete a video using its video ID
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

videos_api = VideosApi(client)

title = "Sample AVI Video"

# List videos that have the exact, unique title you wanted to delete
videos = videos_api.list(title=title)

# Get list of videos out of response object or single item depending on whether you filtered
videos = videos['data']

# In this case, let's assume we know there's only one video with the title we filtered for. 
print(videos[0]['video_id'])
        
# Delete the video
response = videos_api.delete(videos[0]['video_id'])
print(response)
