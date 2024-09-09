import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.case_update import CaseUpdate
from unicourt.model.case_update_list_response import CaseUpdateListResponse
from unicourt.model.case_update_request import CaseUpdateRequest
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.case_update_api import CaseUpdateApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CaseUpdate:

    @staticmethod
    def get_case_update_by_case_id(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case object for which updates are to be retrieved.")],
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
    ) -> SdkResponse[CaseUpdate]:

        """Get Case Updates for a requested CaseId.

        Retrieve case updates for the specified case object.

        :param case_id: The caseId value of the case object for which updates are to be retrieved. (required)
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
            response = CaseUpdateApi(api_client).get_case_update_by_case_id_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_update_by_case_id_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case object for which updates are to be retrieved.")],
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
    ) -> ApiResponse[CaseUpdate]:

        """Get Case Updates for a requested CaseId.

        Retrieve case updates for the specified case object.

        :param case_id: The caseId value of the case object for which updates are to be retrieved. (required)
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
            return CaseUpdateApi(api_client).get_case_update_by_case_id_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_update_by_case_id_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseId value of the case object for which updates are to be retrieved.")],
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

        """Get Case Updates for a requested CaseId.

        Retrieve case updates for the specified case object.

        :param case_id: The caseId value of the case object for which updates are to be retrieved. (required)
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
            response = CaseUpdateApi(api_client).get_case_update_by_case_id_without_preload_content_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_updates(
        case_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="The caseId value of the case for which updates should be retrieved.")] = None,
        requested_date: Annotated[Optional[datetime], Field(description="The date for which case updates are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the case updates to be retrieved.")] = None,
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
    ) -> SdkResponse[CaseUpdateListResponse]:

        """Get Case Update  list for a requested Date.

        Retrieve case updates for the specified date.

        :param case_id: The caseId value of the case for which updates should be retrieved.
        :type case_id: str
        :param requested_date: The date for which case updates are to be retrieved.
        :type requested_date: datetime
        :param status: Status of the case updates to be retrieved.
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
            response = CaseUpdateApi(api_client).get_case_updates_with_http_info(case_id = case_id, requested_date = requested_date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_updates_with_http_info(
        case_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="The caseId value of the case for which updates should be retrieved.")] = None,
        requested_date: Annotated[Optional[datetime], Field(description="The date for which case updates are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the case updates to be retrieved.")] = None,
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
    ) -> ApiResponse[CaseUpdateListResponse]:

        """Get Case Update  list for a requested Date.

        Retrieve case updates for the specified date.

        :param case_id: The caseId value of the case for which updates should be retrieved.
        :type case_id: str
        :param requested_date: The date for which case updates are to be retrieved.
        :type requested_date: datetime
        :param status: Status of the case updates to be retrieved.
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
            return CaseUpdateApi(api_client).get_case_updates_with_http_info(case_id = case_id, requested_date = requested_date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_updates_without_preload_content(
        case_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="The caseId value of the case for which updates should be retrieved.")] = None,
        requested_date: Annotated[Optional[datetime], Field(description="The date for which case updates are to be retrieved.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the case updates to be retrieved.")] = None,
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

        """Get Case Update  list for a requested Date.

        Retrieve case updates for the specified date.

        :param case_id: The caseId value of the case for which updates should be retrieved.
        :type case_id: str
        :param requested_date: The date for which case updates are to be retrieved.
        :type requested_date: datetime
        :param status: Status of the case updates to be retrieved.
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
            response = CaseUpdateApi(api_client).get_case_updates_without_preload_content_with_http_info(case_id = case_id, requested_date = requested_date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def update_case(
        case_update_request: Optional[CaseUpdateRequest] = None,
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
    ) -> SdkResponse[CaseUpdate]:

        """Add Case Update for the requested Case Id.

        Request case updates for the specified case. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Update request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseUpdate\">  WebSocket Callbacks Documentation </a>

        :param case_update_request:
        :type case_update_request: CaseUpdateRequest
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
            response = CaseUpdateApi(api_client).update_case_with_http_info(case_update_request = case_update_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def update_case_with_http_info(
        case_update_request: Optional[CaseUpdateRequest] = None,
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
    ) -> ApiResponse[CaseUpdate]:

        """Add Case Update for the requested Case Id.

        Request case updates for the specified case. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Update request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseUpdate\">  WebSocket Callbacks Documentation </a>

        :param case_update_request:
        :type case_update_request: CaseUpdateRequest
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
            return CaseUpdateApi(api_client).update_case_with_http_info(case_update_request = case_update_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def update_case_without_preload_content(
        case_update_request: Optional[CaseUpdateRequest] = None,
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

        """Add Case Update for the requested Case Id.

        Request case updates for the specified case. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Update request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseUpdate\">  WebSocket Callbacks Documentation </a>

        :param case_update_request:
        :type case_update_request: CaseUpdateRequest
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
            response = CaseUpdateApi(api_client).update_case_without_preload_content_with_http_info(case_update_request = case_update_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
