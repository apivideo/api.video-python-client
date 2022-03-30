"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.chapters_api import ChaptersApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.chapter import Chapter
from apivideo.model.chapters_list_response import ChaptersListResponse
from apivideo.model.not_found import NotFound

from helper import MainTest


responses = Responses()


class TestChaptersApi(MainTest):
    """ChaptersApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = ChaptersApi(self.client)  # noqa: E501

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload a chapter  # noqa: E501
        """
        for status, json in self.load_json('chapters', 'upload'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'language': "en",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/chapters/{language}'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload(**kwargs)

    @responses.activate
    def test_get(self):
        """Test case for get

        Retrieve a chapter  # noqa: E501
        """
        for status, json in self.load_json('chapters', 'get'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'language': "en",
            }
            url = '/videos/{video_id}/chapters/{language}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get(**kwargs)

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete a chapter  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List video chapters  # noqa: E501
        """
        for status, json in self.load_json('chapters', 'list'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
            }
            url = '/videos/{video_id}/chapters'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

