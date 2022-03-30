"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.captions_api import CaptionsApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.caption import Caption
from apivideo.model.captions_list_response import CaptionsListResponse
from apivideo.model.captions_update_payload import CaptionsUpdatePayload
from apivideo.model.not_found import NotFound

from helper import MainTest


responses = Responses()


class TestCaptionsApi(MainTest):
    """CaptionsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = CaptionsApi(self.client)  # noqa: E501

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload a caption  # noqa: E501
        """
        for status, json in self.load_json('captions', 'upload'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Prklg",
                'language': "en",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/captions/{language}'.format(**kwargs)

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

        Retrieve a caption  # noqa: E501
        """
        for status, json in self.load_json('captions', 'get'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Prklg",
                'language': "en",
            }
            url = '/videos/{video_id}/captions/{language}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get(**kwargs)

    @responses.activate
    def test_update(self):
        """Test case for update

        Update a caption  # noqa: E501
        """
        for status, json in self.load_json('captions', 'update'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Prklg",
                'language': "en",
                'captions_update_payload': CaptionsUpdatePayload(
        default=True,
    ),
            }
            url = '/videos/{video_id}/captions/{language}'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.update(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.update(**kwargs)

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete a caption  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List video captions  # noqa: E501
        """
        for status, json in self.load_json('captions', 'list'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Prklg",
            }
            url = '/videos/{video_id}/captions'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

