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
from apivideo.model.conflict_error import ConflictError
from apivideo.model.get_summaries import GetSummaries
from apivideo.model.inline_object import InlineObject
from apivideo.model.not_found import NotFound
from apivideo.model.summary_object import SummaryObject
from apivideo.model.summary_source import SummarySource
from apivideo.model.update_summary_request import UpdateSummaryRequest


class SummariesApi(_EndPoint):

    def create(
            self,
            inline_object,
            **kwargs
        ):
            """Generate video summary  # noqa: E501

            Generate a title, abstract, and key takeaways for a video.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create(inline_object, async_req=True)
            >>> result = thread.get()

            Args:
                inline_object (InlineObject):

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
                SummaryObject
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
            kwargs['inline_object'] = \
                inline_object

            params_map = {
                'all': [
                    'inline_object',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'inline_object',
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
                'inline_object':
                    (InlineObject,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
            }
            location_map = {
                'inline_object': 'body',
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
                "/summaries",
                "POST",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(SummaryObject,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get(
            self,
            summary_id,
            **kwargs
        ):
            """Get summary details  # noqa: E501

            Get all details for a summary.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get(summary_id, async_req=True)
            >>> result = thread.get()

            Args:
                summary_id (str): The unique identifier of the summary source you want to retrieve.

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
                SummarySource
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
            kwargs['summary_id'] = \
                summary_id

            params_map = {
                'all': [
                    'summary_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'summary_id',
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
                'summary_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'summary_id': 'summaryId',
            }
            location_map = {
                'summary_id': 'path',
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
                "/summaries/{summaryId}/source",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(SummarySource,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def update(
            self,
            summary_id,
            update_summary_request,
            **kwargs
        ):
            """Update summary details  # noqa: E501

            Update details for a summary. Note that this operation is only allowed for summary objects where `sourceStatus` is `missing`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update(summary_id, update_summary_request, async_req=True)
            >>> result = thread.get()

            Args:
                summary_id (str): The unique identifier of the summary source you want to update.
                update_summary_request (UpdateSummaryRequest):

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
                SummarySource
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
            kwargs['summary_id'] = \
                summary_id
            kwargs['update_summary_request'] = \
                update_summary_request

            params_map = {
                'all': [
                    'summary_id',
                    'update_summary_request',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'summary_id',
                    'update_summary_request',
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
                'summary_id':
                    (str,),
                'update_summary_request':
                    (UpdateSummaryRequest,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'summary_id': 'summaryId',
            }
            location_map = {
                'summary_id': 'path',
                'update_summary_request': 'body',
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
                "/summaries/{summaryId}/source",
                "PATCH",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(SummarySource,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def delete(
            self,
            summary_id,
            **kwargs
        ):
            """Delete video summary  # noqa: E501

            Delete a summary tied to a video.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete(summary_id, async_req=True)
            >>> result = thread.get()

            Args:
                summary_id (str): The unique identifier of the summary you want to delete.

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
            kwargs['summary_id'] = \
                summary_id

            params_map = {
                'all': [
                    'summary_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'summary_id',
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
                'summary_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'summary_id': 'summaryId',
            }
            location_map = {
                'summary_id': 'path',
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
                "/summaries/{summaryId}",
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
            """List summaries  # noqa: E501

            List all summarries for your videos in a project.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


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
                GetSummaries
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
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
            }
            location_map = {
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
                "/summaries",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(GetSummaries,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

