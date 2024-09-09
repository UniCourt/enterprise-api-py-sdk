import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import Field
from typing_extensions import Annotated
from unicourt.model.court_coverage import CourtCoverage
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.court_availability_api import CourtAvailabilityApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CourtAvailability:

    @staticmethod
    def get_court_coverage(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
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
    ) -> SdkResponse[CourtCoverage]:

        """Gets Court Coverage of all courts of specific type.

        Determine whether the specified court is covered by UniCourt.

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
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
            response = CourtAvailabilityApi(api_client).get_court_coverage_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_coverage_with_http_info(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
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
    ) -> ApiResponse[CourtCoverage]:

        """Gets Court Coverage of all courts of specific type.

        Determine whether the specified court is covered by UniCourt.

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
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
            return CourtAvailabilityApi(api_client).get_court_coverage_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_coverage_without_preload_content(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
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

        """Gets Court Coverage of all courts of specific type.

        Determine whether the specified court is covered by UniCourt.

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
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
            response = CourtAvailabilityApi(api_client).get_court_coverage_without_preload_content_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
