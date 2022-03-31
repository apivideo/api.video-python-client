"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.watermarks_api import WatermarksApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.watermark import Watermark
from apivideo.model.watermarks_list_response import WatermarksListResponse

from helper import MainTest


responses = Responses()


class TestWatermarksApi(MainTest):
    """WatermarksApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = WatermarksApi(self.client)  # noqa: E501

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload a watermark  # noqa: E501
        """
        for status, json in self.load_json('watermarks', 'upload'):
            responses.reset()

            kwargs = {
                'file': open('test_file', 'rb'),
            }
            url = '/watermarks'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload(**kwargs)

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete a watermark  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all watermarks  # noqa: E501
        """
        for status, json in self.load_json('watermarks', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/watermarks'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

