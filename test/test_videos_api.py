"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.videos_api import VideosApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from apivideo.model.video_creation_payload import VideoCreationPayload
from apivideo.model.video_status import VideoStatus
from apivideo.model.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from apivideo.model.video_update_payload import VideoUpdatePayload
from apivideo.model.videos_list_response import VideosListResponse

from helper import MainTest


responses = Responses()


class TestVideosApi(MainTest):
    """VideosApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = VideosApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Create a video  # noqa: E501
        """
        for status, json in self.load_json('videos', 'create'):
            responses.reset()

            kwargs = {
                'video_creation_payload': VideoCreationPayload(
        title="Maths video",
        description="A video about string theory.",
        source="https://www.myvideo.url.com/video.mp4 OR vi4k0jvEUuaTdRAEjQ4JfOyl",
        public=True,
        panoramic=False,
        mp4_support=True,
        player_id="pl45KFKdlddgk654dspkze",
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
        clip=VideoClip(
            start_timecode="8072",
            end_timecode="8072",
        ),
        watermark=VideoWatermark(
            id="watermark_1BWr2L5MTQwxGkuxKjzh6i",
            top="10px",
            left="10px",
            bottom="10px",
            right="10px",
            width="initial",
            height="initial",
            opacity="70%",
        ),
    ),
            }
            url = '/videos'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create(**kwargs)

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload a video  # noqa: E501
        """
        for status, json in self.load_json('videos', 'upload'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/source'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload(**kwargs)

    @responses.activate
    def test_upload_with_upload_token(self):
        """Test case for upload_with_upload_token

        Upload with an upload token  # noqa: E501
        """
        for status, json in self.load_json('videos', 'upload_with_upload_token'):
            responses.reset()

            kwargs = {
                'token': "to1tcmSFHeYY5KzyhOqVKMKb",
                'file': open('test_file', 'rb'),
            }
            url = '/upload'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload_with_upload_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload_with_upload_token(**kwargs)

    @responses.activate
    def test_get(self):
        """Test case for get

        Retrieve a video  # noqa: E501
        """
        for status, json in self.load_json('videos', 'get'):
            responses.reset()

            kwargs = {
                'video_id': "videoId_example",
            }
            url = '/videos/{video_id}'.format(**kwargs)

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

        Update a video  # noqa: E501
        """
        for status, json in self.load_json('videos', 'update'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'video_update_payload': VideoUpdatePayload(
        player_id="pl4k0jvEUuaTdRAEjQ4Jfrgz",
        title="title_example",
        description="A film about good books.",
        public=True,
        panoramic=False,
        mp4_support=True,
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
    ),
            }
            url = '/videos/{video_id}'.format(**kwargs)

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

        Delete a video  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all videos  # noqa: E501
        """
        for status, json in self.load_json('videos', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/videos'.format(**kwargs)

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
        for status, json in self.load_json('videos', 'upload_thumbnail'):
            responses.reset()

            kwargs = {
                'video_id': "videoId_example",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/thumbnail'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload_thumbnail(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload_thumbnail(**kwargs)

    @responses.activate
    def test_pick_thumbnail(self):
        """Test case for pick_thumbnail

        Pick a thumbnail  # noqa: E501
        """
        for status, json in self.load_json('videos', 'pick_thumbnail'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'video_thumbnail_pick_payload': VideoThumbnailPickPayload(
        timecode="04:80:72",
    ),
            }
            url = '/videos/{video_id}/thumbnail'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.pick_thumbnail(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.pick_thumbnail(**kwargs)

    @responses.activate
    def test_get_status(self):
        """Test case for get_status

        Retrieve video status  # noqa: E501
        """
        for status, json in self.load_json('videos', 'get_status'):
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
            }
            url = '/videos/{video_id}/status'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_status(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_status(**kwargs)

