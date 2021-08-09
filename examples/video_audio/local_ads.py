import apivideo, apiaudio, ffmpeg
import os, json, csv, time, sys, webbrowser
from pydub import AudioSegment
from pydub.playback import play
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException


# Functions

# Get the keys from the user 
def get_aflo_key():
    while True:
        aflo = input("Enter your aflorithmic API key (available at https://console.api.audio/): ")
        if len(aflo) < 32 or len(aflo) > 32:
            print("The aflorithmic API key is not correct, please try again.")
        else: 
            return aflo
            break

def get_apivideo_key():
    while True:
        api_video = input("Enter your api.video API key (available at https://my.api.video/: ")
        if len(api_video) < 43 or len(api_video) > 43:
            print("The api.video API key is not correct, please try again.")
        else:
            return api_video

# Choose an .mp4 to add sound to. MP4 is easier to work with when you need to combine videos, so it's the only format accepted. 
# The video you want to combine must be in the same folder the application is running in.
def choose_video(): 
    filelist = os.listdir('.')
    while True:
        for item in filelist:
            if item.endswith(".mp4"):
                print(item)
        filename = input("Please select the video you want to use. \n")
        if filename in filelist:
            return filename
        else: 
            print("That's not a file. Please type the name of the file as you see it listed.\n")

# If you have multiple scripts you can choose the one you want from the Scripts folder.
def choose_script():
    filelist = os.listdir('Scripts')
    while True:
        print(filelist)
        filename = input("Please select the script you want to use by typing its complete name. \n")
        if filename in filelist:
            f = open('Scripts/' + filename)
            print(f.read())
            use = input("Is this the script you wanted to use? Type YES or NO. \n")
            if use.upper() == 'YES':
                print("Great! Let's move on to personalizing your content!")
                return 'Scripts/' + filename
            elif use.upper() == 'NO':
                print("Okay, try again.")

# Choose the csv file you'll use for personalization.
def choose_personalization():
    filelist = os.listdir('Personalization')
    while True:
        print(filelist)
        filename = input("Please select the .csv file you want to use for personalization. \n")
        if filename in filelist:
            for i in range(3):
                f = open('Personalization/' + filename)
                line = f.readlines()
                print(line[i])
            f.close()
            use = input("These are the first three lines of the file you picked. Is this the file you wanted to use? Type YES or NO. \n")
            if use.upper() == 'YES':
                print("Great! Let's move on to creating the audio track!")
                return 'Personalization/' + filename
            elif use.upper() == 'NO':
                print("Okay, try again.")

# When you set up a script for use, you can provide some information about that script. This helps with set up
# and returns a list of all the variables with their values. 
def get_script_details():
    print("To set up the script, we need a few details. \n")
    scriptName = "a"
    moduleName = "a"
    projectName = "a"

    while True:
        scriptName = input("What do you want to name your script? Type it in. \n")
        print("You typed: ", scriptName)
        response = input("Is this the name you wanted to use? Type YES or NO. \n")
        if response.upper() == 'YES':
            print("Great, let's get the other information we need!")
            break
        else:
            print("Ok, try again.")

    while True:
        moduleName = input("What do you want to name your module? Type it in. \n")
        print("You typed: ", moduleName)
        response = input("Is this the name you wanted to use? Type YES or NO. \n")
        if response.upper() == 'YES':
            print("Great, let's get the other information we need!")
            break
        else:
            print("Ok, try again.")
    
    while True:
        projectName = input("What do you want to name your project? Type it in. \n")
        print("You typed: ", projectName)
        response = input("Is this the name you wanted to use? Type YES or NO. \n")
        if response.upper() == 'YES':
            print("Great, that's everything we need!")
            break
        else:
            print("Ok, try again.")

    return [scriptName, moduleName, projectName]

# After you choose a track, it's easier to combine if it's a .wav. This makes the file playable using PyDub and returns a PyDub object. 
# The .wav file can then be used. 
def check_audio_convert_track():
    while True:
        audio_check = input("Type PLAY to hear the sample now. \n")
        if audio_check.upper() == "PLAY":
            track = AudioSegment.from_mp3('Audio/sample.mp3')
            play(track)
            ready = input("Does the track sound the way you wanted? Type YES or NO. For NO, you'll have to start over again. \n")
            if ready.upper() == "YES":
                print("Great! Let's continue on to building the sample video!")
                return track
            if ready.upper() == "NO":
                print("Okay. The program will exit now. You'll need to figure out what tweaks to make to your script and voice.")
                sys.exit()
            else:
                print("That's not a valid response.")
        else: 
            print("That's not a valid entry.")

def make_video(video, wav_track, title):
    input_video = ffmpeg.input(video)
    input_audio = ffmpeg.input(wav_track)
    title = title + ".mp4"
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(title).run()
    print("A video with the title " + title + " was added to this folder.")

def add_video_return_mp4(video_title, av_client, item, vid_description):
    videos_api = VideosApi(av_client)

    item_values = item.values()
    item_list = list(item_values)

    video_create_payload = {
        "title": video_title,
        "description": vid_description,
        "public": True,
        "tags": item_list
    }

# Create the container for your video and print the response
    response = videos_api.create(video_create_payload)

# Retrieve the video ID, you can upload once to a video ID
    video_id = response["video_id"]

