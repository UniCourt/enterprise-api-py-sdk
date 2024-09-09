import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.case_export_callback import CaseExportCallback
from unicourt.model.case_export_callback_list_response import CaseExportCallbackListResponse
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.case_export_api import CaseExportApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CaseExport:

    @staticmethod
    def export_case(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a>")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseExportCallback]:

        """Gets case exported for a requested Case ID.

        Retrieve information about the specified case export.

        :param case_id: The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a> (required)
        :type case_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).export_case_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def export_case_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a>")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseExportCallback]:

        """Gets case exported for a requested Case ID.

        Retrieve information about the specified case export.

        :param case_id: The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a> (required)
        :type case_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).export_case_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def export_case_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a>")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[RESTResponseType]:

        """Gets case exported for a requested Case ID.

        Retrieve information about the specified case export.

        :param case_id: The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseExport\">  WebSocket Callbacks Documentation </a> (required)
        :type case_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).export_case_without_preload_content_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_export_callback_by_id(
        case_export_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseExportCallbackId value of the case export callback object to be retrieved.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseExportCallback]:

        """Get Case Export Callback for a requested Case Export Callback Id.

        Retrieve the specified case export callback object.

        :param case_export_callback_id: The caseExportCallbackId value of the case export callback object to be retrieved. (required)
        :type case_export_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).get_case_export_callback_by_id_with_http_info(case_export_callback_id = case_export_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_export_callback_by_id_with_http_info(
        case_export_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseExportCallbackId value of the case export callback object to be retrieved.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseExportCallback]:

        """Get Case Export Callback for a requested Case Export Callback Id.

        Retrieve the specified case export callback object.

        :param case_export_callback_id: The caseExportCallbackId value of the case export callback object to be retrieved. (required)
        :type case_export_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).get_case_export_callback_by_id_with_http_info(case_export_callback_id = case_export_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_export_callback_by_id_without_preload_content(
        case_export_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseExportCallbackId value of the case export callback object to be retrieved.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[RESTResponseType]:

        """Get Case Export Callback for a requested Case Export Callback Id.

        Retrieve the specified case export callback object.

        :param case_export_callback_id: The caseExportCallbackId value of the case export callback object to be retrieved. (required)
        :type case_export_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).get_case_export_callback_by_id_without_preload_content_with_http_info(case_export_callback_id = case_export_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_export_callbacks(
        date: Annotated[Optional[datetime], Field(description="The date for which callbacks are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="The status code of the callbacks to be retrieved.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the callbacks to be retrieved.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseExportCallbackListResponse]:

        """Get Case Export Callback list for a requested Date.

        Retrieve callbacks according to the specified criteria.

        :param date: The date for which callbacks are to be retrieved.
        :type date: datetime
        :param status: The status code of the callbacks to be retrieved.
        :type status: str
        :param page_number: The page number of the callbacks to be retrieved.<br>   - Minimum: 1 
        :type page_number: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).get_case_export_callbacks_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_export_callbacks_with_http_info(
        date: Annotated[Optional[datetime], Field(description="The date for which callbacks are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="The status code of the callbacks to be retrieved.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the callbacks to be retrieved.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseExportCallbackListResponse]:

        """Get Case Export Callback list for a requested Date.

        Retrieve callbacks according to the specified criteria.

        :param date: The date for which callbacks are to be retrieved.
        :type date: datetime
        :param status: The status code of the callbacks to be retrieved.
        :type status: str
        :param page_number: The page number of the callbacks to be retrieved.<br>   - Minimum: 1 
        :type page_number: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseExportApi(api_client).get_case_export_callbacks_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_export_callbacks_without_preload_content(
        date: Annotated[Optional[datetime], Field(description="The date for which callbacks are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="The status code of the callbacks to be retrieved.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the callbacks to be retrieved.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[RESTResponseType]:

        """Get Case Export Callback list for a requested Date.

        Retrieve callbacks according to the specified criteria.

        :param date: The date for which callbacks are to be retrieved.
        :type date: datetime
        :param status: The status code of the callbacks to be retrieved.
        :type status: str
        :param page_number: The page number of the callbacks to be retrieved.<br>   - Minimum: 1 
        :type page_number: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseExportApi(api_client).get_case_export_callbacks_without_preload_content_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
