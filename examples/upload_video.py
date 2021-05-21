import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

# Set up the authenticated client
client = apivideo.AuthenticatedApiClient(api_key)

# if you rather like to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()

videos_api = VideosApi(client)

# Create the payload with video details 
video_create_payload = {
    "title": "Client Video Test",
    "description": "Client test",
    "public": True,
    "tags": ["bunny"]
}

# Create the container for your video and print the response
response = videos_api.create(video_create_payload)
print("Video Container", response)

# Retrieve the video ID, you can upload once to a video ID
video_id = response["video_id"]

# Prepare the file you want to upload. Place the file in the same folder as your code.
file = open("sample-mov-file.mov", "rb")

# Upload your video. This handles videos of any size. If you want to upload from a link online, you need to u
video_response = videos_api.upload(video_id, file)

print("Uploaded Video", video_response)
