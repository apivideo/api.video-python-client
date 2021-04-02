# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from apivideo.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from apivideo.model.access_token import AccessToken
from apivideo.model.account import Account
from apivideo.model.account_quota import AccountQuota
from apivideo.model.authenticate_payload import AuthenticatePayload
from apivideo.model.bad_request import BadRequest
from apivideo.model.bytes_range import BytesRange
from apivideo.model.captions_list_response import CaptionsListResponse
from apivideo.model.captions_update_payload import CaptionsUpdatePayload
from apivideo.model.chapter import Chapter
from apivideo.model.chapters_list_response import ChaptersListResponse
from apivideo.model.link import Link
from apivideo.model.live_stream import LiveStream
from apivideo.model.live_stream_assets import LiveStreamAssets
from apivideo.model.live_stream_create_payload import LiveStreamCreatePayload
from apivideo.model.live_stream_list_response import LiveStreamListResponse
from apivideo.model.live_stream_session import LiveStreamSession
from apivideo.model.live_stream_session_client import LiveStreamSessionClient
from apivideo.model.live_stream_session_device import LiveStreamSessionDevice
from apivideo.model.live_stream_session_location import LiveStreamSessionLocation
from apivideo.model.live_stream_session_referrer import LiveStreamSessionReferrer
from apivideo.model.live_stream_session_session import LiveStreamSessionSession
from apivideo.model.live_stream_update_payload import LiveStreamUpdatePayload
from apivideo.model.metadata import Metadata
from apivideo.model.not_found import NotFound
from apivideo.model.pagination import Pagination
from apivideo.model.pagination_link import PaginationLink
from apivideo.model.player import Player
from apivideo.model.player_all_of import PlayerAllOf
from apivideo.model.player_all_of_assets import PlayerAllOfAssets
from apivideo.model.player_creation_payload import PlayerCreationPayload
from apivideo.model.player_session_event import PlayerSessionEvent
from apivideo.model.player_update_payload import PlayerUpdatePayload
from apivideo.model.playerinput import Playerinput
from apivideo.model.players_list_response import PlayersListResponse
from apivideo.model.quality import Quality
from apivideo.model.raw_statistics_list_live_stream_analytics_response import RawStatisticsListLiveStreamAnalyticsResponse
from apivideo.model.raw_statistics_list_player_session_events_response import RawStatisticsListPlayerSessionEventsResponse
from apivideo.model.raw_statistics_list_sessions_response import RawStatisticsListSessionsResponse
from apivideo.model.refresh_token_payload import RefreshTokenPayload
from apivideo.model.subtitle import Subtitle
from apivideo.model.token_create_payload import TokenCreatePayload
from apivideo.model.token_list_response import TokenListResponse
from apivideo.model.upload_token import UploadToken
from apivideo.model.video import Video
from apivideo.model.video_assets import VideoAssets
from apivideo.model.video_create_payload import VideoCreatePayload
from apivideo.model.video_session import VideoSession
from apivideo.model.video_session_client import VideoSessionClient
from apivideo.model.video_session_device import VideoSessionDevice
from apivideo.model.video_session_location import VideoSessionLocation
from apivideo.model.video_session_os import VideoSessionOs
from apivideo.model.video_session_referrer import VideoSessionReferrer
from apivideo.model.video_session_session import VideoSessionSession
from apivideo.model.video_source import VideoSource
from apivideo.model.video_source_live_stream import VideoSourceLiveStream
from apivideo.model.video_source_live_stream_link import VideoSourceLiveStreamLink
from apivideo.model.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from apivideo.model.video_update_payload import VideoUpdatePayload
from apivideo.model.videos_list_response import VideosListResponse
from apivideo.model.videostatus import Videostatus
from apivideo.model.videostatus_encoding import VideostatusEncoding
from apivideo.model.videostatus_encoding_metadata import VideostatusEncodingMetadata
from apivideo.model.videostatus_ingest import VideostatusIngest
from apivideo.model.webhook import Webhook
from apivideo.model.webhooks_create_payload import WebhooksCreatePayload
from apivideo.model.webhooks_list_response import WebhooksListResponse
