import click, json, os, re, csv 
import apivideo
from apivideo.apis import VideosApi
from apivideo.apis import UploadTokensApi
from apivideo.apis import LiveStreamsApi
from apivideo.apis import CaptionsApi
from apivideo.apis import PlayerThemesApi
from apivideo.apis import RawStatisticsApi
from apivideo.apis import WebhooksApi
from apivideo.exceptions import ApiAuthException

class ApiKey(click.ParamType):
    name = 'api-key'

    def convert(self, value, param, ctx):
        if len(value) == 43:
            found = re.match(r'[0-9a-zA-Z]{43}', value)
        else: 
            self.fail(
                f'{value} is not a 43-character string.',
                param,
                ctx,
            )
        return value

def setClient(api_key):
    client = apivideo.AuthenticatedApiClient(api_key)
    return client
 
@click.group()
@click.option(
    '--api-key', '-a', type=ApiKey(),
    help="""Your api.video API key.""",
)
@click.option(
    '--config-file', '-c',
    type=click.Path(),
    default='~/.av_commandline.cfg',
)
@click.pass_context
def main(ctx, api_key, config_file):
    filename = os.path.expanduser(config_file)

    if not api_key and os.path.exists(filename):
        with open(filename) as cfg:
            api_key = cfg.read()

    ctx.obj = {
        'api_key': api_key,
        'config_file': filename,
    }

@main.command()
@click.pass_context
def config(ctx):
    """
        Store the api key in a file for use with the api.video API.
    """
    config_file = ctx.obj['config_file']

    api_key = click.prompt(
        "Please enter your api.video API key. We'll display what we have on file.",
        default=ctx.obj.get('api_key', '')
    )

    with open(config_file,'w') as cfg:
        cfg.write(api_key)

# VIDEOS 

## list videos 
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"title":"My Title"}'""")
@click.pass_context
def listvideos(ctx, payload):
    """
        List all videos in your account, or use a filtering option. All choices use snake case. For documentation
        containing camelcase for parameters, change them to snake case. Choices: \n
            * title - string, title of video \n
            * tags - list \n 
            * metadata - list of key:value pairs \n
            * description - string \n
            * live_stream_id - ID for the live stream that created the video \n
            * sort_by - string (asc or desc) \n
            * current_page - integer \n 
            * page_size - integer \n 
    """
    api_key = ctx.obj['api_key']

    kwargs = json.loads(payload)

    client = setClient(api_key)
    client.connect()

    from apivideo.apis import VideosApi
    videos_api = VideosApi(client)
    
    if kwargs:
        videos = videos_api.list(**kwargs)
    else:
        videos = videos_api.list()
    click.echo(videos)

## upload video
@main.command()
@click.option('--payload', default='{"title":"video upload CLI", "description":"default info"}')
@click.argument('filepath')
@click.pass_context
def uploadvideo(ctx, payload, filepath):
    """
        Upload a video to your account and provide info with a dictionary string. All choices use snake
        case. If you're using documentation showing camel case, convert it to snake case for this tool.
        You must provide the path to the file and a title for the upload. Everything else is optional.
        This command combines creating the video container and uploading the video, so you don't need to have
        the video_id.  \n
        * title - string
        * description - string
        * source - string
        * public - boolean
        * panoramic - boolean
        * mp4Support - boolean
        * player_id - string
        * tags - list of strings
        * metadata - list of key:value pairs
        * published_at - date-time
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    video_create_payload = json.loads(payload)

    # Create the container for your video and print the response
    response = videos_api.create(video_create_payload)
    print("Video Container", response)

    # Retrieve the video ID, you can upload once to a video ID
    video_id = response["video_id"]

    # Prepare the file you want to upload. Place the file in the same folder as your code.
    file = open(filepath, "rb")

    video_response = videos_api.upload(video_id, file)
    print("Video Upload Info", video_response)

## upload thumbnail for a video
@main.command()
@click.argument('videoid')
@click.argument('filepath')
@click.pass_context
def uploadthumb(ctx, videoid, filepath):
    """
        Choose a JPG to upload as your image. 
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    file = open(filepath, "rb")

    response = videos_api.upload_thumbnail(videoid, file)
    click.echo(response)

