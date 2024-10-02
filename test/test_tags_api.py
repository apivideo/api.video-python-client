"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.tags_api import TagsApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.restreams_request_object import RestreamsRequestObject

from apivideo.model.list_tags_response import ListTagsResponse
from apivideo.model.too_many_requests import TooManyRequests

from helper import MainTest


responses = Responses()


class TestTagsApi(MainTest):
    """TagsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = TagsApi(self.client)  # noqa: E501

    @responses.activate
    def test_list(self):
        """Test case for list

        List all video tags  # noqa: E501
        """
        for file_name, json in self.load_json('tags', 'list'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
            }
            url = '/tags'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

