
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.captions_api import CaptionsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from apivideo.api.captions_api import CaptionsApi
from apivideo.api.chapters_api import ChaptersApi
from apivideo.api.live_streams_api import LiveStreamsApi
from apivideo.api.player_themes_api import PlayerThemesApi
from apivideo.api.raw_statistics_api import RawStatisticsApi
from apivideo.api.upload_tokens_api import UploadTokensApi
from apivideo.api.videos_api import VideosApi
from apivideo.api.watermarks_api import WatermarksApi
from apivideo.api.webhooks_api import WebhooksApi
