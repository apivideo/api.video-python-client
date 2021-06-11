"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

import time
import unittest

import apivideo
from apivideo.exceptions import ApiAuthException

from urllib3_mock import Responses


responses = Responses()

AUTH_RESPONSE = """
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJh", 
    "refresh_token": "def50200a28d88fb9aa",
    "token_type": "Bearer",
    "expires_in": 11
}
"""


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.client = apivideo.AuthenticatedApiClient("__KEY__")

    @responses.activate
    def test_connect_fail(self):
        responses.add('POST', '/auth/api-key', body="{}", status=int(200), content_type='application/json')
        with self.assertRaises(ApiAuthException):
            self.client.connect()
        with self.assertRaises(ApiAuthException):
            self.client.call_api('/test', 'GET')

    @responses.activate
    def test_connect_success(self):
        responses.add('POST', '/auth/api-key', body=AUTH_RESPONSE, status=200, content_type='application/json')
        responses.add('GET', '/test', body="{}", status=200, content_type='application/json')
        self.client.connect()
        self.client.call_api('/test', 'GET')

    @responses.activate
    def test_refresh_fail(self):
        responses.add('POST', '/auth/api-key', body=AUTH_RESPONSE, status=200, content_type='application/json')
        responses.add('POST', '/auth/refresh', body="{}", status=200, content_type='application/json')
        responses.add('GET', '/test', body="{}", status=200, content_type='application/json')
        with self.assertRaises(ApiAuthException):
            self.client.refresh_token()
        self.client.connect()
        self.client.call_api('/test', 'GET')
        with self.assertRaises(ApiAuthException):
            self.client.refresh_token()
        with self.assertRaises(ApiAuthException):
            self.client.call_api('/test', 'GET')

    @responses.activate
    def test_refresh_success(self):
        responses.add('POST', '/auth/api-key', body=AUTH_RESPONSE, status=200, content_type='application/json')
        responses.add('POST', '/auth/refresh', body=AUTH_RESPONSE, status=200, content_type='application/json')
        responses.add('GET', '/test', body="{}", status=200, content_type='application/json')
        self.client.connect()
        self.client.call_api('/test', 'GET')
        self.client.refresh_token()
        self.client.call_api('/test', 'GET')

    @responses.activate
    def test_autorefresh_fail(self):
        responses.add('POST', '/auth/api-key', body=AUTH_RESPONSE, status=200, content_type='application/json')
        responses.add('POST', '/auth/refresh', body="{}", status=200, content_type='application/json')

        with apivideo.AuthenticatedApiClient("__KEY__") as client:
            time.sleep(2)
            with self.assertRaises(ApiAuthException):
                client.call_api('/test', 'GET')

        self.assertEqual(2, len(responses.calls))
