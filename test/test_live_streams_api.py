"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.live_streams_api import LiveStreamsApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.live_stream import LiveStream
from apivideo.model.live_stream_creation_payload import LiveStreamCreationPayload
from apivideo.model.live_stream_list_response import LiveStreamListResponse
from apivideo.model.live_stream_update_payload import LiveStreamUpdatePayload
from apivideo.model.not_found import NotFound

from helper import MainTest


responses = Responses()


class TestLiveStreamsApi(MainTest):
    """LiveStreamsApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = LiveStreamsApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Create live stream  # noqa: E501
        """
        for status, json in self.load_json('live_streams', 'create'):
            responses.reset()

            kwargs = {
                'live_stream_creation_payload': LiveStreamCreationPayload(
        name="My Live Stream Video",
        record=True,
        public=True,
        player_id="pl4f4ferf5erfr5zed4fsdd",
    ),
            }
            url = '/live-streams'.format(**kwargs)

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

        Retrieve live stream  # noqa: E501
        """
        for status, json in self.load_json('live_streams', 'get'):
            responses.reset()

            kwargs = {
                'live_stream_id': "li400mYKSgQ6xs7taUeSaEKr",
            }
            url = '/live-streams/{live_stream_id}'.format(**kwargs)

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

        Update a live stream  # noqa: E501
        """
        for status, json in self.load_json('live_streams', 'update'):
            responses.reset()

            kwargs = {
                'live_stream_id': "li400mYKSgQ6xs7taUeSaEKr",
                'live_stream_update_payload': LiveStreamUpdatePayload(
        name="My Live Stream Video",
        public=True,
        record=True,
        player_id="pl45KFKdlddgk654dspkze",
    ),
            }
            url = '/live-streams/{live_stream_id}'.format(**kwargs)

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

        Delete a live stream  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all live streams  # noqa: E501
        """
        for status, json in self.load_json('live_streams', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/live-streams'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

    @responses.activate
    def test_upload_thumbnail(self):
        """Test case for upload_thumbnail

        Upload a thumbnail  # noqa: E501
        """
        pass

    @responses.activate
    def test_delete_thumbnail(self):
        """Test case for delete_thumbnail

        Delete a thumbnail  # noqa: E501
        """
        pass

