"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

import os  # noqa: F401
import re  # noqa: F401
import sys  # noqa: F401
from types import MethodType
from types import FunctionType

from apivideo.api_client import ApiClient
from apivideo.endpoint import EndPoint as _EndPoint, ChunkIO
from apivideo.model.video_id import VideoId
from apivideo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from apivideo.exceptions import ApiTypeError, ApiValueError
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from apivideo.model.analytics_plays_response import AnalyticsPlaysResponse
from apivideo.model.model403_error_schema import Model403ErrorSchema
from apivideo.model.not_found import NotFound


class AnalyticsApi(_EndPoint):

    def get_live_streams_plays(
            self,
            _from,
            dimension,
            **kwargs
        ):
            """Get play events for live stream  # noqa: E501

            Retrieve filtered analytics about the number of plays for your live streams in a project.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_live_streams_plays(_from, dimension, async_req=True)
            >>> result = thread.get()

            Args:
                _from (date): Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 
                dimension (str): Use this query parameter to define the dimension that you want analytics for. - `liveStreamId`: Returns analytics based on the public live stream identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. Possible response values are: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. Response values include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers during the play event. Response values include `chrome`, `firefox`, `edge`, `opera`.

            Keyword Args:
                to (date): Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. . [optional]
                filter (str): Use this query parameter to filter your results to a specific live stream in a project that you want analytics for. You must use the `liveStreamId:` prefix when specifying a live stream ID.. [optional]
                current_page (int): Choose the number of search results to return per page. Minimum value: 1. [optional] if omitted the server will use the default value of 1
                page_size (int): Results per page. Allowed values 1-100, default is 25.. [optional] if omitted the server will use the default value of 25
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                async_req (bool): execute request asynchronously

            Returns:
                AnalyticsPlaysResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_from'] = \
                _from
            kwargs['dimension'] = \
                dimension

            params_map = {
                'all': [
                    '_from',
                    'dimension',
                    'to',
                    'filter',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    '_from',
                    'dimension',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'dimension',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('dimension',): {

                    "LIVESTREAMID": "liveStreamId",
                    "EMITTEDAT": "emittedAt",
                    "COUNTRY": "country",
                    "DEVICETYPE": "deviceType",
                    "OPERATINGSYSTEM": "operatingSystem",
                    "BROWSER": "browser"
                },
            }
            openapi_types = {
                '_from':
                    (date,),
                'dimension':
                    (str,),
                'to':
                    (date,),
                'filter':
                    (str,),
                'current_page':
                    (int,),
                'page_size':
                    (int,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                '_from': 'from',
                'dimension': 'dimension',
                'to': 'to',
                'filter': 'filter',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                '_from': 'query',
                'dimension': 'query',
                'to': 'query',
                'filter': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get_live_streams_plays`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get_live_streams_plays`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get_live_streams_plays`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/analytics/live-streams/plays",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(AnalyticsPlaysResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get_videos_plays(
            self,
            _from,
            dimension,
            **kwargs
        ):
            """Get play events for video  # noqa: E501

            Retrieve filtered analytics about the number of plays for your videos in a project.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_videos_plays(_from, dimension, async_req=True)
            >>> result = thread.get()

            Args:
                _from (date): Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 
                dimension (str): Use this query parameter to define the dimension that you want analytics for. - `videoId`: Returns analytics based on the public video identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. Possible response values are: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. Response values include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers during the play event. Response values include `chrome`, `firefox`, `edge`, `opera`.

            Keyword Args:
                to (date): Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. . [optional]
                filter (str): Use this query parameter to filter your results to a specific video in a project that you want analytics for. You must use the `videoId:` prefix when specifying a video ID.. [optional]
                current_page (int): Choose the number of search results to return per page. Minimum value: 1. [optional] if omitted the server will use the default value of 1
                page_size (int): Results per page. Allowed values 1-100, default is 25.. [optional] if omitted the server will use the default value of 25
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                async_req (bool): execute request asynchronously

            Returns:
                AnalyticsPlaysResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_from'] = \
                _from
            kwargs['dimension'] = \
                dimension

            params_map = {
                'all': [
                    '_from',
                    'dimension',
                    'to',
                    'filter',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    '_from',
                    'dimension',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'dimension',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('dimension',): {

                    "VIDEOID": "videoId",
                    "EMITTEDAT": "emittedAt",
                    "COUNTRY": "country",
                    "DEVICETYPE": "deviceType",
                    "OPERATINGSYSTEM": "operatingSystem",
                    "BROWSER": "browser"
                },
            }
            openapi_types = {
                '_from':
                    (date,),
                'dimension':
                    (str,),
                'to':
                    (date,),
                'filter':
                    (str,),
                'current_page':
                    (int,),
                'page_size':
                    (int,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                '_from': 'from',
                'dimension': 'dimension',
                'to': 'to',
                'filter': 'filter',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                '_from': 'query',
                'dimension': 'query',
                'to': 'query',
                'filter': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get_videos_plays`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get_videos_plays`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get_videos_plays`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/analytics/videos/plays",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(AnalyticsPlaysResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

