# Upload an image as a thumbnail for your video
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

# Set variables, you need the video ID for the video you want to add a thumbnail to.
api_key = "your api key here"
video_id = "your video ID here"

# Open the file you want to use as the thumbnail in binary format. Your image must
# have an extension that is one of these: jpeg, jpg, JPG, JPEG 
file = open("your jpg", "rb")

# Authenticate and set up your client 
client = apivideo.AuthenticatedApiClient(api_key)

client.connect()

videos_api = VideosApi(client)

# Send the thumbnail and video ID to API video. The thumbnail is added to the video associated with the ID 
# you provide. You can check on your dashboard to make sure the thumbnail was added. 

response = videos_api.upload_thumbnail(video_id, file)
print(response)
