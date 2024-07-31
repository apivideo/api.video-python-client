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
from apivideo.model.restreams_request_object import RestreamsRequestObject

from apivideo.model.analytics_aggregated_metrics_response import AnalyticsAggregatedMetricsResponse
from apivideo.model.analytics_metrics_breakdown_response import AnalyticsMetricsBreakdownResponse
from apivideo.model.analytics_metrics_over_time_response import AnalyticsMetricsOverTimeResponse
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from apivideo.model.filter_by2 import FilterBy2
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.unrecognized_request_url import UnrecognizedRequestUrl

from helper import MainTest


responses = Responses()


class TestAnalyticsApi(MainTest):
    """AnalyticsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = AnalyticsApi(self.client)  # noqa: E501

    @responses.activate
    def test_get_aggregated_metrics(self):
        """Test case for get_aggregated_metrics

        Retrieve aggregated metrics  # noqa: E501
        """
        for file_name, json in self.load_json('analytics', 'get_aggregated_metrics'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'metric': "play",
                'aggregation': "count",
            }
            url = '/data/metrics/{metric}/{aggregation}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_aggregated_metrics(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_aggregated_metrics(**kwargs)

    @responses.activate
    def test_get_metrics_breakdown(self):
        """Test case for get_metrics_breakdown

        Retrieve metrics in a breakdown of dimensions  # noqa: E501
        """
        for file_name, json in self.load_json('analytics', 'get_metrics_breakdown'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'metric': "play",
                'breakdown': "media-id",
            }
            url = '/data/buckets/{metric}/{breakdown}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_metrics_breakdown(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_metrics_breakdown(**kwargs)

    @responses.activate
    def test_get_metrics_over_time(self):
        """Test case for get_metrics_over_time

        Retrieve metrics over time  # noqa: E501
        """
        for file_name, json in self.load_json('analytics', 'get_metrics_over_time'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'metric': "play",
            }
            url = '/data/timeseries/{metric}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_metrics_over_time(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_metrics_over_time(**kwargs)

