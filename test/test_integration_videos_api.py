"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""
from pprint import pprint
from unittest import TestCase
import tempfile
import unittest
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
        self.client.connect()
        self.api = VideosApi(self.client)  # noqa: E501

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
    def test_upload(self):
        video = self.api.create(video_creation_payload=VideoCreationPayload(
            title='upload',
            public=True,
            tags=["bunny"]))

        file = open("sample.mp4", "rb")
        self.api.upload(video.video_id, file, _request_timeout=20)
        file.close()
        self.api.delete(video.video_id)

    @unittest.skipIf(os.getenv("API_KEY") is None, "No API key")
    def test_upload_temporary_file(self):
        video = self.api.create(video_creation_payload=VideoCreationPayload(
            title='upload',
            public=True,
            tags=["bunny"]))

        file = open("sample.mp4", "rb")
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

        file = open("sample-mp4-file.mp4", "rb")
        self.api.upload(video.video_id, file, _request_timeout=20)
        file.close()
        self.api.delete(video.video_id)