## pick thumbnail for a video
@main.command()
@click.argument('videoid')
@click.argument('payload', default='{"timecode":"00:00:01:000"}')
@click.pass_context
def pickthumb(ctx, videoid, payload):
    """
        Pick a thumbnail from a frame in the video timeline.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    payload = json.loads(payload)

    videos_api = VideosApi(client)

    response = videos_api.pick_thumbnail(videoid, payload)
    click.echo(response)

## show a video / get video details 
@main.command()
@click.argument('videoid')
@click.pass_context
def getvideo(ctx, videoid):
    """
        Retrieve details for a video using the video ID.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    response = videos_api.get(videoid)
    click.echo(response)

## delete a video 
@main.command()
@click.argument('videoid')
@click.pass_context
def deletevideo(ctx, videoid):
    """
        Delete a video using its video ID.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    response = videos_api.delete(videoid)
    click.echo(response)

## bulk delete videos
@main.command()
@click.argument('vidlist')
@click.pass_context
def bulkdelete(ctx, vidlist):
    """
        Delete list of videos presented by ID in a comma separated string.
    """
    vidlist = vidlist.replace(" ", "")
    del_list = vidlist.split(',')
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    for item in del_list:
        response = videos_api.delete(item)
        print(response)
    
## update a video
@main.command()
@click.argument('videoid')
@click.argument('payload')
@click.pass_context
def updatevideo(ctx, videoid, payload):
    """
        Update a video's details using its video ID.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    videos_api = VideosApi(client)

    payload = json.loads(payload)
    response = videos_api.update(videoid, payload)
    click.echo(response)

## show video status 
@main.command()
@click.argument('videoid')
@click.pass_context
def showvideostatus(ctx, videoid):
    """
        Show whether video is ready for playback.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()


    videos_api = VideosApi(client)

    response = videos_api.get_status(videoid)
    print(response)

# DELEGATED VIDEO

## list active tokens
@main.command()
@click.option ('--payload', default={}, help="Dictionary as string containing sorting choices.")
@click.pass_context
def listtokens(ctx, payload):
    """
        List all active delegated tokens. You can sort tokens by including a dictionary
        as a string. If you are reading documentation, instances of camelCase are snake case for this
        tool, so convert them before including them. Available choices are:
        * sort_by - string ('asc' or 'desc')
        * current_page - string
        * page_size - string
    """    

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    tokens_api = UploadTokensApi(client)

    kwargs = json.loads(payload)
    if kwargs:
        response = tokens_api.list(**kwargs)
    else:
        response = tokens_api.list()
    click.echo(response)

## generate upload token
@main.command()
@click.argument('ttl')
@click.pass_context
def createtoken(ctx, ttl):
    """
        Create an upload token. Choose ttl in seconds. If one is not selected, the token never 
        expires.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    tokens_api = UploadTokensApi(client)

    ttl = json.loads(ttl)

    response = tokens_api.create_token(ttl)
    click.echo(response)

## show upload token
@main.command()
@click.argument('token')
@click.pass_context
def gettoken(ctx, token):
    """
        Get details about a single token using the token's ID.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    tokens_api = UploadTokensApi(client)

    response = tokens_api.get_token(token)
    click.echo(response)    

## delete upload token
@main.command()
@click.argument('token')
@click.pass_context
def deletetoken(ctx, token):
    """
        Delete a token.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    tokens_api = UploadTokensApi(client)

    response = tokens_api.delete_token(token) 
    click.echo(response)   

## upload with upload token
@main.command()
@click.argument('path')
@click.argument('token')
@click.pass_context
def tokenupload(ctx, path, token):
    """
        Upload a video with a token. You must have created a token already. 
        You can edit its details afterwards with updatevideo.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    videos_api = VideosApi(client)

    file = open(path, "rb")

    response = videos_api.upload_with_upload_token(token, file)
    click.echo(response)

# LIVE STREAMS 

## list live streams
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"name":"My Live Stream", "sort_by":"asc"} '""")
@click.pass_context
def liststreams(ctx, payload):
    """
        List all the live streams in your account, or use a filtering option. All choices use snake case. For documentation
        containing camelcase for parameters, change them to snake case. Choices: \n
            * stream_key - string \n
            * name - string \n
            * sort_by - string \n
            * sort_order - string \n
            * current_page - string \n
            * page_size - string \n
    """
    api_key = ctx.obj['api_key']

    kwargs = json.loads(payload)

    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)
    
    if kwargs:
        live_streams = live_stream_api.list(**kwargs)
    else:
        live_streams = live_stream_api.list()
    click.echo(live_streams)

