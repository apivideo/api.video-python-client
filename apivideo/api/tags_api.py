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
from apivideo.model.list_tags_response import ListTagsResponse
from apivideo.model.too_many_requests import TooManyRequests


class TagsApi(_EndPoint):

    def list(
            self,
            **kwargs
        ):
            """List all video tags  # noqa: E501

            This endpoint enables you to search for video tags in a project and see how many videos are tagged with them. If you do not define any query parameters, the endpoint lists all video tags and the numbers of times they are used in a project.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                value (str): Use this parameter to search for specific video tags. The API filters results even on partial values, and ignores accents, uppercase, and lowercase. . [optional]
                sort_by (str): Use this parameter to choose which field the API will use to sort the response data. The default is `value`.  These are the available fields to sort by:  - `value`: Sorts the results based on tag values in alphabetic order. - `videoCount`: Sorts the results based on the number of times a video tag is used. . [optional]
                sort_order (str): Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A.. [optional]
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
                ListTagsResponse
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

            params_map = {
                'all': [
                    'value',
                    'sort_by',
                    'sort_order',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'sort_by',
                    'sort_order',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('sort_by',): {

                    "VALUE": "value",
                    "VIDEOCOUNT": "videoCount"
                },
                ('sort_order',): {

                    "ASC": "asc",
                    "DESC": "desc"
                },
            }
            openapi_types = {
                'value':
                    (str,),
                'sort_by':
                    (str,),
                'sort_order':
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
                'value': 'value',
                'sort_by': 'sortBy',
                'sort_order': 'sortOrder',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                'value': 'query',
                'sort_by': 'query',
                'sort_order': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `list`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `list`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`list`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/tags",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(ListTagsResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

