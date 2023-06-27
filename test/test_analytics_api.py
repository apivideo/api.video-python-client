"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.analytics_api import AnalyticsApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from apivideo.model.analytics_plays_response import AnalyticsPlaysResponse
from apivideo.model.model403_error_schema import Model403ErrorSchema
from apivideo.model.not_found import NotFound

from helper import MainTest


responses = Responses()


class TestAnalyticsApi(MainTest):
    """AnalyticsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = AnalyticsApi(self.client)  # noqa: E501

    @responses.activate
    def test_get_live_streams_plays(self):
        """Test case for get_live_streams_plays

        Get play events for live stream  # noqa: E501
        """
        for file_name, json in self.load_json('analytics', 'get_live_streams_plays'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                '_from': dateutil_parser('2023-06-01').date(),
                'dimension': "browser",
            }
            url = '/analytics/live-streams/plays'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_live_streams_plays(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_live_streams_plays(**kwargs)

    @responses.activate
    def test_get_videos_plays(self):
        """Test case for get_videos_plays

        Get play events for video  # noqa: E501
        """
        for file_name, json in self.load_json('analytics', 'get_videos_plays'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                '_from': dateutil_parser('2023-06-01').date(),
                'dimension': "browser",
            }
            url = '/analytics/videos/plays'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_videos_plays(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_videos_plays(**kwargs)

