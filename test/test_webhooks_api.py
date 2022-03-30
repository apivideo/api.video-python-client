"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.webhooks_api import WebhooksApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.webhook import Webhook
from apivideo.model.webhooks_creation_payload import WebhooksCreationPayload
from apivideo.model.webhooks_list_response import WebhooksListResponse

from helper import MainTest


responses = Responses()


class TestWebhooksApi(MainTest):
    """WebhooksApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = WebhooksApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Create Webhook  # noqa: E501
        """
        for status, json in self.load_json('webhooks', 'create'):
            responses.reset()

            kwargs = {
                'webhooks_creation_payload': WebhooksCreationPayload(
        events=["video.encoding.quality.completed"],
        url="https://example.com/webhooks",
    ),
            }
            url = '/webhooks'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create(**kwargs)

    @responses.activate
    def test_get(self):
        """Test case for get

        Retrieve Webhook details  # noqa: E501
        """
        for status, json in self.load_json('webhooks', 'get'):
            responses.reset()

            kwargs = {
                'webhook_id': "webhookId_example",
            }
            url = '/webhooks/{webhook_id}'.format(**kwargs)

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

        Delete a Webhook  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all webhooks  # noqa: E501
        """
        for status, json in self.load_json('webhooks', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/webhooks'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