## create live stream
@main.command()
@click.argument('payload')
@click.pass_context
def createstream(ctx, payload):
    """
        Create a live stream with details about the stream. Add a JSON dictionary of details
        as a string. When you encounter camel case in the documentation, convert to camel case
        for your string.
    """

    api_key = ctx.obj['api_key']

    payload = json.loads(payload)

    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)

    response = live_stream_api.create(payload)
    click.echo(response)

## show live stream
@main.command()
@click.argument('livestreamid')
@click.pass_context
def getstream(ctx, livestreamid):
    """
        Retrieve details about a live stream using its ID.
    """

    api_key = ctx.obj['api_key']

    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)
    response = live_stream_api.get(livestreamid)
    click.echo(response)

## delete live stream
@main.command()
@click.argument('livestreamid')
@click.pass_context
def deletestream(ctx, livestreamid):
    """
        Delete a live stream. 
    """
    api_key = ctx.obj['api_key']

    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)
    response = live_stream_api.delete(livestreamid)
    click.echo(response)

## update live stream
@main.command()
@click.argument('livestreamid')
@click.argument('payload')
@click.pass_context
def updatestream(ctx, livestreamid, payload):
    """
        Update details about a live stream.
    """
    api_key = ctx.obj['api_key']

    client = setClient(api_key)
    client.connect()

    payload = json.loads(payload)
    live_stream_api = LiveStreamsApi(client)   
    response = live_stream_api.update(livestreamid, payload)
    print(response)

## upload live stream thumbnail
@main.command()
@click.argument('livestreamid')
@click.argument('filepath')
@click.pass_context
def uploadstreamthumb(ctx, livestreamid, filepath):
    """
        Choose a JPG to upload as your image. 
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)

    file = open(filepath, "rb")

    response = live_stream_api.upload_thumbnail(livestreamid, file)
    click.echo(response)

## delete live stream thumbnail
@main.command()
@click.argument('livestreamid')
@click.pass_context
def deletestreamthumb(ctx, livestreamid):
    """
        Delete a live stream thumbnail.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    live_stream_api = LiveStreamsApi(client)

    response = live_stream_api.delete_thumbnail(livestreamid)
    click.echo(response)

# CAPTIONS

## get video caption 
@main.command()
@click.argument('videoid')
@click.argument('language')
@click.pass_context
def getcaption(ctx, videoid, language):
    """
        Display caption for a video in a specific language. If available, the language specified is
        returned. Languages use BCP-47 representation. 
    """
    
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    captions_api = CaptionsApi(client)

    response = captions_api.get(videoid, language)
    click.echo(response)

## upload video caption
@main.command()
@click.argument('videoid')
@click.argument('language')
@click.argument('filepath')
@click.pass_context
def uploadcaption(ctx, videoid, language, filepath):
    """
        Upload a new .VTT caption file.
    """

    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    captions_api = CaptionsApi(client)
    file = open(filepath, "rb")

    response = captions_api.upload(videoid, language, file)
    click.echo(response)

## delete video caption
@main.command()
@click.argument('videoid')
@click.argument('language')
@click.pass_context
def deletecaption(ctx, videoid, language):
    """
        Delete caption for a language if it's there. Language tags are in
        BCP 47 representation.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    captions_api = CaptionsApi(client)

    response = captions_api.delete(videoid, language)
    click.echo(response)

## update video caption
@main.command()
@click.argument('videoid')
@click.argument('language')
@click.argument('payload')
@click.pass_context
def updatecaption(ctx, videoid, language, payload):
    """
        Set whether captions will be on or off for a particular language.
        Language tag is in BCP 47 representation.
    """
    payload = json.loads(payload)
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    captions_api = CaptionsApi(client)

    response = captions_api.update(videoid, language, payload)
    click.echo(response)

## list video captions 
@main.command()
@click.option('--querystring', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"sort_by":"asc"} '""")
@click.argument('videoid')
@click.pass_context
def listcaption(ctx, querystring, videoid):
    """
        List available captions for a video. If you include a dictionary, convert camel case to snake case for the choices.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    captions_api = CaptionsApi(client)

    querystring = json.loads(querystring)

    if querystring:
        response = captions_api.list(videoid, querystring)
    else:
        response = captions_api.list(videoid)
    click.echo(response)
  
# PLAYERS

## list all players
@main.command()
@click.option('--querystring', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"sort_by":"asc"} '""")
@click.pass_context
def listplayers(ctx, querystring):
    """
        List all players. If you add a dictionary, convert camel case to snake case. 
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    player_api = PlayerThemesApi(client)

    querystring = json.loads(querystring)

    if querystring:
        response = player_api.list(querystring)
    else:
        response = player_api.list()
    print(response)

## create a player
@main.command()
@click.argument('payload')
@click.pass_context
def createplayer(ctx, payload):
    """
        Create a new player.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    payload = json.loads(payload)
    player_api = PlayerThemesApi(client)  

    response = player_api.create(payload)
    print(response)

