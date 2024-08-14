import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.attorney import Attorney
from unicourt.model.attorneys import Attorneys
from unicourt.model.case import Case
from unicourt.model.docket_entries import DocketEntries
from unicourt.model.docket_entry_primary_documents import DocketEntryPrimaryDocuments
from unicourt.model.docket_entry_secondary_documents import DocketEntrySecondaryDocuments
from unicourt.model.hearings import Hearings
from unicourt.model.judge import Judge
from unicourt.model.judges import Judges
from unicourt.model.parties import Parties
from unicourt.model.party import Party
from unicourt.model.party_attorney_associations import PartyAttorneyAssociations
from unicourt.model.related_cases import RelatedCases
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.case_docket_api import CaseDocketApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CaseDocket:

    @staticmethod
    def get_attorney_associated_parties(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the parties represented by the attorney with the specified attorneyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PartyAttorneyAssociations]:

        """Gets Associated Party details for a requested Attorney ID.

        Retrieve the parties represented by the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the parties represented by the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_attorney_associated_parties_with_http_info(attorney_id = attorney_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_associated_parties_with_http_info(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the parties represented by the attorney with the specified attorneyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PartyAttorneyAssociations]:

        """Gets Associated Party details for a requested Attorney ID.

        Retrieve the parties represented by the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the parties represented by the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_attorney_associated_parties_with_http_info(attorney_id = attorney_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_associated_parties_without_preload_content(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the parties represented by the attorney with the specified attorneyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Associated Party details for a requested Attorney ID.

        Retrieve the parties represented by the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the parties represented by the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_attorney_associated_parties_without_preload_content_with_http_info(attorney_id = attorney_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_by_id(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the attorney with the specified attorneyId value.")],
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
    ) -> SdkResponse[Attorney]:

        """Gets details for a requested Attorney ID.

        Retrieve the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
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
            response = CaseDocketApi(api_client).get_attorney_by_id_with_http_info(attorney_id = attorney_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_by_id_with_http_info(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the attorney with the specified attorneyId value.")],
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
    ) -> ApiResponse[Attorney]:

        """Gets details for a requested Attorney ID.

        Retrieve the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
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
            return CaseDocketApi(api_client).get_attorney_by_id_with_http_info(attorney_id = attorney_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_by_id_without_preload_content(
        attorney_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the attorney with the specified attorneyId value.")],
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

        """Gets details for a requested Attorney ID.

        Retrieve the attorney with the specified attorneyId value.

        :param attorney_id: Retrieve the attorney with the specified attorneyId value. (required)
        :type attorney_id: str
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
            response = CaseDocketApi(api_client).get_attorney_by_id_without_preload_content_with_http_info(attorney_id = attorney_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
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
    ) -> SdkResponse[Case]:

        """Gets case information for a requested Case ID.

        Retrieve the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
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
            response = CaseDocketApi(api_client).get_case_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
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
    ) -> ApiResponse[Case]:

        """Gets case information for a requested Case ID.

        Retrieve the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
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
            return CaseDocketApi(api_client).get_case_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
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

        """Gets case information for a requested Case ID.

        Retrieve the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
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
            response = CaseDocketApi(api_client).get_case_without_preload_content_with_http_info(case_id = case_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_attorneys(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[Attorneys]:

        """Gets Attorneys for a requested Case ID.

        Retrieve the attorneys in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_attorneys_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_attorneys_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[Attorneys]:

        """Gets Attorneys for a requested Case ID.

        Retrieve the attorneys in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_case_attorneys_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_attorneys_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Attorneys for a requested Case ID.

        Retrieve the attorneys in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_attorneys_without_preload_content_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_docket_entries(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        docket_number: Annotated[Optional[StrictInt], Field(description="Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort the retrieved docket entries in ascending order or descending order of date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[DocketEntries]:

        """Gets Docket Entries for a requested Case ID.

        Retrieve the docket entries in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param docket_number: Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.
        :type docket_number: int
        :param sort_by: Sort the retrieved docket entries in ascending order or descending order of date.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_docket_entries_with_http_info(case_id = case_id, docket_number = docket_number, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_docket_entries_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        docket_number: Annotated[Optional[StrictInt], Field(description="Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort the retrieved docket entries in ascending order or descending order of date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[DocketEntries]:

        """Gets Docket Entries for a requested Case ID.

        Retrieve the docket entries in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param docket_number: Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.
        :type docket_number: int
        :param sort_by: Sort the retrieved docket entries in ascending order or descending order of date.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_case_docket_entries_with_http_info(case_id = case_id, docket_number = docket_number, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_docket_entries_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        docket_number: Annotated[Optional[StrictInt], Field(description="Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort the retrieved docket entries in ascending order or descending order of date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Docket Entries for a requested Case ID.

        Retrieve the docket entries in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param docket_number: Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.
        :type docket_number: int
        :param sort_by: Sort the retrieved docket entries in ascending order or descending order of date.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_docket_entries_without_preload_content_with_http_info(case_id = case_id, docket_number = docket_number, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_hearings(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        sort_by: Annotated[Optional[StrictStr], Field(description="Specify the sort order of hearings in the case with the specified caseId.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[Hearings]:

        """Gets Hearings for a requested Case ID.

        Gets Hearings for a requested Case ID.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param sort_by: Specify the sort order of hearings in the case with the specified caseId.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_hearings_with_http_info(case_id = case_id, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_hearings_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        sort_by: Annotated[Optional[StrictStr], Field(description="Specify the sort order of hearings in the case with the specified caseId.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[Hearings]:

        """Gets Hearings for a requested Case ID.

        Gets Hearings for a requested Case ID.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param sort_by: Specify the sort order of hearings in the case with the specified caseId.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_case_hearings_with_http_info(case_id = case_id, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_hearings_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        sort_by: Annotated[Optional[StrictStr], Field(description="Specify the sort order of hearings in the case with the specified caseId.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Hearings for a requested Case ID.

        Gets Hearings for a requested Case ID.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param sort_by: Specify the sort order of hearings in the case with the specified caseId.
        :type sort_by: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_hearings_without_preload_content_with_http_info(case_id = case_id, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_judges(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[Judges]:

        """Gets Judges for a requested Case ID.

        Retrieve the judges involved in the specified case.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_judges_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_judges_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[Judges]:

        """Gets Judges for a requested Case ID.

        Retrieve the judges involved in the specified case.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_case_judges_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_judges_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Judges for a requested Case ID.

        Retrieve the judges involved in the specified case.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_judges_without_preload_content_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_parties(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
        party_role_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.")] = None,
        party_role_group_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.")] = None,
        attorney_representation_type_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.")] = None,
        party_classification_type: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=10)]], Field(description="Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.")] = None,
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
    ) -> SdkResponse[Parties]:

        """Gets Parties for a requested Case ID.

        Retrieve the parties involved in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
        :type page_number: int
        :param party_role_id: Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.
        :type party_role_id: str
        :param party_role_group_id: Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.
        :type party_role_group_id: str
        :param attorney_representation_type_id: Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.
        :type attorney_representation_type_id: str
        :param party_classification_type: Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.
        :type party_classification_type: str
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
            response = CaseDocketApi(api_client).get_case_parties_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, party_role_id = party_role_id, party_role_group_id = party_role_group_id, attorney_representation_type_id = attorney_representation_type_id, party_classification_type = party_classification_type, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_parties_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
        party_role_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.")] = None,
        party_role_group_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.")] = None,
        attorney_representation_type_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.")] = None,
        party_classification_type: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=10)]], Field(description="Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.")] = None,
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
    ) -> ApiResponse[Parties]:

        """Gets Parties for a requested Case ID.

        Retrieve the parties involved in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
        :type page_number: int
        :param party_role_id: Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.
        :type party_role_id: str
        :param party_role_group_id: Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.
        :type party_role_group_id: str
        :param attorney_representation_type_id: Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.
        :type attorney_representation_type_id: str
        :param party_classification_type: Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.
        :type party_classification_type: str
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
            return CaseDocketApi(api_client).get_case_parties_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, party_role_id = party_role_id, party_role_group_id = party_role_group_id, attorney_representation_type_id = attorney_representation_type_id, party_classification_type = party_classification_type, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_parties_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        is_visible: Annotated[Optional[StrictBool], Field(description="Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
        party_role_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.")] = None,
        party_role_group_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.")] = None,
        attorney_representation_type_id: Annotated[Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]], Field(description="Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.")] = None,
        party_classification_type: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=10)]], Field(description="Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.")] = None,
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

        """Gets Parties for a requested Case ID.

        Retrieve the parties involved in the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param is_visible: Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.
        :type is_visible: bool
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
        :type page_number: int
        :param party_role_id: Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.
        :type party_role_id: str
        :param party_role_group_id: Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.
        :type party_role_group_id: str
        :param attorney_representation_type_id: Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.
        :type attorney_representation_type_id: str
        :param party_classification_type: Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.
        :type party_classification_type: str
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
            response = CaseDocketApi(api_client).get_case_parties_without_preload_content_with_http_info(case_id = case_id, is_visible = is_visible, page_number = page_number, party_role_id = party_role_id, party_role_group_id = party_role_group_id, attorney_representation_type_id = attorney_representation_type_id, party_classification_type = party_classification_type, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_related_cases(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[RelatedCases]:

        """Gets Related Cases for a requested Case ID.

        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_related_cases_with_http_info(case_id = case_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_related_cases_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[RelatedCases]:

        """Gets Related Cases for a requested Case ID.

        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_case_related_cases_with_http_info(case_id = case_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_related_cases_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Related Cases for a requested Case ID.

        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_case_related_cases_without_preload_content_with_http_info(case_id = case_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_by_id(
        judge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the judge with the specified judgeId value.")],
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
    ) -> SdkResponse[Judge]:

        """Gets details for a requested Judge ID.

        Retrieve the judge with the specified judgeId value.

        :param judge_id: Retrieve the judge with the specified judgeId value. (required)
        :type judge_id: str
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
            response = CaseDocketApi(api_client).get_judge_by_id_with_http_info(judge_id = judge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_by_id_with_http_info(
        judge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the judge with the specified judgeId value.")],
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
    ) -> ApiResponse[Judge]:

        """Gets details for a requested Judge ID.

        Retrieve the judge with the specified judgeId value.

        :param judge_id: Retrieve the judge with the specified judgeId value. (required)
        :type judge_id: str
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
            return CaseDocketApi(api_client).get_judge_by_id_with_http_info(judge_id = judge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_judge_by_id_without_preload_content(
        judge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the judge with the specified judgeId value.")],
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

        """Gets details for a requested Judge ID.

        Retrieve the judge with the specified judgeId value.

        :param judge_id: Retrieve the judge with the specified judgeId value. (required)
        :type judge_id: str
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
            response = CaseDocketApi(api_client).get_judge_by_id_without_preload_content_with_http_info(judge_id = judge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_associated_attorneys(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PartyAttorneyAssociations]:

        """Gets Associated Attorney details for a requested Party ID.

        Retrieve the attorneys in the case with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_party_associated_attorneys_with_http_info(party_id = party_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_associated_attorneys_with_http_info(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PartyAttorneyAssociations]:

        """Gets Associated Attorney details for a requested Party ID.

        Retrieve the attorneys in the case with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_party_associated_attorneys_with_http_info(party_id = party_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_associated_attorneys_without_preload_content(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Associated Attorney details for a requested Party ID.

        Retrieve the attorneys in the case with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_party_associated_attorneys_without_preload_content_with_http_info(party_id = party_id, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_by_id(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
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
    ) -> SdkResponse[Party]:

        """Gets details for a requested Party ID.

        Retrieve the party with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
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
            response = CaseDocketApi(api_client).get_party_by_id_with_http_info(party_id = party_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_by_id_with_http_info(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
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
    ) -> ApiResponse[Party]:

        """Gets details for a requested Party ID.

        Retrieve the party with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
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
            return CaseDocketApi(api_client).get_party_by_id_with_http_info(party_id = party_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_by_id_without_preload_content(
        party_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the party with the specified partyId value.")],
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

        """Gets details for a requested Party ID.

        Retrieve the party with the specified partyId value.

        :param party_id: Retrieve the party with the specified partyId value. (required)
        :type party_id: str
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
            response = CaseDocketApi(api_client).get_party_by_id_without_preload_content_with_http_info(party_id = party_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_primary_documents_for_docket_entries(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[DocketEntryPrimaryDocuments]:

        """Gets Primary Documents of Docket Entries.

        Retrieve the primary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_primary_documents_for_docket_entries_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_primary_documents_for_docket_entries_with_http_info(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[DocketEntryPrimaryDocuments]:

        """Gets Primary Documents of Docket Entries.

        Retrieve the primary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_primary_documents_for_docket_entries_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_primary_documents_for_docket_entries_without_preload_content(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Primary Documents of Docket Entries.

        Retrieve the primary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_primary_documents_for_docket_entries_without_preload_content_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_secondary_documents_for_docket_entries(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[DocketEntrySecondaryDocuments]:

        """Gets Secondary Documents of Docket Entries.

        Retrieve the secondary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_secondary_documents_for_docket_entries_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_secondary_documents_for_docket_entries_with_http_info(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[DocketEntrySecondaryDocuments]:

        """Gets Secondary Documents of Docket Entries.

        Retrieve the secondary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            return CaseDocketApi(api_client).get_secondary_documents_for_docket_entries_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_secondary_documents_for_docket_entries_without_preload_content(
        docket_number: Annotated[StrictInt, Field(description="Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.")],
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Retrieve the case with the specified caseId value.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="Query parameter specifying the page number of the search results to be retrieved.")] = None,
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

        """Gets Secondary Documents of Docket Entries.

        Retrieve the secondary documents in the case with the specified caseId value.

        :param docket_number: Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value. (required)
        :type docket_number: int
        :param case_id: Retrieve the case with the specified caseId value. (required)
        :type case_id: str
        :param in_library: Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.
        :type in_library: bool
        :param after_first_fetch_date: Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
        :type after_first_fetch_date: datetime
        :param library_date: Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
        :type library_date: datetime
        :param page_number: Query parameter specifying the page number of the search results to be retrieved.
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
            response = CaseDocketApi(api_client).get_secondary_documents_for_docket_entries_without_preload_content_with_http_info(docket_number = docket_number, case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
