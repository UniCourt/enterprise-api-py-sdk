import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import Field
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.pacer_credential import PacerCredential
from unicourt.model.pacer_credential_list_response import PacerCredentialListResponse
from unicourt.model.pacer_credential_request import PacerCredentialRequest
from unicourt.model.success import Success
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.pacer_credential_api import PACERCredentialApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class PACERCredential:

    @staticmethod
    def add_pacer_credential(
        pacer_credential_request: Optional[PacerCredentialRequest] = None,
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
    ) -> SdkResponse[Success]:

        """Add Pacer Credential.

        Register PACER credentials with UniCourt.

        :param pacer_credential_request:
        :type pacer_credential_request: PacerCredentialRequest
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
            response = PACERCredentialApi(api_client).add_pacer_credential_with_http_info(pacer_credential_request = pacer_credential_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def add_pacer_credential_with_http_info(
        pacer_credential_request: Optional[PacerCredentialRequest] = None,
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
    ) -> ApiResponse[Success]:

        """Add Pacer Credential.

        Register PACER credentials with UniCourt.

        :param pacer_credential_request:
        :type pacer_credential_request: PacerCredentialRequest
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
            return PACERCredentialApi(api_client).add_pacer_credential_with_http_info(pacer_credential_request = pacer_credential_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def add_pacer_credential_without_preload_content(
        pacer_credential_request: Optional[PacerCredentialRequest] = None,
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

        """Add Pacer Credential.

        Register PACER credentials with UniCourt.

        :param pacer_credential_request:
        :type pacer_credential_request: PacerCredentialRequest
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
            response = PACERCredentialApi(api_client).add_pacer_credential_without_preload_content_with_http_info(pacer_credential_request = pacer_credential_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_pacer_credential(
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 ")] = None,
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
    ) -> SdkResponse[PacerCredentialListResponse]:

        """Get Pacer Credential List.

        List registered PACER credentials.

        :param page_number: The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 
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
            response = PACERCredentialApi(api_client).get_pacer_credential_with_http_info(page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_pacer_credential_with_http_info(
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 ")] = None,
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
    ) -> ApiResponse[PacerCredentialListResponse]:

        """Get Pacer Credential List.

        List registered PACER credentials.

        :param page_number: The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 
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
            return PACERCredentialApi(api_client).get_pacer_credential_with_http_info(page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_pacer_credential_without_preload_content(
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 ")] = None,
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

        """Get Pacer Credential List.

        List registered PACER credentials.

        :param page_number: The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1 
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
            response = PACERCredentialApi(api_client).get_pacer_credential_without_preload_content_with_http_info(page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_pacer_credential_by_id(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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
    ) -> SdkResponse[PacerCredential]:

        """Get Pacer Credential for a requested pacer User Id.

        Retrieve the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            response = PACERCredentialApi(api_client).get_pacer_credential_by_id_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_pacer_credential_by_id_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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
    ) -> ApiResponse[PacerCredential]:

        """Get Pacer Credential for a requested pacer User Id.

        Retrieve the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            return PACERCredentialApi(api_client).get_pacer_credential_by_id_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_pacer_credential_by_id_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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

        """Get Pacer Credential for a requested pacer User Id.

        Retrieve the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            response = PACERCredentialApi(api_client).get_pacer_credential_by_id_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def remove_pacer_credential_by_id(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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
    ) -> SdkResponse[Success]:

        """Remove Pacer credential for a specific Pacer User Id.

        De-register the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            response = PACERCredentialApi(api_client).remove_pacer_credential_by_id_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def remove_pacer_credential_by_id_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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
    ) -> ApiResponse[Success]:

        """Remove Pacer credential for a specific Pacer User Id.

        De-register the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            return PACERCredentialApi(api_client).remove_pacer_credential_by_id_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def remove_pacer_credential_by_id_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=40, description="The PACER username for which PACER credentials are to be retrieved.")],
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

        """Remove Pacer credential for a specific Pacer User Id.

        De-register the PACER credentials for the specified PACER username.

        :param pacer_user_id: The PACER username for which PACER credentials are to be retrieved. (required)
        :type pacer_user_id: str
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
            response = PACERCredentialApi(api_client).remove_pacer_credential_by_id_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
