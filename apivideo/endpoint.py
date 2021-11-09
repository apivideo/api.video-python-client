"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from functools import partial
import io
import math

from apivideo.model_utils import check_allowed_values
from apivideo.model_utils import check_validations
from apivideo.model_utils import file_type
from apivideo.model_utils import validate_and_convert_types


class ChunkIO(io.BytesIO):
    def __init__(self, content: bytes, name: str):
        super().__init__(content)
        self.name = name


class EndPoint(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def _validate_inputs(self, kwargs, params_map, allowed_values, validations, openapi_types):
        for param in params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in params_map['validation']:
            if param in kwargs:
                check_validations(
                    validations,
                    (param,),
                    kwargs[param],
                    configuration=self.api_client.configuration
                )

        for key, value in kwargs.items():
            fixed_val = validate_and_convert_types(
                value,
                openapi_types[key],
                [key],
                False,
                True,
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    @staticmethod
    def _gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {'Accept': 'application/json', 'Content-Type': 'application/json'},
            'path': {},
            'query': []
        }

        for param_name, param_value in kwargs.items():
            param_location = location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = attribute_map[param_name]
                if (param_location == 'form' and
                        openapi_types[param_name] == (file_type,)):
                    params['file'][param_name] = [param_value]
                elif (param_location == 'form' and
                        openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][param_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        if params['file']:
            params['header']['Content-Type'] = 'multipart/form-data'

        return params

    def _chunk_file(self, file_info):
        file_name, files = file_info.popitem()
        file = files[0]
        index = 0
        file.seek(0, 2)
        file_size = file.tell()
        file.seek(0, 0)
        partsCount = math.ceil(file_size/self.api_client.configuration.chunk_size)
        part = 1

        for chunk in iter(partial(file.read, self.api_client.configuration.chunk_size), b''):
            offset = index + len(chunk)
            yield 'part {}/{}'.format(part, partsCount), {file_name: [ChunkIO(chunk, file.name)]}, offset == file_size, offset, file_size
            index = offset
            part = part + 1
