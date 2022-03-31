"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.upload_tokens_api import UploadTokensApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.token_creation_payload import TokenCreationPayload
from apivideo.model.token_list_response import TokenListResponse
from apivideo.model.upload_token import UploadToken

from helper import MainTest


responses = Responses()


class TestUploadTokensApi(MainTest):
    """UploadTokensApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = UploadTokensApi(self.client)  # noqa: E501

    @responses.activate
    def test_create_token(self):
        """Test case for create_token

        Generate an upload token  # noqa: E501
        """
        for status, json in self.load_json('upload_tokens', 'create_token'):
            responses.reset()

            kwargs = {
                'token_creation_payload': TokenCreationPayload(
        ttl=0,
    ),
            }
            url = '/upload-tokens'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create_token(**kwargs)

    @responses.activate
    def test_get_token(self):
        """Test case for get_token

        Retrieve upload token  # noqa: E501
        """
        for status, json in self.load_json('upload_tokens', 'get_token'):
            responses.reset()

            kwargs = {
                'upload_token': "to1tcmSFHeYY5KzyhOqVKMKb",
            }
            url = '/upload-tokens/{upload_token}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_token(**kwargs)

    @responses.activate
    def test_delete_token(self):
        """Test case for delete_token

        Delete an upload token  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all active upload tokens.  # noqa: E501
        """
        for status, json in self.load_json('upload_tokens', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/upload-tokens'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

