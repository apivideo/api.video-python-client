# API.VIDEO COMMANDLINE 
This tool allows you to use all the features of the Python API client for api.video from the commandline. You can tweak and customize it, and we also accept
suggestions for new features to add. 

# Installation

1. It's recommended that you create a virtual environment. 
2. In your virtual environment, you need to pip install click and pip install api.video. 
3. Add these files. 
4. Add a folder at the same level as these files called 'videos' - this isn't required, but it's what I used to upload videos from. You can upload from anywhere
   else too though.

# Configure the commandline
To use the commandline, the first thing you need to do is add your API key. In a terminal type: 

`python av_cli.py config`

Follow the instructions to add your api key. You should now be able to use all the features of the commandline. 

You can type: 
`python av_cli.py --help` 

To get an exhaustive list of available commandline commands. 

You can also add --help after any of the individual commands for more information, like this: 
`python av_cli.py liststreams --help` 

Usage will be stated at the top to show you how to structure each command. 

You can review api.video documentation for details about available parameters per endpoint. 

**NOTE:** To use the parameters from the documentation, change any instances of camel case to snake case. So if it says sortBy it would be sort_by. 

# Documentation

[docs.api.video/reference/apivideo-api-reference](https://docs.api.video/reference/apivideo-api-reference)
