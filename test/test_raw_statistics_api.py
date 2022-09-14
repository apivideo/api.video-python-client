"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.raw_statistics_api import RawStatisticsApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.not_found import NotFound
from apivideo.model.raw_statistics_list_live_stream_analytics_response import RawStatisticsListLiveStreamAnalyticsResponse
from apivideo.model.raw_statistics_list_player_session_events_response import RawStatisticsListPlayerSessionEventsResponse
from apivideo.model.raw_statistics_list_sessions_response import RawStatisticsListSessionsResponse

from helper import MainTest


responses = Responses()


class TestRawStatisticsApi(MainTest):
    """RawStatisticsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = RawStatisticsApi(self.client)  # noqa: E501

    @responses.activate
    def test_list_live_stream_sessions(self):
        """Test case for list_live_stream_sessions

        List live stream player sessions  # noqa: E501
        """
        for status, json in self.load_json('raw_statistics', 'list_live_stream_sessions'):
            responses.reset()

            kwargs = {
                'live_stream_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'period': "2019-01-01T00:00:00.000Z",
            }
            url = '/analytics/live-streams/{live_stream_id}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list_live_stream_sessions(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list_live_stream_sessions(**kwargs)

    @responses.activate
    def test_list_session_events(self):
        """Test case for list_session_events

        List player session events  # noqa: E501
        """
        for status, json in self.load_json('raw_statistics', 'list_session_events'):
            responses.reset()

            kwargs = {
                'session_id': "psEmFwGQUAXR2lFHj5nDOpy",
            }
            url = '/analytics/sessions/{session_id}/events'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list_session_events(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list_session_events(**kwargs)

    @responses.activate
    def test_list_video_sessions(self):
        """Test case for list_video_sessions

        List video player sessions  # noqa: E501
        """
        for status, json in self.load_json('raw_statistics', 'list_video_sessions'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Prklg",
                'period': "period_example",
            }
            url = '/analytics/videos/{video_id}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list_video_sessions(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list_video_sessions(**kwargs)

