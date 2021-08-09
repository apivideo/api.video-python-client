# api.audio and api.video

This project combines api.audio and api.video. You use api.audio to create audio tracks via AI. The AI can read messages that you personalize by providing
input from a .csv file for all the spots you want to change from track to track. These can all be added over the same video to make messages that are
localized to a specific area.

You'll get to walk through:

1. Choosing a script, csv spreadsheet for use with personalizing ads and video to use for your project.
2. Creating a single audio sample.
3. Checking the audio sample.
4. Converting your sample to a .wav.
5. Combining audio with a video file.
6. Adding tags to the video file so you can search for it later.
7. Checking the new video file.
8. Combining and uploading each video to apivideo.
9. Creating a spreadsheet with each video and a link to it provided. 

You will need to add an 'Audio' folder when you download this project because the program will try to store audio files there. It's not added here,
since it would just be an empty folder. 

You will also need this video: 
https://embed.api.video/vod/vi61TFbqHlfb37gR4fEIQf72

It's a silent video for combining with the audio tracks you'll be creating. This video needs to be stored in the same folder you run the code sample from. 

# Prerequisites 

For this project, you're going to need: 

* An api.video account - [Sign up here!](https://api.video)
* An aflorithmic.ai account - [Sign up here!](https://console.api.audio/)

# Installation

We will use the [api.video Python client](https://github.com/apivideo/python-api-client) and [Aflorithic.ai's apiaudio library](https://docs.api.audio/recipes).

Installation for api.video: 
```pip install api.video```

Installation for Aflorithmic:
```pip install -U apiaudio```

## ffmpeg installation
If you want to run the project as-is, you'll also need to install ffmpeg. These instructions help you with installation on a mac. What you'll want to do is make sure you have brew installed. Then it's very easy, you just install with:

```brew install ffmpeg``` 

You need to install ffmpeg before you install the next two items.

## pydub and pyaudio installation
pydub and pyaudio can also be difficult to install, depending on your set up and what you've tried to install already. If you made the mistake of trying to install these before installing ffmpeg, then what you would do is first run:

```brew remove portaudio```

Then, reinstall this like so: 

```brew install port audio``` 

After these steps, you should be able to successfully install the modules you'll need. Here's the commands: 

```brew pyaudio```

and 

```brew pydub```

# Walkthrough 

To run the program, just download the folder, add the empty Audio folder, add the video from the link (it needs to be in .mp4 format, which is what it will
download as).

Then run it and follow the instructions! You will be able to change the csv file, the script, and the video for use with your own project, or you can pull
the code sample apart and use pieces of it for your own project. 
