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
from apivideo.model.bad_request import BadRequest
from apivideo.model.live_stream import LiveStream
from apivideo.model.live_stream_creation_payload import LiveStreamCreationPayload
from apivideo.model.live_stream_list_response import LiveStreamListResponse
from apivideo.model.live_stream_update_payload import LiveStreamUpdatePayload
from apivideo.model.not_found import NotFound
from apivideo.model.too_many_requests import TooManyRequests


class LiveStreamsApi(_EndPoint):

    def create(
            self,
            live_stream_creation_payload,
            **kwargs
        ):
            """Create live stream  # noqa: E501

            Creates a livestream object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create(live_stream_creation_payload, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_creation_payload (LiveStreamCreationPayload):

            Keyword Args:
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
                LiveStream
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
            kwargs['live_stream_creation_payload'] = \
                live_stream_creation_payload

            params_map = {
                'all': [
                    'live_stream_creation_payload',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_creation_payload',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_creation_payload':
                    (LiveStreamCreationPayload,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
            }
            location_map = {
                'live_stream_creation_payload': 'body',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `create`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `create`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`create`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams",
                "POST",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStream,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get(
            self,
            live_stream_id,
            **kwargs
        ):
            """Retrieve live stream  # noqa: E501

            Get a livestream by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get(live_stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique ID for the live stream you want to watch.

            Keyword Args:
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
                LiveStream
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
            kwargs['live_stream_id'] = \
                live_stream_id

            params_map = {
                'all': [
                    'live_stream_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
            }
            location_map = {
                'live_stream_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStream,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def update(
            self,
            live_stream_id,
            live_stream_update_payload,
            **kwargs
        ):
            """Update a live stream  # noqa: E501

            Updates the livestream object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update(live_stream_id, live_stream_update_payload, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique ID for the live stream that you want to update information for such as player details.
                live_stream_update_payload (LiveStreamUpdatePayload):

            Keyword Args:
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
                LiveStream
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
            kwargs['live_stream_id'] = \
                live_stream_id
            kwargs['live_stream_update_payload'] = \
                live_stream_update_payload

            params_map = {
                'all': [
                    'live_stream_id',
                    'live_stream_update_payload',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                    'live_stream_update_payload',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'live_stream_update_payload':
                    (LiveStreamUpdatePayload,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
            }
            location_map = {
                'live_stream_id': 'path',
                'live_stream_update_payload': 'body',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `update`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `update`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`update`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}",
                "PATCH",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStream,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def delete(
            self,
            live_stream_id,
            **kwargs
        ):
            """Delete a live stream  # noqa: E501

            If you do not need a live stream any longer, you can send a request to delete it. All you need is the liveStreamId.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete(live_stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique ID for the live stream that you want to remove.

            Keyword Args:
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
                None
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
            kwargs['live_stream_id'] = \
                live_stream_id

            params_map = {
                'all': [
                    'live_stream_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
            }
            location_map = {
                'live_stream_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `delete`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `delete`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`delete`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}",
                "DELETE",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=None,
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def list(
            self,
            **kwargs
        ):
            """List all live streams  # noqa: E501

            Get the list of livestreams on the workspace.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                stream_key (str): The unique stream key that allows you to stream videos.. [optional]
                name (str): You can filter live streams by their name or a part of their name.. [optional]
                sort_by (str): Enables you to sort live stream results. Allowed attributes: `name`, `createdAt`, `updatedAt`. `name` - the name of the live stream. `createdAt` - the time a live stream was created. `updatedAt` - the time a live stream was last updated.  When using `createdAt` or `updatedAt`, the API sorts the results based on the ISO-8601 time format. . [optional]
                sort_order (str): Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending.. [optional]
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
                LiveStreamListResponse
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
                    'stream_key',
                    'name',
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

                    "NAME": "name",
                    "CREATEDAT": "createdAt",
                    "UPDATEDAT": "updatedAt"
                },
                ('sort_order',): {

                    "ASC": "asc",
                    "DESC": "desc"
                },
            }
            openapi_types = {
                'stream_key':
                    (str,),
                'name':
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
                'stream_key': 'streamKey',
                'name': 'name',
                'sort_by': 'sortBy',
                'sort_order': 'sortOrder',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                'stream_key': 'query',
                'name': 'query',
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
                "/live-streams",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStreamListResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def upload_thumbnail(
            self,
            live_stream_id,
            file,
            **kwargs
        ):
            """Upload a thumbnail  # noqa: E501

            Upload the thumbnail for the livestream.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upload_thumbnail(live_stream_id, file, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique ID for the live stream you want to upload.
                file (file_type): The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB.

            Keyword Args:
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
                LiveStream
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
            kwargs['live_stream_id'] = \
                live_stream_id
            kwargs['file'] = \
                file

            params_map = {
                'all': [
                    'live_stream_id',
                    'file',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                    'file',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'file':
                    (file_type,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
                'file': 'file',
            }
            location_map = {
                'live_stream_id': 'path',
                'file': 'form',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `upload_thumbnail`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `upload_thumbnail`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`upload_thumbnail`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}/thumbnail",
                "POST",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStream,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def delete_thumbnail(
            self,
            live_stream_id,
            **kwargs
        ):
            """Delete a thumbnail  # noqa: E501

            Send the unique identifier for a live stream to delete its thumbnail.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_thumbnail(live_stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique identifier of the live stream whose thumbnail you want to delete.

            Keyword Args:
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
                LiveStream
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
            kwargs['live_stream_id'] = \
                live_stream_id

            params_map = {
                'all': [
                    'live_stream_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
            }
            location_map = {
                'live_stream_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `delete_thumbnail`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `delete_thumbnail`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`delete_thumbnail`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}/thumbnail",
                "DELETE",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(LiveStream,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def complete(
            self,
            live_stream_id,
            **kwargs
        ):
            """Complete a live stream  # noqa: E501

            Request the completion of a live stream that is currently running. This operation is asynchronous and the live stream will stop after a few seconds.   The API adds the `EXT-X-ENDLIST` tag to the live stream's HLS manifest. This stops the live stream on the player and also stops the recording of the live stream. The API keeps the incoming connection from the streamer open for at most 1 minute, which can be used to terminate the stream.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.complete(live_stream_id, async_req=True)
            >>> result = thread.get()

            Args:
                live_stream_id (str): The unique ID for the live stream you want to complete.

            Keyword Args:
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
                None
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
            kwargs['live_stream_id'] = \
                live_stream_id

            params_map = {
                'all': [
                    'live_stream_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'live_stream_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'live_stream_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'live_stream_id': 'liveStreamId',
            }
            location_map = {
                'live_stream_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `complete`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `complete`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`complete`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/live-streams/{liveStreamId}/complete",
                "PUT",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=None,
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

