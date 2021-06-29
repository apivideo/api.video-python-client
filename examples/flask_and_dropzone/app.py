# Imports 
import os
import apivideo
from apivideo.apis import VideosApi
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# You can do this for extra security. MAX_CONTENT_LENGTH lets you set how big files can be. 
# UPLOAD_EXTENSIONS lets you limit what types of files can be uploaded. 
app.config['MAX_CONTENT_LENGTH'] = 5000 * 5000 * 100000
app.config['UPLOAD_EXTENSIONS'] = ['.mov', '.mp4', '.m4v', '.jpm', '.jp2', '.3gp', '.3g2', '.mkv', '.mpg', '.ogv',
                                   '.webm', '.wmv']
app.config['UPLOAD_PATH'] = 'uploads'

# If a file is too big, you'll get this. 
@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

# State what template you want to show
@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/', methods=['POST'])
def upload_file():
  
# Retrieve files and form data, they are in two separate parts of the request info from Flask. 
    my_files = request.files
    api_key = request.form['API Key']

# The files are in an immutable multi-dictionary, so loop through to grab them all. 
    for item in my_files:
        uploaded_file = my_files.get(item)

# Check if the file name was left blank or isn't in the extensions list. 
        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

# Start up the client and connect 
        client = apivideo.AuthenticatedApiClient(api_key)
        client.connect()

# Set up to use the videos endpoint
        videos_api = VideosApi(client)

# Add the file name from the FileStorage object from Flask
        video_create_payload = {
            "title": uploaded_file.filename,
        }

# Create a video container to upload your video into and retrieve the video ID for the container
        response = videos_api.create(video_create_payload)
        video_id = response["video_id"]

# Upload your file as a stream. NOTE! IMPORTANT! If you are uploading a big file, this will take awhile if it's over 128MB.
        video_response = videos_api.upload(video_id, uploaded_file.stream)
    return redirect(url_for('index'))
