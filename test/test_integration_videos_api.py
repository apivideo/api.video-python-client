"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""
from pprint import pprint
from unittest import TestCase
import tempfile
import unittest

from apivideo.model.token_creation_payload import TokenCreationPayload

from apivideo.api.upload_tokens_api import UploadTokensApi

import apivideo
import string
import os
from apivideo.api.videos_api import VideosApi  # noqa: E501
from apivideo.model.metadata import Metadata
from apivideo.model.video_creation_payload import VideoCreationPayload
import random


class TestVideosApi(TestCase):
    """VideosApi integration tests"""

    def setUp(self):
        super().setUp()
        self.client = apivideo.AuthenticatedApiClient(os.getenv("API_KEY"))
        self.client.set_application_name("client-integration-tests", "0")
        self.client.connect()
        self.api = VideosApi(self.client)  # noqa: E501
        self.token_api = UploadTokensApi(self.client)  # noqa: E501

    def tearDown(self) -> None:
        self.client.close()

    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_metadata(self):
        letters = string.ascii_lowercase
        metadataValue = ''.join(random.choice(letters) for i in range(64))

        video_with_metadata = self.api.create(video_creation_payload=VideoCreationPayload(
            title='with metadata',
            metadata=[
                Metadata(key="k", value=metadataValue)
            ]))
        video_without_metadata = self.api.create(video_creation_payload=VideoCreationPayload(
            title='without metadata'))

        videos_list = self.api.list(**{'metadata': {'k': metadataValue}})

        self.assertEqual(len(videos_list.data), 1)

        self.api.delete(video_with_metadata.video_id)
        self.api.delete(video_without_metadata.video_id)


    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_tags(self):

        video_with_tags = self.api.create(video_creation_payload=VideoCreationPayload(
            tags=["aa", "bb"],
            title='with tags'
            ))

        videos_list_two_tags = self.api.list(**{'tags': ["aa", "bb"]})
        videos_list_one_tag = self.api.list(**{'tags': ["aa"]})
        videos_list_wrong_tag = self.api.list(**{'tags': ["cc"]})

        self.api.delete(video_with_tags.video_id)

        self.assertGreaterEqual(len(videos_list_two_tags.data), 1)
        self.assertGreaterEqual(len(videos_list_one_tag.data), 1)
        self.assertEqual(len(videos_list_wrong_tag.data), 0)


    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload(self):

        def listener(uploaded, total):
            print('Progress: {}/{}'.format(uploaded, total))

        video = self.api.create(video_creation_payload=VideoCreationPayload(
            title='upload',
            public=True,
            tags=["bunny"]))

        file = open("10m.mp4", "rb")
        self.api.upload(video.video_id, file, _request_timeout=20, _progress_listener=listener)
        file.close()
        self.api.delete(video.video_id)


    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload_stream(self):
        video = self.api.create(video_creation_payload=VideoCreationPayload(title='upload stream'))

        part1 = open('10m.mp4.part.a', 'rb')
        part2 = open('10m.mp4.part.b', 'rb')
        part3 = open('10m.mp4.part.c', 'rb')

        session = self.api.create_upload_progressive_session(video.video_id)
        session.uploadPart(part1)
        session.uploadPart(part2)
        session.uploadLastPart(part3)

        part1.close()
        part2.close()
        part3.close()

        self.api.delete(video.video_id)


    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload_token_stream(self):
        token = self.token_api.create_token(TokenCreationPayload()).token

        part1 = open('10m.mp4.part.a', 'rb')
        part2 = open('10m.mp4.part.b', 'rb')
        part3 = open('10m.mp4.part.c', 'rb')

        session = self.api.create_upload_with_upload_token_progressive_session(token)
        session.uploadPart(part1)
        session.uploadPart(part2)
        res = session.uploadLastPart(part3)

        part1.close()
        part2.close()
        part3.close()

        self.api.delete(res.video_id)
        self.token_api.delete_token(token)

    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload_temporary_file(self):
        video = self.api.create(video_creation_payload=VideoCreationPayload(
            title='upload',
            public=True,
            tags=["bunny"]))

        file = open("558k.mp4", "rb")
        with tempfile.SpooledTemporaryFile(mode="wb") as temp:
            temp.write(file.read())
            self.api.upload(video.video_id, temp, _request_timeout=20)
        file.close()
        self.api.delete(video.video_id)

    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload_chunks(self):
        video = self.api.create(video_creation_payload=VideoCreationPayload(
            title='upload',
            public=True,
            tags=["bunny"]))

        file = open("10m.mp4", "rb")
        self.api.upload(video.video_id, file, _request_timeout=20)
        file.close()
        self.api.delete(video.video_id)