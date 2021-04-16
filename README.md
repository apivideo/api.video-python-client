![](https://raw.githubusercontent.com/apivideo/API_OAS_file/master/apivideo_banner.png)

# api.video Python api client

api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

## Requirements.

Python >= 3.6

## Installation

```sh
pip install api.video
```

## Examples

# Automatic authentification

list all videos:

```python
import apivideo
from apivideo.apis import VideosApi

api_key = "__API_KEY__"

with apivideo.AuthenticatedApiClient(api_key) as client:
    # if you rather like to use the sandbox environment:
    # with apivideo.AuthenticatedApiClient(api_key, production=False) as client:

    videos_api = VideosApi(client)
    videos = videos_api.list()
```

In this context the client will keep its authentification updated.

# Manual authentification

If you rather update the access token manually:

```python
import apivideo
from apivideo.apis import VideosApi
from apivideo.exceptions import ApiAuthException

api_key = "__API_KEY__"

client = apivideo.AuthenticatedApiClient(api_key):
# if you rather like to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)
client.connect()
videos_api = VideosApi(client)
videos = videos_api.list()

try:
    client.refresh_token()
except ApiAuthException:
    print("cannot refresh token !")

...
```


## Documentation

[All the documentation is in the `docs` directory.](docs/)