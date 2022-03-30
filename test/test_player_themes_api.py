"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.player_themes_api import PlayerThemesApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.player_theme import PlayerTheme
from apivideo.model.player_theme_creation_payload import PlayerThemeCreationPayload
from apivideo.model.player_theme_update_payload import PlayerThemeUpdatePayload
from apivideo.model.player_themes_list_response import PlayerThemesListResponse

from helper import MainTest


responses = Responses()


class TestPlayerThemesApi(MainTest):
    """PlayerThemesApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = PlayerThemesApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Create a player  # noqa: E501
        """
        for status, json in self.load_json('player_themes', 'create'):
            responses.reset()

            kwargs = {
                'player_theme_creation_payload': PlayerThemeCreationPayload(
        name="name_example",
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        link_active="link_active_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=False,
        hide_title=False,
        force_loop=False,
    ),
            }
            url = '/players'.format(**kwargs)

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

        Retrieve a player  # noqa: E501
        """
        for status, json in self.load_json('player_themes', 'get'):
            responses.reset()

            kwargs = {
                'player_id': "pl45d5vFFGrfdsdsd156dGhh",
            }
            url = '/players/{player_id}'.format(**kwargs)

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

        Update a player  # noqa: E501
        """
        for status, json in self.load_json('player_themes', 'update'):
            responses.reset()

            kwargs = {
                'player_id': "pl45d5vFFGrfdsdsd156dGhh",
                'player_theme_update_payload': PlayerThemeUpdatePayload(
        name="name_example",
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        link_active="link_active_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=True,
        hide_title=True,
        force_loop=True,
    ),
            }
            url = '/players/{player_id}'.format(**kwargs)

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

        Delete a player  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all player themes  # noqa: E501
        """
        for status, json in self.load_json('player_themes', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/players'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

    @responses.activate
    def test_upload_logo(self):
        """Test case for upload_logo

        Upload a logo  # noqa: E501
        """
        pass

    @responses.activate
    def test_delete_logo(self):
        """Test case for delete_logo

        Delete logo  # noqa: E501
        """
        pass

