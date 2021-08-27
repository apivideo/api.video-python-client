# Use a delegated token to upload a video
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException 

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()
videos_api = VideosApi(client)

# Setting up variables for the path to the video and the token you already created
path = 'path to video'
token = 'your token'

# Opening your vieo file so it can be sent
file = open(path, "rb")

# Sending file. 
response = videos_api.upload_with_upload_token(token, file)
print(response)
