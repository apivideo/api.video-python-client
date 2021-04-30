"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from os import path, listdir
import unittest

import apivideo


class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = apivideo.AuthenticatedApiClient("__KEY__")
        self.client.update_params_for_auth = lambda *x: None  # ignore auth

    def load_json(self, api, operation):
        api_path = path.join(path.dirname(path.realpath(__file__)), 'payloads', api, operation, 'responses')
        for status_file in listdir(api_path):
            file_path = path.join(api_path, status_file)
            if path.isfile(file_path):
                status = path.splitext(status_file)[0]
                with(open(file_path, 'r')) as file:
                    yield status, file.read()
