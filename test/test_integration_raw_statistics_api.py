"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""
import time
from unittest import TestCase
import unittest
import apivideo
import os
from apivideo.api.raw_statistics_api import RawStatisticsApi  # noqa: E501
from apivideo.api.videos_api import VideosApi
from apivideo.model.metadata import Metadata
from apivideo.model.video_creation_payload import VideoCreationPayload
import requests
from datetime import datetime


class TestVideosApi(TestCase):
    """VideosApi integration tests"""

    def setUp(self):
        super().setUp()
        self.client = apivideo.AuthenticatedApiClient(os.getenv("API_KEY"))
        self.client.connect()
        self.rawStatisticsApi = RawStatisticsApi(self.client)  # noqa: E501
        self.videoApi = VideosApi(self.client)  # noqa: E501

    def tearDown(self) -> None:
        self.client.close()

    @unittest.skip
    def test_list_video_sessions_metadata(self):
        video = self.videoApi.create(video_creation_payload=VideoCreationPayload(
            title='session',
            metadata=[
                Metadata(key="user", value='__user__')
            ]))

        file = open("558k.mp4", "rb")
        self.videoApi.upload(video.video_id, file, _request_timeout=20)
        file.close()

        now = datetime.now().strftime("%Y-%M-%dT%H:%M:%S.000Z")
        payload = {"emitted_at": now,
                   "session": {"loaded_at": now, "referrer": "",
                               "metadata": [{"user": "python_test"}], "video_id": video.video_id},
                   "events": [{"type": "ready", "emitted_at": now, "at": 0}]}
        requests.post("https://collector.api.video/vod?t=1623232157262", json=payload)

        time.sleep(5)

        stats = self.rawStatisticsApi.list_video_sessions(video.video_id, **{'metadata': {'user': 'python_test'}})

        self.assertEqual(len(stats.data), 1)
        self.assertEqual(stats.data[0].session.metadata[0].key, 'user')
        self.assertEqual(stats.data[0].session.metadata[0].value, 'python_test')

        self.videoApi.delete(video.video_id)
