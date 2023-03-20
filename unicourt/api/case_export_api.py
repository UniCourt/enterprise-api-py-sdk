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
from unicourt.model.case_export_callback import CaseExportCallback
from unicourt.model.case_export_callback_list_response import CaseExportCallbackListResponse
from unicourt.model.exception import Exception


class CaseExportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.export_case_endpoint = _Endpoint(
            settings={
                'response_type': (CaseExportCallback,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/caseExport/{caseId}',
                'operation_id': 'export_case',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'case_id',
                ],
                'required': [
                    'case_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'case_id',
                ]
            },
            root_map={
                'validations': {
                    ('case_id',): {
                        'max_length': 18,
                        'min_length': 18,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'case_id':
                        (str,),
                },
                'attribute_map': {
                    'case_id': 'caseId',
                },
                'location_map': {
                    'case_id': 'path',
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
        self.get_case_export_callback_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (CaseExportCallback,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/caseExport/callbacks/{caseExportCallbackId}',
                'operation_id': 'get_case_export_callback_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'case_export_callback_id',
                ],
                'required': [
                    'case_export_callback_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'case_export_callback_id',
                ]
            },
            root_map={
                'validations': {
                    ('case_export_callback_id',): {
                        'max_length': 18,
                        'min_length': 18,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'case_export_callback_id':
                        (str,),
                },
                'attribute_map': {
                    'case_export_callback_id': 'caseExportCallbackId',
                },
                'location_map': {
                    'case_export_callback_id': 'path',
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
        self.get_case_export_callbacks_endpoint = _Endpoint(
            settings={
                'response_type': (CaseExportCallbackListResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/caseExport/callbacks',
                'operation_id': 'get_case_export_callbacks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'date',
                    'status',
                    'page_number',
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
                    'page_number',
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
                    ('page_number',): {

                        'inclusive_minimum': 1,
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
                    'page_number':
                        (int,),
                },
                'attribute_map': {
                    'date': 'date',
                    'status': 'status',
                    'page_number': 'pageNumber',
                },
                'location_map': {
                    'date': 'query',
                    'status': 'query',
                    'page_number': 'query',
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

    def export_case(
        self,
        case_id,
        **kwargs
    ):
        """Gets case exported for a requested Case ID.  # noqa: E501

        Retrieve information about the specified case export.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_case(case_id, async_req=True)
        >>> result = thread.get()

        Args:
            case_id (str): The caseId value of the case for which case export information is to be retrieved.

        Keyword Args:
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
            CaseExportCallback
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
        kwargs['case_id'] = \
            case_id
        return self.export_case_endpoint.call_with_http_info(**kwargs)

    def get_case_export_callback_by_id(
        self,
        case_export_callback_id,
        **kwargs
    ):
        """Get Case Export Callback for a requested Case Export Callback Id.  # noqa: E501

        Retrieve the specified case export callback object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_case_export_callback_by_id(case_export_callback_id, async_req=True)
        >>> result = thread.get()

        Args:
            case_export_callback_id (str): The caseExportCallbackId value of the case export callback object to be retrieved.

        Keyword Args:
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
            CaseExportCallback
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
        kwargs['case_export_callback_id'] = \
            case_export_callback_id
        return self.get_case_export_callback_by_id_endpoint.call_with_http_info(**kwargs)

    def get_case_export_callbacks(
        self,
        **kwargs
    ):
        """Get Case Export Callback list for a requested Date.  # noqa: E501

        Retrieve callbacks according to the specified criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_case_export_callbacks(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            date (datetime): The date for which callbacks are to be retrieved.. [optional]
            status (str): The status code of the callbacks to be retrieved.. [optional]
            page_number (int): The page number of the callbacks to be retrieved.<br>   - Minimum: 1 . [optional] if omitted the server will use the default value of 1
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
            CaseExportCallbackListResponse
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
        return self.get_case_export_callbacks_endpoint.call_with_http_info(**kwargs)

