"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

import time
import json

from apivideo.api_client import ApiClient
from apivideo.exceptions import ApiException, ApiAuthException


HOST_ENVIRONMENT = {
    "production": "https://ws.api.video",
    "sandbox": "https://sandbox.api.video"
}


class AuthenticatedApiClient(ApiClient):
    """Authenticated API client for api.video

    :param api_key: The api key to authenticate
    """

    def __init__(self, api_key, production=True, **kwargs):
        self.api_key = api_key

        # Auth
        self._access_token = None
        self._refresh_token = None
        self.token_type = "Bearer"
        self.next_refresh = None
        self._terminated = False

        super().__init__(**kwargs)
        self.configuration.host = HOST_ENVIRONMENT.get("production" if production else "sandbox")

    def __enter__(self):
        self.connect()
        self.pool.apply_async(self._refresh)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._terminated = True
        self.close()

    def update_params_for_auth(self, headers, querys, auth_settings,
                               resource_path, method, body):
        if not self._access_token:
            raise ApiAuthException("Not connected")
        headers['Authorization'] = '{} {}'.format(self.token_type, self._access_token)

    def _update_connection(self, resource_path, body):
        url = self.configuration.host + resource_path
        headers = { 'AV-Origin-Client': self.default_headers['AV-Origin-Client'] }
        if self.default_headers.__contains__('AV-Origin-App') and len(self.default_headers.get('AV-Origin-App')):
            headers['AV-Origin-App'] = self.default_headers['AV-Origin-App']
        resp = self.rest_client.POST(url, body=body, headers=headers)
        data = json.loads(resp.data)
        try:
            self._access_token = data['access_token']
            self._refresh_token = data['refresh_token']
            self.token_type = data['token_type']
            self.next_refresh = time.time() + data['expires_in'] - 10
        except KeyError:
            self._access_token = None  # In case of auth error, invalidate the access token
            raise ApiAuthException("Wrong auth response")

    def connect(self):
        self._update_connection("/auth/api-key", {"apiKey": self.api_key})

    def refresh_token(self):
        if not self._refresh_token:
            raise ApiAuthException("Cannot refresh token before being connected")
        self._update_connection("/auth/refresh", {"refreshToken": self._refresh_token})

    def _refresh(self):
        while time.time() < self.next_refresh:
            if self._terminated:
                break
            time.sleep(1)
        self.refresh_token()
        self.pool.apply_async(self._refresh)
