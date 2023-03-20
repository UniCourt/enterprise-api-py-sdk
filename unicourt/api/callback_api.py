"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from unicourt.api_client import ApiClient, Endpoint as _Endpoint
from unicourt.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from unicourt.model.callback_list_response import CallbackListResponse
from unicourt.model.exception import Exception


class CallbackApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_callbacks_endpoint = _Endpoint(
            settings={
                'response_type': (CallbackListResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/callbacks',
                'operation_id': 'get_callbacks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'date',
                    'status',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                    'date',
                    'status',
                ]
            },
            root_map={
                'validations': {
                    ('date',): {
                        'max_length': 25,
                        'min_length': 25,
                    },
                    ('status',): {
                        'max_length': 11,
                        'min_length': 7,
                    },
                },
                'allowed_values': {
                    ('status',): {

                        "IN_PROGRESS": "IN_PROGRESS",
                        "COMPLETE": "COMPLETE",
                        "FAILURE": "FAILURE"
                    },
                },
                'openapi_types': {
                    'date':
                        (datetime,),
                    'status':
                        (str,),
                },
                'attribute_map': {
                    'date': 'date',
                    'status': 'status',
                },
                'location_map': {
                    'date': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_callbacks(
        self,
        **kwargs
    ):
        """Get list of callback types with count for a requested Date.  # noqa: E501

        Get list of callback types with count for a requested Date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_callbacks(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            date (datetime): Date for which fetch the callback type list. By default, the date will be set to current date.. [optional]
            status (str): Status of the callbacks. Default status will fetch all callbacks.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CallbackListResponse
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
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_callbacks_endpoint.call_with_http_info(**kwargs)