## get a player 
@main.command()
@click.argument('playerid')
@click.pass_context
def getplayer(ctx, playerid):
    """
        Get details about a specific player.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    player_api = PlayerThemesApi(client)

    response = player_api.get(playerid)
    print(response)

## delete a player
@main.command()
@click.argument('playerid')
@click.pass_context
def deleteplayer(ctx, playerid):
    """
        Delete a player.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    player_api = PlayerThemesApi(client)

    response = player_api.delete(playerid)
    print(response)

## update a player
@main.command()
@click.argument('playerid')
@click.argument('payload')
@click.pass_context
def updateplayer(ctx, playerid, payload):
    """
        Update details about a player.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    payload = json.loads(payload)
    player_api = PlayerThemesApi(client)
    response = player_api.update(playerid, **payload)
    print(response)


## upload a logo
@main.command()
@click.argument('playerid')
@click.argument('file')
@click.argument('link')
@click.pass_context
def uploadlogo(ctx, playerid, file, link):
    """
        Upload a custom logo.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    player_api = PlayerThemesApi(client)
    player_id = playerid
    file = open(file, "rb")
    response = player_api.upload_logo(player_id, file, link)
    print(response)

## delete a logo
@main.command()
@click.argument('playerid')
@click.pass_context
def deletelogo(ctx, playerid):
    """
        Delete uploaded logo.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()

    player_api = PlayerThemesApi(client)

    response = player_api.delete_logo(playerid)
    print(response)

# ANALYTICS

# list video player sessions 
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"sort_by":"asc"} '""")
@click.option('--csvfile', default=False, help="""Put true if you want a csv file of the output.""")
@click.argument('videoid')
@click.pass_context
def listvideosessions(ctx, videoid, payload, csvfile):
    """
        Retrieve all or a filtered list of video sessions by video ID and other attributes.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    rawstats_api = RawStatisticsApi(client)
   
    payload = json.loads(payload)

    if payload:
        response = rawstats_api.list_video_sessions(videoid, **payload)
    else:
        response = rawstats_api.list_video_sessions(videoid)
    print(response)

    if csvfile:
        response = response['data']
        with open('video_sessions_file.csv', 'w', newline='') as csv_file:
            fieldnames = ['Client Name', 'Client Type', 'Client Version', 'Device Model', 'Device Type', 'Device Vendor', 'City', 'Country', 'OS Name', 'OS Shortname', 'OS Version', 'Ref Medium', 'Ref Search Term', 'Ref Source', 'Ref URL', 'Session End', 'Session Loaded At', 'Session ID']
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()
            for item in response:
                writer.writerow({'Client Name':item['client']['name'], 'Client Type':item['client']['type'], 'Client Version':item['client']['version'], 'Device Model':item['device']['model'], 'Device Type':item['device']['type'], 'Device Vendor':item['device']['vendor'], 'City':item['location']['city'], 'Country':item['location']['country'], 'OS Name':item['os']['name'], 'OS Shortname':item['os']['shortname'], 'OS Version':item['os']['version'], 'Ref Medium':item['referrer']['medium'], 'Ref Search Term':item['referrer']['search_term'], 'Ref Source':item['referrer']['source'], 'Ref URL':item['referrer']['url'], 'Session End':item['session']['ended_at'], 'Session Loaded At':item['session']['loaded_at'], 'Session ID':item['session']['session_id']})


# list live stream sessions
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"sort_by":"asc"} """)
@click.option('--csvfile', default=False, help="""Put true if you want a csv file of the output.""")
@click.argument('videoid')
@click.pass_context
def listlivesessions(ctx, videoid, payload, csvfile):
    """
        Retrieve all or a filtered list of live stream sessions by live stream ID and other attributes.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    rawstats_api = RawStatisticsApi(client)
   
    payload = json.loads(payload)
    if payload:
        response = rawstats_api.list_live_stream_sessions(videoid, **payload)
    else:
        response = rawstats_api.list_live_stream_sessions(videoid)
    print(response)

    if csvfile:
        response = response['data']
        with open('live_sessions_file.csv', 'w', newline='') as csv_file:
            fieldnames = ['Client Name', 'Client Type', 'Client Version', 'Device Model', 'Device Type', 'Device Vendor', 'City', 'Country', 'OS Name', 'OS Shortname', 'OS Version', 'Ref Medium', 'Ref Search Term', 'Ref Source', 'Ref URL', 'Session End', 'Session Loaded At', 'Session ID']
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()
            for item in response:
                writer.writerow({'Client Name':item['client']['name'], 'Client Type':item['client']['type'], 'Client Version':item['client']['version'], 'Device Model':item['device']['model'], 'Device Type':item['device']['type'], 'Device Vendor':item['device']['vendor'], 'City':item['location']['city'], 'Country':item['location']['country'], 'OS Name':item['os']['name'], 'OS Shortname':item['os']['shortname'], 'OS Version':item['os']['version'], 'Ref Medium':item['referrer']['medium'], 'Ref Search Term':item['referrer']['search_term'], 'Ref Source':item['referrer']['source'], 'Ref URL':item['referrer']['url'], 'Session End':item['session']['ended_at'], 'Session Loaded At':item['session']['loaded_at'], 'Session ID':item['session']['session_id']})

# list player sessions 
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"sort_by":"asc"} """)
@click.option('--csvfile', default=False, help="""Put true if you want a csv file of the output.""")
@click.argument('sessionid')
@click.pass_context
def listplayersessions(ctx, sessionid, payload):
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()
    rawstats_api = RawStatisticsApi(client)
   
    payload = json.loads(payload)
    if payload:
        response = rawstats_api.list_session_events(sessionid, **payload)
    else:
        response = rawstats_api.list_session_events(sessionid)
    print(response)

    if csvfile:
        response = response['data']
        with open('player_sessions_file.csv', 'w', newline='') as csv_file:
            fieldnames = ['Type', 'Emitted At', 'At', 'From', 'To']
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()
            for item in response:
                if 'at' in item: 
                    AT = item['at']
                if 'at' not in item:
                    AT = 'not'
                if 'from' in item:
                    FROM = item['from']
                if 'from' not in item:
                    FROM = 'not'
                if 'to' in item:
                    TO = item['to']
                if 'to' not in item:
                    TO = 'not'
                writer.writerow({'Type':item['type'], 'Emitted At':item['emittedAt'], 'At':AT, 'From':FROM, 'To':TO})