# Prepare the file you want to upload. Place the file in the same folder as your code.
    file = open(video_title, "rb")

# Upload your video. This handles videos of any size. The video must be in the same folder as your code and 1080p. 
# If you want to upload from a link online, you need to add the source parameter when you create a new video.
    video_response = videos_api.upload(video_id, file)
    url = video_response['assets']['player']
    return(url)    


# Welcome and Instructions
print("--------------------------------------------------------------")
print("*          HELLO AND WELCOME TO THE AD LOCALIZER !           *")
print("*   This tool lets you take a video and add a voice over     *")
print("*   that can be personalized with information read from a    *")
print("*   .csv file containing the personalization information.    *")
print("*   Use the example content provided to start with, then try *")
print("*   your own!                                                *")
print("*   NOTE: You can exit the program at any time by typing     *")
print("*   CTRL-C                                                   *")
print("--------------------------------------------------------------")

# Collect API Keys 

print("To get started, you'll need an api.video API key and an aflorithmic.ai API key.")
aflo_key = get_aflo_key()
api_video = get_apivideo_key()

# Authenticate
av_client = apivideo.AuthenticatedApiClient(api_video)
av_client.connect()
apiaudio.api_key = aflo

print("Thanks! Now you're ready to choose your video. Your video must be in the same folder as this application.")
print("Pick your video. \n")

# Choose Video
video = choose_video()

# Choose Script
script = choose_script()

# Create Script
script_details = get_script_details()
text = open(script, "r")
text = text.read()

script = apiaudio.Script().create(scriptText=text, scriptName=script_details[0], moduleName=script_details[1], projectName=script_details[2])

# Personalization 
print("You can personalize your script by reading in values from a .csv file to your script. \n")
csv_f = choose_personalization()

# Create speech. Choose a voice! https://library.api.audio/speakers

# Set up the csv file for use.
audience_combinations = []
with open(csv_f, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        audience_combinations.append(row)

i = 0
vid_description = ""

csv_header = {"Video": "Video Title", "MP4 Link": "MP4 Link Here"}
with open('all_vid_links.csv', 'w') as f: 
    w = csv.DictWriter(f, csv_header.keys())
    w.writeheader()
    w.writerow(csv_header)

while True:
    vid_description = input("Before we create the audio track, provide a brief description to describe the videos in the series we'll create. \n")
    keep_it = input(vid_description + " --- Is that the description you want? Type YES or NO. \n")
    if keep_it.upper() == "YES":
        print("Great! We're ready to work on the audio track now. Hang on a few moments while we process the first track.")
        break
    else: 
        print("Okay, try again.")

for item in audience_combinations:
    time.sleep(1)
    r = apiaudio.Speech().create(
        scriptId=script.get("scriptId"),
        voice="Aria",
        speed=100,
        silence_padding=0,
        audience=[item]
    )

    template = "copacabana"

    r = apiaudio.Mastering().create(
        scriptId=script.get("scriptId"), soundTemplate=template, audience=[item]
    )

    file = apiaudio.Mastering().download(
        scriptId=script.get("scriptId"),
        parameters=item,
        destination="Audio/",
    )
    
    print(f"✨ Mastered file for template {template} ✨")
    print(file)

    if i == 0: 
        
        new_file = os.path.join(os.path.dirname(file), "sample.mp3")
        os.rename(file, new_file)

        print("You have generated your first audio file. It's in the Audio folder and we've named it 'sample.mp3.'")
        print("Let's make sure it sounds the way you want.")
        wav_track = check_audio_convert_track()
        wav_track.export("Audio/sample.wav", format="wav")
        vid_list = video.split('.')
        video_title = vid_list[0]
        print("We're going to combine the video and the audio now. The video will appear in the same folder as your application title " + video_title + "-sample")
        make_video(video, 'Audio/sample.wav', video_title + "-sample")
        link_mp4 = add_video_return_mp4(video_title + "-sample.mp4", av_client, item, vid_description)
        print("Please watch the sample video that we'll open for you in the webbrowser. Then return to the terminal here. \n")
        webbrowser.open(link_mp4)
        while True:
            answer = input("Are the video and audio correct? You will have to start over if not. Type YES or NO. \n")
            if answer.upper() == "YES":
                print("Great, we'll start creating the videos in bulk and uploading to api.video now.")
                break
            if answer.upper() == "NO":
                print("You will have to go back and figure out what's wrong with the video or audio. Exiting now.")
                sys.exit()
            else:
                print("That's not a valid response, try again.")
        
    else: 
        # Convert the audio file so we can combine it. 
        counter = str(i)
        vid_list = video.split('.')
        audio_title = "Audio/" + vid_list[0] + "-audio" + ".wav"
        wav_track = AudioSegment.from_mp3(file)
        wav_track.export(audio_title, format="wav")

        # Make a video 
        video_title = vid_list[0] + counter
        make_video(video, audio_title, video_title)
        link_mp4 = add_video_return_mp4(video_title + ".mp4", av_client, item, vid_description)
        my_dict = {"Video": video_title + ".mp4", "MP4 Link": link_mp4}
        with open('all_vid_links.csv', 'a') as f: 
            w = csv.DictWriter(f, my_dict.keys())
            w.writerow(my_dict)
            
        # Upload the video and delete it from here
        os.remove(video_title + ".mp4")
        print("Video " + video_title "added!")


