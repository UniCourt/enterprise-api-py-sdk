import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.callback_list_response import CallbackListResponse
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.callback_api import CallbackApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class Callback:

    @staticmethod
    def get_callbacks(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the callback type list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the callbacks. Default status will fetch all callbacks.")] = None,
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
    ) -> SdkResponse[CallbackListResponse]:

        """Get list of callback types with count for a requested Date.

        Get list of callback types with count for a requested Date.

        :param date: Date for which fetch the callback type list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of the callbacks. Default status will fetch all callbacks.
        :type status: str
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
            response = CallbackApi(api_client).get_callbacks_with_http_info(date = date, status = status, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_callbacks_with_http_info(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the callback type list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the callbacks. Default status will fetch all callbacks.")] = None,
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
    ) -> ApiResponse[CallbackListResponse]:

        """Get list of callback types with count for a requested Date.

        Get list of callback types with count for a requested Date.

        :param date: Date for which fetch the callback type list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of the callbacks. Default status will fetch all callbacks.
        :type status: str
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
            return CallbackApi(api_client).get_callbacks_with_http_info(date = date, status = status, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_callbacks_without_preload_content(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the callback type list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of the callbacks. Default status will fetch all callbacks.")] = None,
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

        """Get list of callback types with count for a requested Date.

        Get list of callback types with count for a requested Date.

        :param date: Date for which fetch the callback type list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of the callbacks. Default status will fetch all callbacks.
        :type status: str
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
            response = CallbackApi(api_client).get_callbacks_without_preload_content_with_http_info(date = date, status = status, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