# WEBHOOKS 

# list all webhooks 
@main.command()
@click.option('--payload', default={}, help="""Add a JSON dictionary containing all the search features you want to use. The format would be: '{"page_size":1}' """)
@click.pass_context
def listwebhooks(ctx, payload):
    """
        Retrieve a list of all or filtered webhooks. 
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()    

    webhooks_api = WebhooksApi(client)

    payload = json.loads(payload)
    if payload:
        response = webhooks_api.list(**payload)
    else:
        response = webhooks_api.list()
    print(response)

# create a webhook
@main.command()
@click.argument('payload')
@click.pass_context
def createwebhook(ctx, payload):
    """
        Create a webhook. Send a dictionary containing a list of the webhooks you want to subscribe to.
        Send the URL you want the webhook information sent to.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()    

    webhooks_api = WebhooksApi(client)

    payload = json.loads(payload)
    response = webhooks_api.list(**payload)
    print(response)

# show webhook
@main.command()
@click.argument('webhookid')
@click.pass_context
def getwebhook(ctx, webhookid):
    """
        Retrieve details for a webhook using its ID.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()    

    webhooks_api = WebhooksApi(client)    

    response = webhooks_api.get(webhookid)
    print(response)

# delete a webhook
@main.command()
@click.argument('webhookid')
@click.pass_context
def deletewebhook(ctx, webhookid):
    """
        Delete a webhook using its ID.
    """
    api_key = ctx.obj['api_key']
    client = setClient(api_key)
    client.connect()    

    webhooks_api = WebhooksApi(client)

    response = webhooks_api.delete(webhookid)
    print(response)

if __name__ == "__main__":
    main()
