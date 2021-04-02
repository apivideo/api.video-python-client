
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.account_api import AccountApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from apivideo.api.account_api import AccountApi
from apivideo.api.captions_api import CaptionsApi
from apivideo.api.chapters_api import ChaptersApi
from apivideo.api.live_api import LiveApi
from apivideo.api.players_api import PlayersApi
from apivideo.api.raw_statistics_api import RawStatisticsApi
from apivideo.api.videos_api import VideosApi
from apivideo.api.videos_delegated_upload_api import VideosDelegatedUploadApi
from apivideo.api.webhooks_api import WebhooksApi
