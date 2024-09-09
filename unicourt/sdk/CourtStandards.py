import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.area_of_law import AreaOfLaw
from unicourt.model.area_of_law_response import AreaOfLawResponse
from unicourt.model.attorney_representation_type import AttorneyRepresentationType
from unicourt.model.attorney_representation_type_response import AttorneyRepresentationTypeResponse
from unicourt.model.attorney_type import AttorneyType
from unicourt.model.attorney_type_response import AttorneyTypeResponse
from unicourt.model.case_class import CaseClass
from unicourt.model.case_class_response import CaseClassResponse
from unicourt.model.case_relationship_type import CaseRelationshipType
from unicourt.model.case_relationship_type_response import CaseRelationshipTypeResponse
from unicourt.model.case_status import CaseStatus
from unicourt.model.case_status_group import CaseStatusGroup
from unicourt.model.case_status_group_response import CaseStatusGroupResponse
from unicourt.model.case_status_response import CaseStatusResponse
from unicourt.model.case_type import CaseType
from unicourt.model.case_type_group import CaseTypeGroup
from unicourt.model.case_type_group_response import CaseTypeGroupResponse
from unicourt.model.case_type_response import CaseTypeResponse
from unicourt.model.cause_of_action import CauseOfAction
from unicourt.model.cause_of_action_additional_data import CauseOfActionAdditionalData
from unicourt.model.cause_of_action_additional_data_response import CauseOfActionAdditionalDataResponse
from unicourt.model.cause_of_action_group import CauseOfActionGroup
from unicourt.model.cause_of_action_group_response import CauseOfActionGroupResponse
from unicourt.model.cause_of_action_response import CauseOfActionResponse
from unicourt.model.charge import Charge
from unicourt.model.charge_additional_data import ChargeAdditionalData
from unicourt.model.charge_additional_data_response import ChargeAdditionalDataResponse
from unicourt.model.charge_degree import ChargeDegree
from unicourt.model.charge_degree_response import ChargeDegreeResponse
from unicourt.model.charge_group import ChargeGroup
from unicourt.model.charge_group_response import ChargeGroupResponse
from unicourt.model.charge_response import ChargeResponse
from unicourt.model.charge_severity import ChargeSeverity
from unicourt.model.charge_severity_response import ChargeSeverityResponse
from unicourt.model.court import Court
from unicourt.model.court_location import CourtLocation
from unicourt.model.court_location_response import CourtLocationResponse
from unicourt.model.court_response import CourtResponse
from unicourt.model.court_service_status import CourtServiceStatus
from unicourt.model.court_service_status_response import CourtServiceStatusResponse
from unicourt.model.court_system import CourtSystem
from unicourt.model.court_system_response import CourtSystemResponse
from unicourt.model.court_type import CourtType
from unicourt.model.court_type_response import CourtTypeResponse
from unicourt.model.judge_type import JudgeType
from unicourt.model.judge_type_response import JudgeTypeResponse
from unicourt.model.jurisdiction_geo import JurisdictionGeo
from unicourt.model.jurisdiction_geo_response import JurisdictionGeoResponse
from unicourt.model.party_role import PartyRole
from unicourt.model.party_role_group import PartyRoleGroup
from unicourt.model.party_role_group_response import PartyRoleGroupResponse
from unicourt.model.party_role_response import PartyRoleResponse
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.court_standards_api import CourtStandardsApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CourtStandards:

    @staticmethod
    def get_appeal_courts_for_court(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtResponse]:

        """Appeal Court Objects for given courtId.

        Retrieve the appeals courts associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_appeal_courts_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_appeal_courts_for_court_with_http_info(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtResponse]:

        """Appeal Court Objects for given courtId.

        Retrieve the appeals courts associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_appeal_courts_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_appeal_courts_for_court_without_preload_content(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Appeal Court Objects for given courtId.

        Retrieve the appeals courts associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_appeal_courts_for_court_without_preload_content_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_area_of_law(
        area_of_law_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The areaOfLawId value of the desired area of law.")],
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
    ) -> SdkResponse[AreaOfLaw]:

        """AreaOfLaw Object for the given AreaOfLaw Id.

        Retrieve the specified area of law. 

        :param area_of_law_id: The areaOfLawId value of the desired area of law. (required)
        :type area_of_law_id: str
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
            response = CourtStandardsApi(api_client).get_area_of_law_with_http_info(area_of_law_id = area_of_law_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_area_of_law_with_http_info(
        area_of_law_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The areaOfLawId value of the desired area of law.")],
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
    ) -> ApiResponse[AreaOfLaw]:

        """AreaOfLaw Object for the given AreaOfLaw Id.

        Retrieve the specified area of law. 

        :param area_of_law_id: The areaOfLawId value of the desired area of law. (required)
        :type area_of_law_id: str
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
            return CourtStandardsApi(api_client).get_area_of_law_with_http_info(area_of_law_id = area_of_law_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_area_of_law_without_preload_content(
        area_of_law_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The areaOfLawId value of the desired area of law.")],
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

        """AreaOfLaw Object for the given AreaOfLaw Id.

        Retrieve the specified area of law. 

        :param area_of_law_id: The areaOfLawId value of the desired area of law. (required)
        :type area_of_law_id: str
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
            response = CourtStandardsApi(api_client).get_area_of_law_without_preload_content_with_http_info(area_of_law_id = area_of_law_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_areas_of_law(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[AreaOfLawResponse]:

        """AreaOfLaw Object.

        The keyword expression targeting the desired area of law.   ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject 

        :param q: Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_areas_of_law_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_areas_of_law_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[AreaOfLawResponse]:

        """AreaOfLaw Object.

        The keyword expression targeting the desired area of law.   ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject 

        :param q: Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_areas_of_law_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_areas_of_law_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """AreaOfLaw Object.

        The keyword expression targeting the desired area of law.   ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject 

        :param q: Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_areas_of_law_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_representation_type(
        attorney_representation_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyRepresentationTypeId value of the desired attorney representation type.")],
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
    ) -> SdkResponse[AttorneyRepresentationType]:

        """Attorney Representation Type Object for the given attorneyRepresentationTypeId.

        Retrieve the specified attorney representation type. 

        :param attorney_representation_type_id: The attorneyRepresentationTypeId value of the desired attorney representation type. (required)
        :type attorney_representation_type_id: str
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
            response = CourtStandardsApi(api_client).get_attorney_representation_type_with_http_info(attorney_representation_type_id = attorney_representation_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_representation_type_with_http_info(
        attorney_representation_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyRepresentationTypeId value of the desired attorney representation type.")],
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
    ) -> ApiResponse[AttorneyRepresentationType]:

        """Attorney Representation Type Object for the given attorneyRepresentationTypeId.

        Retrieve the specified attorney representation type. 

        :param attorney_representation_type_id: The attorneyRepresentationTypeId value of the desired attorney representation type. (required)
        :type attorney_representation_type_id: str
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
            return CourtStandardsApi(api_client).get_attorney_representation_type_with_http_info(attorney_representation_type_id = attorney_representation_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_representation_type_without_preload_content(
        attorney_representation_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyRepresentationTypeId value of the desired attorney representation type.")],
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

        """Attorney Representation Type Object for the given attorneyRepresentationTypeId.

        Retrieve the specified attorney representation type. 

        :param attorney_representation_type_id: The attorneyRepresentationTypeId value of the desired attorney representation type. (required)
        :type attorney_representation_type_id: str
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
            response = CourtStandardsApi(api_client).get_attorney_representation_type_without_preload_content_with_http_info(attorney_representation_type_id = attorney_representation_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_representation_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney representation type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[AttorneyRepresentationTypeResponse]:

        """Attorney Representation Type Object.

        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above. ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject 

        :param q: The keyword expression targeting the attorney representation type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_attorney_representation_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_representation_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney representation type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[AttorneyRepresentationTypeResponse]:

        """Attorney Representation Type Object.

        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above. ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject 

        :param q: The keyword expression targeting the attorney representation type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_attorney_representation_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_representation_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney representation type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Attorney Representation Type Object.

        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above. ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject 

        :param q: The keyword expression targeting the attorney representation type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_attorney_representation_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_type(
        attorney_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyTypeId value of the desired attorney type.")],
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
    ) -> SdkResponse[AttorneyType]:

        """Attorney Type Object for given Attorney Type Id.

        Retrieve a specified attorney type object. 

        :param attorney_type_id: The attorneyTypeId value of the desired attorney type. (required)
        :type attorney_type_id: str
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
            response = CourtStandardsApi(api_client).get_attorney_type_with_http_info(attorney_type_id = attorney_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_type_with_http_info(
        attorney_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyTypeId value of the desired attorney type.")],
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
    ) -> ApiResponse[AttorneyType]:

        """Attorney Type Object for given Attorney Type Id.

        Retrieve a specified attorney type object. 

        :param attorney_type_id: The attorneyTypeId value of the desired attorney type. (required)
        :type attorney_type_id: str
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
            return CourtStandardsApi(api_client).get_attorney_type_with_http_info(attorney_type_id = attorney_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_type_without_preload_content(
        attorney_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The attorneyTypeId value of the desired attorney type.")],
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

        """Attorney Type Object for given Attorney Type Id.

        Retrieve a specified attorney type object. 

        :param attorney_type_id: The attorneyTypeId value of the desired attorney type. (required)
        :type attorney_type_id: str
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
            response = CourtStandardsApi(api_client).get_attorney_type_without_preload_content_with_http_info(attorney_type_id = attorney_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[AttorneyTypeResponse]:

        """Attorney Type Object.

        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject 

        :param q: The keyword expression targeting the attorney type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_attorney_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_attorney_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[AttorneyTypeResponse]:

        """Attorney Type Object.

        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject 

        :param q: The keyword expression targeting the attorney type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_attorney_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_attorney_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the attorney type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Attorney Type Object.

        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject 

        :param q: The keyword expression targeting the attorney type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_attorney_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_class(
        case_class_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseClassId value of the desired case class.")],
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
    ) -> SdkResponse[CaseClass]:

        """Case Class Object for the given Case Class Id.

        Retrieve the specified case class. 

        :param case_class_id: The caseClassId value of the desired case class. (required)
        :type case_class_id: str
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
            response = CourtStandardsApi(api_client).get_case_class_with_http_info(case_class_id = case_class_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_class_with_http_info(
        case_class_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseClassId value of the desired case class.")],
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
    ) -> ApiResponse[CaseClass]:

        """Case Class Object for the given Case Class Id.

        Retrieve the specified case class. 

        :param case_class_id: The caseClassId value of the desired case class. (required)
        :type case_class_id: str
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
            return CourtStandardsApi(api_client).get_case_class_with_http_info(case_class_id = case_class_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_class_without_preload_content(
        case_class_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseClassId value of the desired case class.")],
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

        """Case Class Object for the given Case Class Id.

        Retrieve the specified case class. 

        :param case_class_id: The caseClassId value of the desired case class. (required)
        :type case_class_id: str
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
            response = CourtStandardsApi(api_client).get_case_class_without_preload_content_with_http_info(case_class_id = case_class_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_relationship_type(
        case_relationship_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseRelationshipTypeId value of the desired case relationship type.")],
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
    ) -> SdkResponse[CaseRelationshipType]:

        """Case Relationship Type Object for the given caseRelationshipTypeId.

        Retrieve the specified case relationship type. 

        :param case_relationship_type_id: The caseRelationshipTypeId value of the desired case relationship type. (required)
        :type case_relationship_type_id: str
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
            response = CourtStandardsApi(api_client).get_case_relationship_type_with_http_info(case_relationship_type_id = case_relationship_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_relationship_type_with_http_info(
        case_relationship_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseRelationshipTypeId value of the desired case relationship type.")],
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
    ) -> ApiResponse[CaseRelationshipType]:

        """Case Relationship Type Object for the given caseRelationshipTypeId.

        Retrieve the specified case relationship type. 

        :param case_relationship_type_id: The caseRelationshipTypeId value of the desired case relationship type. (required)
        :type case_relationship_type_id: str
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
            return CourtStandardsApi(api_client).get_case_relationship_type_with_http_info(case_relationship_type_id = case_relationship_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_relationship_type_without_preload_content(
        case_relationship_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseRelationshipTypeId value of the desired case relationship type.")],
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

        """Case Relationship Type Object for the given caseRelationshipTypeId.

        Retrieve the specified case relationship type. 

        :param case_relationship_type_id: The caseRelationshipTypeId value of the desired case relationship type. (required)
        :type case_relationship_type_id: str
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
            response = CourtStandardsApi(api_client).get_case_relationship_type_without_preload_content_with_http_info(case_relationship_type_id = case_relationship_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_relationship_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the case relationship type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseRelationshipTypeResponse]:

        """Case Relationship Type Object.

        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject 

        :param q: The keyword expression targeting the case relationship type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_relationship_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_relationship_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the case relationship type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseRelationshipTypeResponse]:

        """Case Relationship Type Object.

        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject 

        :param q: The keyword expression targeting the case relationship type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_case_relationship_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_relationship_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the case relationship type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Case Relationship Type Object.

        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject 

        :param q: The keyword expression targeting the case relationship type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_relationship_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status(
        case_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusId value of the desired case status.")],
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
    ) -> SdkResponse[CaseStatus]:

        """Returns the caseStatus information for the given caseStatusId.

        Retrieve the specified case status. 

        :param case_status_id: The caseStatusId value of the desired case status. (required)
        :type case_status_id: str
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
            response = CourtStandardsApi(api_client).get_case_status_with_http_info(case_status_id = case_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status_with_http_info(
        case_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusId value of the desired case status.")],
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
    ) -> ApiResponse[CaseStatus]:

        """Returns the caseStatus information for the given caseStatusId.

        Retrieve the specified case status. 

        :param case_status_id: The caseStatusId value of the desired case status. (required)
        :type case_status_id: str
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
            return CourtStandardsApi(api_client).get_case_status_with_http_info(case_status_id = case_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_status_without_preload_content(
        case_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusId value of the desired case status.")],
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

        """Returns the caseStatus information for the given caseStatusId.

        Retrieve the specified case status. 

        :param case_status_id: The caseStatusId value of the desired case status. (required)
        :type case_status_id: str
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
            response = CourtStandardsApi(api_client).get_case_status_without_preload_content_with_http_info(case_status_id = case_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status_group(
        case_status_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusGroupId value of the desired case status group.")],
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
    ) -> SdkResponse[CaseStatusGroup]:

        """Returns the caseStatusGroup information for the given caseStatusGroupId.

        Retrieve the specified case status group. 

        :param case_status_group_id: The caseStatusGroupId value of the desired case status group. (required)
        :type case_status_group_id: str
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
            response = CourtStandardsApi(api_client).get_case_status_group_with_http_info(case_status_group_id = case_status_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status_group_with_http_info(
        case_status_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusGroupId value of the desired case status group.")],
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
    ) -> ApiResponse[CaseStatusGroup]:

        """Returns the caseStatusGroup information for the given caseStatusGroupId.

        Retrieve the specified case status group. 

        :param case_status_group_id: The caseStatusGroupId value of the desired case status group. (required)
        :type case_status_group_id: str
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
            return CourtStandardsApi(api_client).get_case_status_group_with_http_info(case_status_group_id = case_status_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_status_group_without_preload_content(
        case_status_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseStatusGroupId value of the desired case status group.")],
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

        """Returns the caseStatusGroup information for the given caseStatusGroupId.

        Retrieve the specified case status group. 

        :param case_status_group_id: The caseStatusGroupId value of the desired case status group. (required)
        :type case_status_group_id: str
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
            response = CourtStandardsApi(api_client).get_case_status_group_without_preload_content_with_http_info(case_status_group_id = case_status_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status_groups(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseStatusGroupResponse]:

        """Case Status Group Object.

        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject 

        :param q: The keyword expression targeting the desired case status group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_status_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_status_groups_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseStatusGroupResponse]:

        """Case Status Group Object.

        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject 

        :param q: The keyword expression targeting the desired case status group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_case_status_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_status_groups_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Case Status Group Object.

        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject 

        :param q: The keyword expression targeting the desired case status group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_status_groups_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type(
        case_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseTypeId value of the desired case type.")],
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
    ) -> SdkResponse[CaseType]:

        """CaseType Object for given Case Type Id.

        Retrieve the specified case type. 

        :param case_type_id: The caseTypeId value of the desired case type. (required)
        :type case_type_id: str
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
            response = CourtStandardsApi(api_client).get_case_type_with_http_info(case_type_id = case_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type_with_http_info(
        case_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseTypeId value of the desired case type.")],
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
    ) -> ApiResponse[CaseType]:

        """CaseType Object for given Case Type Id.

        Retrieve the specified case type. 

        :param case_type_id: The caseTypeId value of the desired case type. (required)
        :type case_type_id: str
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
            return CourtStandardsApi(api_client).get_case_type_with_http_info(case_type_id = case_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_type_without_preload_content(
        case_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The caseTypeId value of the desired case type.")],
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

        """CaseType Object for given Case Type Id.

        Retrieve the specified case type. 

        :param case_type_id: The caseTypeId value of the desired case type. (required)
        :type case_type_id: str
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
            response = CourtStandardsApi(api_client).get_case_type_without_preload_content_with_http_info(case_type_id = case_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type_group(
        case_type_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="caseTypeGroupId")],
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
    ) -> SdkResponse[CaseTypeGroup]:

        """CaseType Group for the given CaseType Group Id.

        Retrieve the specified case type group. 

        :param case_type_group_id: caseTypeGroupId (required)
        :type case_type_group_id: str
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
            response = CourtStandardsApi(api_client).get_case_type_group_with_http_info(case_type_group_id = case_type_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type_group_with_http_info(
        case_type_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="caseTypeGroupId")],
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
    ) -> ApiResponse[CaseTypeGroup]:

        """CaseType Group for the given CaseType Group Id.

        Retrieve the specified case type group. 

        :param case_type_group_id: caseTypeGroupId (required)
        :type case_type_group_id: str
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
            return CourtStandardsApi(api_client).get_case_type_group_with_http_info(case_type_group_id = case_type_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_type_group_without_preload_content(
        case_type_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="caseTypeGroupId")],
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

        """CaseType Group for the given CaseType Group Id.

        Retrieve the specified case type group. 

        :param case_type_group_id: caseTypeGroupId (required)
        :type case_type_group_id: str
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
            response = CourtStandardsApi(api_client).get_case_type_group_without_preload_content_with_http_info(case_type_group_id = case_type_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type_groups(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseTypeGroupResponse]:

        """CaseTypeGroup Object.

        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject 

        :param q: Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_type_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_type_groups_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseTypeGroupResponse]:

        """CaseTypeGroup Object.

        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject 

        :param q: Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_case_type_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_type_groups_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """CaseTypeGroup Object.

        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject 

        :param q: Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_type_groups_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseTypeResponse]:

        """Case Type Object.

        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject 

        :param q: Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseTypeResponse]:

        """Case Type Object.

        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject 

        :param q: Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_case_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Case Type Object.

        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject 

        :param q: Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_case_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cases_class(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case class.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseClassResponse]:

        """Case Class Object.

        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject 

        :param q: The keyword expression targeting the desired case class.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_cases_class_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cases_class_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case class.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseClassResponse]:

        """Case Class Object.

        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject 

        :param q: The keyword expression targeting the desired case class.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_cases_class_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_cases_class_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case class.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Case Class Object.

        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject 

        :param q: The keyword expression targeting the desired case class.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_cases_class_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cases_status(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CaseStatusResponse]:

        """Case Status Object.

        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject 

        :param q: The keyword expression targeting the desired case status.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_cases_status_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cases_status_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CaseStatusResponse]:

        """Case Status Object.

        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject 

        :param q: The keyword expression targeting the desired case status.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_cases_status_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_cases_status_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired case status.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Case Status Object.

        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject 

        :param q: The keyword expression targeting the desired case status.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_cases_status_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action(
        cause_of_action_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionId value of the desired cause of action.")],
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
    ) -> SdkResponse[CauseOfAction]:

        """CauseOfAction Object for the given causeOfActionId.

        Retrieve the specified cause of action. 

        :param cause_of_action_id: The causeOfActionId value of the desired cause of action. (required)
        :type cause_of_action_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_with_http_info(cause_of_action_id = cause_of_action_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action_with_http_info(
        cause_of_action_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionId value of the desired cause of action.")],
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
    ) -> ApiResponse[CauseOfAction]:

        """CauseOfAction Object for the given causeOfActionId.

        Retrieve the specified cause of action. 

        :param cause_of_action_id: The causeOfActionId value of the desired cause of action. (required)
        :type cause_of_action_id: str
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
            return CourtStandardsApi(api_client).get_cause_of_action_with_http_info(cause_of_action_id = cause_of_action_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_cause_of_action_without_preload_content(
        cause_of_action_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionId value of the desired cause of action.")],
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

        """CauseOfAction Object for the given causeOfActionId.

        Retrieve the specified cause of action. 

        :param cause_of_action_id: The causeOfActionId value of the desired cause of action. (required)
        :type cause_of_action_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_without_preload_content_with_http_info(cause_of_action_id = cause_of_action_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action_additional_data(
        cause_of_action_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionAdditionalDataId value of the desired cause of action additional data.")],
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
    ) -> SdkResponse[CauseOfActionAdditionalData]:

        """CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.

        Retrieve the specified cause of action additional data. 

        :param cause_of_action_additional_data_id: The causeOfActionAdditionalDataId value of the desired cause of action additional data. (required)
        :type cause_of_action_additional_data_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_additional_data_with_http_info(cause_of_action_additional_data_id = cause_of_action_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action_additional_data_with_http_info(
        cause_of_action_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionAdditionalDataId value of the desired cause of action additional data.")],
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
    ) -> ApiResponse[CauseOfActionAdditionalData]:

        """CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.

        Retrieve the specified cause of action additional data. 

        :param cause_of_action_additional_data_id: The causeOfActionAdditionalDataId value of the desired cause of action additional data. (required)
        :type cause_of_action_additional_data_id: str
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
            return CourtStandardsApi(api_client).get_cause_of_action_additional_data_with_http_info(cause_of_action_additional_data_id = cause_of_action_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_cause_of_action_additional_data_without_preload_content(
        cause_of_action_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The causeOfActionAdditionalDataId value of the desired cause of action additional data.")],
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

        """CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.

        Retrieve the specified cause of action additional data. 

        :param cause_of_action_additional_data_id: The causeOfActionAdditionalDataId value of the desired cause of action additional data. (required)
        :type cause_of_action_additional_data_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_additional_data_without_preload_content_with_http_info(cause_of_action_additional_data_id = cause_of_action_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action_group(
        cause_of_action_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="causeOfActionGroupId")],
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
    ) -> SdkResponse[CauseOfActionGroup]:

        """CauseOfActionGroup Object for the given causeOfActionGroupId.

        Retrieve the specified cause of action group. 

        :param cause_of_action_group_id: causeOfActionGroupId (required)
        :type cause_of_action_group_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_group_with_http_info(cause_of_action_group_id = cause_of_action_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_cause_of_action_group_with_http_info(
        cause_of_action_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="causeOfActionGroupId")],
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
    ) -> ApiResponse[CauseOfActionGroup]:

        """CauseOfActionGroup Object for the given causeOfActionGroupId.

        Retrieve the specified cause of action group. 

        :param cause_of_action_group_id: causeOfActionGroupId (required)
        :type cause_of_action_group_id: str
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
            return CourtStandardsApi(api_client).get_cause_of_action_group_with_http_info(cause_of_action_group_id = cause_of_action_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_cause_of_action_group_without_preload_content(
        cause_of_action_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="causeOfActionGroupId")],
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

        """CauseOfActionGroup Object for the given causeOfActionGroupId.

        Retrieve the specified cause of action group. 

        :param cause_of_action_group_id: causeOfActionGroupId (required)
        :type cause_of_action_group_id: str
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
            response = CourtStandardsApi(api_client).get_cause_of_action_group_without_preload_content_with_http_info(cause_of_action_group_id = cause_of_action_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CauseOfActionResponse]:

        """CauseOfAction Object.

        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject 

        :param q: The keyword expression targeting the desired cause of action.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CauseOfActionResponse]:

        """CauseOfAction Object.

        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject 

        :param q: The keyword expression targeting the desired cause of action.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_causes_of_action_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_causes_of_action_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """CauseOfAction Object.

        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject 

        :param q: The keyword expression targeting the desired cause of action.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action_additional_data(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CauseOfActionAdditionalDataResponse]:

        """CauseOfActionAdditionaData Object.

        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired cause of action additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_additional_data_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action_additional_data_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CauseOfActionAdditionalDataResponse]:

        """CauseOfActionAdditionaData Object.

        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired cause of action additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_causes_of_action_additional_data_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_causes_of_action_additional_data_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """CauseOfActionAdditionaData Object.

        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired cause of action additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_additional_data_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action_group(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CauseOfActionGroupResponse]:

        """CauseOfActionGroup Object.

        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject 

        :param q: The keyword expression targeting the desired cause of action group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_group_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_causes_of_action_group_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CauseOfActionGroupResponse]:

        """CauseOfActionGroup Object.

        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject 

        :param q: The keyword expression targeting the desired cause of action group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_causes_of_action_group_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_causes_of_action_group_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired cause of action group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """CauseOfActionGroup Object.

        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject 

        :param q: The keyword expression targeting the desired cause of action group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_causes_of_action_group_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge(
        charge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeId value of the desired charge.")],
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
    ) -> SdkResponse[Charge]:

        """Charge Object for the given chargeId.

        Retrieve the specified charge. 

        :param charge_id: The chargeId value of the desired charge. (required)
        :type charge_id: str
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
            response = CourtStandardsApi(api_client).get_charge_with_http_info(charge_id = charge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_with_http_info(
        charge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeId value of the desired charge.")],
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
    ) -> ApiResponse[Charge]:

        """Charge Object for the given chargeId.

        Retrieve the specified charge. 

        :param charge_id: The chargeId value of the desired charge. (required)
        :type charge_id: str
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
            return CourtStandardsApi(api_client).get_charge_with_http_info(charge_id = charge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_without_preload_content(
        charge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeId value of the desired charge.")],
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

        """Charge Object for the given chargeId.

        Retrieve the specified charge. 

        :param charge_id: The chargeId value of the desired charge. (required)
        :type charge_id: str
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
            response = CourtStandardsApi(api_client).get_charge_without_preload_content_with_http_info(charge_id = charge_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_additional_data(
        charge_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeAdditionalDataId value of the desired charge additional data.")],
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
    ) -> SdkResponse[ChargeAdditionalData]:

        """Charge Additional Data Object for the given chargeAdditionalDataId.

        Retrieve the specified charge additional data. 

        :param charge_additional_data_id: The chargeAdditionalDataId value of the desired charge additional data. (required)
        :type charge_additional_data_id: str
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
            response = CourtStandardsApi(api_client).get_charge_additional_data_with_http_info(charge_additional_data_id = charge_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_additional_data_with_http_info(
        charge_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeAdditionalDataId value of the desired charge additional data.")],
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
    ) -> ApiResponse[ChargeAdditionalData]:

        """Charge Additional Data Object for the given chargeAdditionalDataId.

        Retrieve the specified charge additional data. 

        :param charge_additional_data_id: The chargeAdditionalDataId value of the desired charge additional data. (required)
        :type charge_additional_data_id: str
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
            return CourtStandardsApi(api_client).get_charge_additional_data_with_http_info(charge_additional_data_id = charge_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_additional_data_without_preload_content(
        charge_additional_data_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeAdditionalDataId value of the desired charge additional data.")],
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

        """Charge Additional Data Object for the given chargeAdditionalDataId.

        Retrieve the specified charge additional data. 

        :param charge_additional_data_id: The chargeAdditionalDataId value of the desired charge additional data. (required)
        :type charge_additional_data_id: str
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
            response = CourtStandardsApi(api_client).get_charge_additional_data_without_preload_content_with_http_info(charge_additional_data_id = charge_additional_data_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_degree(
        charge_degree_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeDegreeId value of the desired charge degree.")],
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
    ) -> SdkResponse[ChargeDegree]:

        """ChargeDegree Object for the given chargeDegreeId.

        Retrieve the specified charge degree. 

        :param charge_degree_id: The chargeDegreeId value of the desired charge degree. (required)
        :type charge_degree_id: str
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
            response = CourtStandardsApi(api_client).get_charge_degree_with_http_info(charge_degree_id = charge_degree_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_degree_with_http_info(
        charge_degree_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeDegreeId value of the desired charge degree.")],
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
    ) -> ApiResponse[ChargeDegree]:

        """ChargeDegree Object for the given chargeDegreeId.

        Retrieve the specified charge degree. 

        :param charge_degree_id: The chargeDegreeId value of the desired charge degree. (required)
        :type charge_degree_id: str
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
            return CourtStandardsApi(api_client).get_charge_degree_with_http_info(charge_degree_id = charge_degree_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_degree_without_preload_content(
        charge_degree_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeDegreeId value of the desired charge degree.")],
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

        """ChargeDegree Object for the given chargeDegreeId.

        Retrieve the specified charge degree. 

        :param charge_degree_id: The chargeDegreeId value of the desired charge degree. (required)
        :type charge_degree_id: str
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
            response = CourtStandardsApi(api_client).get_charge_degree_without_preload_content_with_http_info(charge_degree_id = charge_degree_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_group(
        charge_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeGroupId value of the desired charge group.")],
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
    ) -> SdkResponse[ChargeGroup]:

        """Charge Group Object for the given chargeGroupId.

        Retrieve the specified charge group. 

        :param charge_group_id: The chargeGroupId value of the desired charge group. (required)
        :type charge_group_id: str
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
            response = CourtStandardsApi(api_client).get_charge_group_with_http_info(charge_group_id = charge_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_group_with_http_info(
        charge_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeGroupId value of the desired charge group.")],
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
    ) -> ApiResponse[ChargeGroup]:

        """Charge Group Object for the given chargeGroupId.

        Retrieve the specified charge group. 

        :param charge_group_id: The chargeGroupId value of the desired charge group. (required)
        :type charge_group_id: str
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
            return CourtStandardsApi(api_client).get_charge_group_with_http_info(charge_group_id = charge_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_group_without_preload_content(
        charge_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeGroupId value of the desired charge group.")],
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

        """Charge Group Object for the given chargeGroupId.

        Retrieve the specified charge group. 

        :param charge_group_id: The chargeGroupId value of the desired charge group. (required)
        :type charge_group_id: str
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
            response = CourtStandardsApi(api_client).get_charge_group_without_preload_content_with_http_info(charge_group_id = charge_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_groups(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[ChargeGroupResponse]:

        """Charge Group Object.

        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject 

        :param q: The keyword expression targeting the desired charge group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charge_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_groups_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[ChargeGroupResponse]:

        """Charge Group Object.

        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject 

        :param q: The keyword expression targeting the desired charge group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_charge_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_groups_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Charge Group Object.

        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject 

        :param q: The keyword expression targeting the desired charge group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charge_groups_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_severity(
        charge_severity_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeSeverityId value of the desired charge severity.")],
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
    ) -> SdkResponse[ChargeSeverity]:

        """ChargeSeverity Object for the given chargeSeverityId.

        Retrieve the specified charge severity. 

        :param charge_severity_id: The chargeSeverityId value of the desired charge severity. (required)
        :type charge_severity_id: str
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
            response = CourtStandardsApi(api_client).get_charge_severity_with_http_info(charge_severity_id = charge_severity_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charge_severity_with_http_info(
        charge_severity_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeSeverityId value of the desired charge severity.")],
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
    ) -> ApiResponse[ChargeSeverity]:

        """ChargeSeverity Object for the given chargeSeverityId.

        Retrieve the specified charge severity. 

        :param charge_severity_id: The chargeSeverityId value of the desired charge severity. (required)
        :type charge_severity_id: str
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
            return CourtStandardsApi(api_client).get_charge_severity_with_http_info(charge_severity_id = charge_severity_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charge_severity_without_preload_content(
        charge_severity_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The chargeSeverityId value of the desired charge severity.")],
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

        """ChargeSeverity Object for the given chargeSeverityId.

        Retrieve the specified charge severity. 

        :param charge_severity_id: The chargeSeverityId value of the desired charge severity. (required)
        :type charge_severity_id: str
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
            response = CourtStandardsApi(api_client).get_charge_severity_without_preload_content_with_http_info(charge_severity_id = charge_severity_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[ChargeResponse]:

        """Charge Object.

        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject 

        :param q: The keyword expression targeting the desired charge.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[ChargeResponse]:

        """Charge Object.

        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject 

        :param q: The keyword expression targeting the desired charge.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_charges_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charges_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Charge Object.

        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject 

        :param q: The keyword expression targeting the desired charge.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_additional_data(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[ChargeAdditionalDataResponse]:

        """Charge Additional Data Object.

        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired charge additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_additional_data_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_additional_data_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[ChargeAdditionalDataResponse]:

        """Charge Additional Data Object.

        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired charge additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_charges_additional_data_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charges_additional_data_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge additional data.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Charge Additional Data Object.

        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject 

        :param q: The keyword expression targeting the desired charge additional data.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_additional_data_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_degree(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge degree.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[ChargeDegreeResponse]:

        """ChargeDegree Object.

        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject 

        :param q: The keyword expression targeting the desired charge degree.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_degree_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_degree_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge degree.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[ChargeDegreeResponse]:

        """ChargeDegree Object.

        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject 

        :param q: The keyword expression targeting the desired charge degree.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_charges_degree_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charges_degree_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge degree.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """ChargeDegree Object.

        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject 

        :param q: The keyword expression targeting the desired charge degree.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_degree_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_severity(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge severity.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[ChargeSeverityResponse]:

        """ChargeSeverity Object.

        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject 

        :param q: The keyword expression targeting the desired charge severity.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_severity_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_charges_severity_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge severity.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[ChargeSeverityResponse]:

        """ChargeSeverity Object.

        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject 

        :param q: The keyword expression targeting the desired charge severity.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_charges_severity_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_charges_severity_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired charge severity.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """ChargeSeverity Object.

        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject 

        :param q: The keyword expression targeting the desired charge severity.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_charges_severity_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court(
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
    ) -> SdkResponse[Court]:

        """Court Object for given courtId.

        Retrieve information about a specified court. 

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
            response = CourtStandardsApi(api_client).get_court_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_with_http_info(
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
    ) -> ApiResponse[Court]:

        """Court Object for given courtId.

        Retrieve information about a specified court. 

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
            return CourtStandardsApi(api_client).get_court_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_without_preload_content(
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

        """Court Object for given courtId.

        Retrieve information about a specified court. 

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
            response = CourtStandardsApi(api_client).get_court_without_preload_content_with_http_info(court_id = court_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_location(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="courtLocationId")],
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
    ) -> SdkResponse[CourtLocation]:

        """Courthouse Object for given Court Location Id.

        Contains the Court Location Object. 

        :param court_location_id: courtLocationId (required)
        :type court_location_id: str
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
            response = CourtStandardsApi(api_client).get_court_location_with_http_info(court_location_id = court_location_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_location_with_http_info(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="courtLocationId")],
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
    ) -> ApiResponse[CourtLocation]:

        """Courthouse Object for given Court Location Id.

        Contains the Court Location Object. 

        :param court_location_id: courtLocationId (required)
        :type court_location_id: str
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
            return CourtStandardsApi(api_client).get_court_location_with_http_info(court_location_id = court_location_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_location_without_preload_content(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="courtLocationId")],
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

        """Courthouse Object for given Court Location Id.

        Contains the Court Location Object. 

        :param court_location_id: courtLocationId (required)
        :type court_location_id: str
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
            response = CourtStandardsApi(api_client).get_court_location_without_preload_content_with_http_info(court_location_id = court_location_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_locations(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtLocationResponse]:

        """Courthouse Object.

        Retrieve the specified court location or court locations.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_locations_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_locations_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtLocationResponse]:

        """Courthouse Object.

        Retrieve the specified court location or court locations.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_court_locations_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_locations_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Courthouse Object.

        Retrieve the specified court location or court locations.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_locations_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_locations_for_court(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtLocationResponse]:

        """Associated Court Location for given courtId.

        Retrieve the court locations associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_locations_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_locations_for_court_with_http_info(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtLocationResponse]:

        """Associated Court Location for given courtId.

        Retrieve the court locations associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_court_locations_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_locations_for_court_without_preload_content(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Associated Court Location for given courtId.

        Retrieve the court locations associated with the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_locations_for_court_without_preload_content_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_service_status(
        court_service_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtServiceStatusId value of the desired court.")],
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
    ) -> SdkResponse[CourtServiceStatus]:

        """Court Service Status Object for the given courtServiceStatusId.

        Retrieve the court status of the specified court. 

        :param court_service_status_id: The courtServiceStatusId value of the desired court. (required)
        :type court_service_status_id: str
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
            response = CourtStandardsApi(api_client).get_court_service_status_with_http_info(court_service_status_id = court_service_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_service_status_with_http_info(
        court_service_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtServiceStatusId value of the desired court.")],
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
    ) -> ApiResponse[CourtServiceStatus]:

        """Court Service Status Object for the given courtServiceStatusId.

        Retrieve the court status of the specified court. 

        :param court_service_status_id: The courtServiceStatusId value of the desired court. (required)
        :type court_service_status_id: str
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
            return CourtStandardsApi(api_client).get_court_service_status_with_http_info(court_service_status_id = court_service_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_service_status_without_preload_content(
        court_service_status_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtServiceStatusId value of the desired court.")],
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

        """Court Service Status Object for the given courtServiceStatusId.

        Retrieve the court status of the specified court. 

        :param court_service_status_id: The courtServiceStatusId value of the desired court. (required)
        :type court_service_status_id: str
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
            response = CourtStandardsApi(api_client).get_court_service_status_without_preload_content_with_http_info(court_service_status_id = court_service_status_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_system(
        court_system_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtSystemId value of the court system to be retrieved.")],
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
    ) -> SdkResponse[CourtSystem]:

        """Court System Object for given courtSystemId.

        Retrieve the specified court system. 

        :param court_system_id: The courtSystemId value of the court system to be retrieved. (required)
        :type court_system_id: str
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
            response = CourtStandardsApi(api_client).get_court_system_with_http_info(court_system_id = court_system_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_system_with_http_info(
        court_system_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtSystemId value of the court system to be retrieved.")],
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
    ) -> ApiResponse[CourtSystem]:

        """Court System Object for given courtSystemId.

        Retrieve the specified court system. 

        :param court_system_id: The courtSystemId value of the court system to be retrieved. (required)
        :type court_system_id: str
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
            return CourtStandardsApi(api_client).get_court_system_with_http_info(court_system_id = court_system_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_system_without_preload_content(
        court_system_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtSystemId value of the court system to be retrieved.")],
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

        """Court System Object for given courtSystemId.

        Retrieve the specified court system. 

        :param court_system_id: The courtSystemId value of the court system to be retrieved. (required)
        :type court_system_id: str
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
            response = CourtStandardsApi(api_client).get_court_system_without_preload_content_with_http_info(court_system_id = court_system_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_systems(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtSystemResponse]:

        """Court System Objects.

        Retrieve information about the specified court system or court systems.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_systems_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_systems_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtSystemResponse]:

        """Court System Objects.

        Retrieve information about the specified court system or court systems.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_court_systems_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_systems_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Court System Objects.

        Retrieve information about the specified court system or court systems.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_systems_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_type(
        court_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtTypeId value of the court type to be retrieved.")],
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
    ) -> SdkResponse[CourtType]:

        """Court Type Object for given courtTypeId.

        Retrieve the information concerning the specific court type. 

        :param court_type_id: The courtTypeId value of the court type to be retrieved. (required)
        :type court_type_id: str
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
            response = CourtStandardsApi(api_client).get_court_type_with_http_info(court_type_id = court_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_type_with_http_info(
        court_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtTypeId value of the court type to be retrieved.")],
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
    ) -> ApiResponse[CourtType]:

        """Court Type Object for given courtTypeId.

        Retrieve the information concerning the specific court type. 

        :param court_type_id: The courtTypeId value of the court type to be retrieved. (required)
        :type court_type_id: str
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
            return CourtStandardsApi(api_client).get_court_type_with_http_info(court_type_id = court_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_type_without_preload_content(
        court_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtTypeId value of the court type to be retrieved.")],
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

        """Court Type Object for given courtTypeId.

        Retrieve the information concerning the specific court type. 

        :param court_type_id: The courtTypeId value of the court type to be retrieved. (required)
        :type court_type_id: str
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
            response = CourtStandardsApi(api_client).get_court_type_without_preload_content_with_http_info(court_type_id = court_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtTypeResponse]:

        """Court Type Objects.

        Retrieve court types recognized by UniCourt.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_court_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtTypeResponse]:

        """Court Type Objects.

        Retrieve court types recognized by UniCourt.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_court_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_court_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Court Type Objects.

        Retrieve court types recognized by UniCourt.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_court_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtResponse]:

        """Court Objects.

        Retrieve information about a specified court or courts.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtResponse]:

        """Court Objects.

        Retrieve information about a specified court or courts.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_courts_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_courts_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Court Objects.

        Retrieve information about a specified court or courts.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|         | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject 

        :param q: The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_for_court_location(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtLocationId value of the court location for which courts are to be retrieved.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtResponse]:

        """Associated Court for given Court Location.

        Retrieve the courts associated with the specified court location. 

        :param court_location_id: The courtLocationId value of the court location for which courts are to be retrieved. (required)
        :type court_location_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_for_court_location_with_http_info(court_location_id = court_location_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_for_court_location_with_http_info(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtLocationId value of the court location for which courts are to be retrieved.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtResponse]:

        """Associated Court for given Court Location.

        Retrieve the courts associated with the specified court location. 

        :param court_location_id: The courtLocationId value of the court location for which courts are to be retrieved. (required)
        :type court_location_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_courts_for_court_location_with_http_info(court_location_id = court_location_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_courts_for_court_location_without_preload_content(
        court_location_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtLocationId value of the court location for which courts are to be retrieved.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Associated Court for given Court Location.

        Retrieve the courts associated with the specified court location. 

        :param court_location_id: The courtLocationId value of the court location for which courts are to be retrieved. (required)
        :type court_location_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_for_court_location_without_preload_content_with_http_info(court_location_id = court_location_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_for_jurisdiction_geo(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="jurisdictionGeoId")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page number. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Sort order.")] = None,
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
    ) -> SdkResponse[CourtResponse]:

        """Associated Court for given Jurisdiction Geo.

        Returns Associated Court for given Jurisdiction Geo. 

        :param jurisdiction_geo_id: jurisdictionGeoId (required)
        :type jurisdiction_geo_id: str
        :param page_number: Page number. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: Sort field.
        :type sort: str
        :param order: Sort order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_for_jurisdiction_geo_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_for_jurisdiction_geo_with_http_info(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="jurisdictionGeoId")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page number. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Sort order.")] = None,
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
    ) -> ApiResponse[CourtResponse]:

        """Associated Court for given Jurisdiction Geo.

        Returns Associated Court for given Jurisdiction Geo. 

        :param jurisdiction_geo_id: jurisdictionGeoId (required)
        :type jurisdiction_geo_id: str
        :param page_number: Page number. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: Sort field.
        :type sort: str
        :param order: Sort order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_courts_for_jurisdiction_geo_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_courts_for_jurisdiction_geo_without_preload_content(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="jurisdictionGeoId")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page number. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Sort order.")] = None,
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

        """Associated Court for given Jurisdiction Geo.

        Returns Associated Court for given Jurisdiction Geo. 

        :param jurisdiction_geo_id: jurisdictionGeoId (required)
        :type jurisdiction_geo_id: str
        :param page_number: Page number. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: Sort field.
        :type sort: str
        :param order: Sort order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_for_jurisdiction_geo_without_preload_content_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_service_status(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[CourtServiceStatusResponse]:

        """Court Service Status Object.

        Retrieve the status of one or more courts using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject 

        :param q: The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_service_status_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_courts_service_status_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[CourtServiceStatusResponse]:

        """Court Service Status Object.

        Retrieve the status of one or more courts using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject 

        :param q: The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_courts_service_status_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_courts_service_status_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Court Service Status Object.

        Retrieve the status of one or more courts using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject 

        :param q: The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_courts_service_status_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_type(
        judge_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The judgeTypeId of the desired judge type.")],
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
    ) -> SdkResponse[JudgeType]:

        """Judge Type Object for the given judgeTypeId.

        Retrieve the specified judge type. 

        :param judge_type_id: The judgeTypeId of the desired judge type. (required)
        :type judge_type_id: str
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
            response = CourtStandardsApi(api_client).get_judge_type_with_http_info(judge_type_id = judge_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_type_with_http_info(
        judge_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The judgeTypeId of the desired judge type.")],
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
    ) -> ApiResponse[JudgeType]:

        """Judge Type Object for the given judgeTypeId.

        Retrieve the specified judge type. 

        :param judge_type_id: The judgeTypeId of the desired judge type. (required)
        :type judge_type_id: str
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
            return CourtStandardsApi(api_client).get_judge_type_with_http_info(judge_type_id = judge_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_judge_type_without_preload_content(
        judge_type_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The judgeTypeId of the desired judge type.")],
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

        """Judge Type Object for the given judgeTypeId.

        Retrieve the specified judge type. 

        :param judge_type_id: The judgeTypeId of the desired judge type. (required)
        :type judge_type_id: str
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
            response = CourtStandardsApi(api_client).get_judge_type_without_preload_content_with_http_info(judge_type_id = judge_type_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_types(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the judge type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[JudgeTypeResponse]:

        """Judge Type Object.

        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject 

        :param q: The keyword expression targeting the judge type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_judge_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_judge_types_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the judge type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[JudgeTypeResponse]:

        """Judge Type Object.

        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject 

        :param q: The keyword expression targeting the judge type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_judge_types_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_judge_types_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the judge type.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Judge Type Object.

        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject 

        :param q: The keyword expression targeting the judge type.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_judge_types_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdiction_geo(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The jurisdictionGeoId value of the desired jurisdiction geography.")],
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
    ) -> SdkResponse[JurisdictionGeo]:

        """Jurisdiction Geo Object for given Jurisdiction Geo Id.

        Retrieve the specified jurisdiction geography. 

        :param jurisdiction_geo_id: The jurisdictionGeoId value of the desired jurisdiction geography. (required)
        :type jurisdiction_geo_id: str
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
            response = CourtStandardsApi(api_client).get_jurisdiction_geo_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdiction_geo_with_http_info(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The jurisdictionGeoId value of the desired jurisdiction geography.")],
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
    ) -> ApiResponse[JurisdictionGeo]:

        """Jurisdiction Geo Object for given Jurisdiction Geo Id.

        Retrieve the specified jurisdiction geography. 

        :param jurisdiction_geo_id: The jurisdictionGeoId value of the desired jurisdiction geography. (required)
        :type jurisdiction_geo_id: str
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
            return CourtStandardsApi(api_client).get_jurisdiction_geo_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_jurisdiction_geo_without_preload_content(
        jurisdiction_geo_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The jurisdictionGeoId value of the desired jurisdiction geography.")],
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

        """Jurisdiction Geo Object for given Jurisdiction Geo Id.

        Retrieve the specified jurisdiction geography. 

        :param jurisdiction_geo_id: The jurisdictionGeoId value of the desired jurisdiction geography. (required)
        :type jurisdiction_geo_id: str
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
            response = CourtStandardsApi(api_client).get_jurisdiction_geo_without_preload_content_with_http_info(jurisdiction_geo_id = jurisdiction_geo_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdiction_geo_for_court(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[JurisdictionGeoResponse]:

        """Jurisdiction Geo Objects for given courtId.

        Retrieve the jurisdiction geography object for the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_jurisdiction_geo_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdiction_geo_for_court_with_http_info(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[JurisdictionGeoResponse]:

        """Jurisdiction Geo Objects for given courtId.

        Retrieve the jurisdiction geography object for the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_jurisdiction_geo_for_court_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_jurisdiction_geo_for_court_without_preload_content(
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the target court.")],
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Jurisdiction Geo Objects for given courtId.

        Retrieve the jurisdiction geography object for the specified court. 

        :param court_id: The courtId value of the target court. (required)
        :type court_id: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_jurisdiction_geo_for_court_without_preload_content_with_http_info(court_id = court_id, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdictions_geo(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[JurisdictionGeoResponse]:

        """Jurisdiction Geo Object.

        Retrieve one or more jurisdiction geographies using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject 

        :param q: The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_jurisdictions_geo_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_jurisdictions_geo_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[JurisdictionGeoResponse]:

        """Jurisdiction Geo Object.

        Retrieve one or more jurisdiction geographies using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject 

        :param q: The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_jurisdictions_geo_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_jurisdictions_geo_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Jurisdiction Geo Object.

        Retrieve one or more jurisdiction geographies using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject 

        :param q: The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_jurisdictions_geo_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role(
        party_role_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleId value of the desired party role.")],
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
    ) -> SdkResponse[PartyRole]:

        """Party Role Object.

        Retrieve the specified party role. 

        :param party_role_id: The partyRoleId value of the desired party role. (required)
        :type party_role_id: str
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
            response = CourtStandardsApi(api_client).get_party_role_with_http_info(party_role_id = party_role_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role_with_http_info(
        party_role_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleId value of the desired party role.")],
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
    ) -> ApiResponse[PartyRole]:

        """Party Role Object.

        Retrieve the specified party role. 

        :param party_role_id: The partyRoleId value of the desired party role. (required)
        :type party_role_id: str
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
            return CourtStandardsApi(api_client).get_party_role_with_http_info(party_role_id = party_role_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_role_without_preload_content(
        party_role_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleId value of the desired party role.")],
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

        """Party Role Object.

        Retrieve the specified party role. 

        :param party_role_id: The partyRoleId value of the desired party role. (required)
        :type party_role_id: str
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
            response = CourtStandardsApi(api_client).get_party_role_without_preload_content_with_http_info(party_role_id = party_role_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role_group(
        party_role_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleGroupId value of the desired party role group.")],
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
    ) -> SdkResponse[PartyRoleGroup]:

        """Party Role Group Object.

        Retrieve the specified party role group. 

        :param party_role_group_id: The partyRoleGroupId value of the desired party role group. (required)
        :type party_role_group_id: str
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
            response = CourtStandardsApi(api_client).get_party_role_group_with_http_info(party_role_group_id = party_role_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role_group_with_http_info(
        party_role_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleGroupId value of the desired party role group.")],
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
    ) -> ApiResponse[PartyRoleGroup]:

        """Party Role Group Object.

        Retrieve the specified party role group. 

        :param party_role_group_id: The partyRoleGroupId value of the desired party role group. (required)
        :type party_role_group_id: str
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
            return CourtStandardsApi(api_client).get_party_role_group_with_http_info(party_role_group_id = party_role_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_role_group_without_preload_content(
        party_role_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The partyRoleGroupId value of the desired party role group.")],
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

        """Party Role Group Object.

        Retrieve the specified party role group. 

        :param party_role_group_id: The partyRoleGroupId value of the desired party role group. (required)
        :type party_role_group_id: str
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
            response = CourtStandardsApi(api_client).get_party_role_group_without_preload_content_with_http_info(party_role_group_id = party_role_group_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role_groups(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[PartyRoleGroupResponse]:

        """Party Role Group Object.

        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject 

        :param q: The keyword expression targeting the desired party role group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_party_role_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_role_groups_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[PartyRoleGroupResponse]:

        """Party Role Group Object.

        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject 

        :param q: The keyword expression targeting the desired party role group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_party_role_groups_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_role_groups_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role group.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Party Role Group Object.

        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject 

        :param q: The keyword expression targeting the desired party role group.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_party_role_groups_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_roles(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> SdkResponse[PartyRoleResponse]:

        """Party Role Object.

        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject 

        :param q: The keyword expression targeting the desired party role.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_party_roles_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_party_roles_with_http_info(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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
    ) -> ApiResponse[PartyRoleResponse]:

        """Party Role Object.

        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject 

        :param q: The keyword expression targeting the desired party role.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            return CourtStandardsApi(api_client).get_party_roles_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_party_roles_without_preload_content(
        q: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2000)]], Field(description="The keyword expression targeting the desired party role.</a> ")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="The page number of the results to be retrieved. - minimum: 1 - maximum: 100 ")] = None,
        sort: Annotated[Optional[Annotated[str, Field(min_length=4, strict=True, max_length=4)]], Field(description="The field according to which search results are to be sorted.")] = None,
        order: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]], Field(description="Whether search results are to be shown in ascending or descending order.")] = None,
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

        """Party Role Object.

        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject 

        :param q: The keyword expression targeting the desired party role.</a> 
        :type q: str
        :param page_number: The page number of the results to be retrieved. - minimum: 1 - maximum: 100 
        :type page_number: int
        :param sort: The field according to which search results are to be sorted.
        :type sort: str
        :param order: Whether search results are to be shown in ascending or descending order.
        :type order: str
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
            response = CourtStandardsApi(api_client).get_party_roles_without_preload_content_with_http_info(q = q, page_number = page_number, sort = sort, order = order, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
