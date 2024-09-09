import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from unicourt.model.pacer_import_case import PACERImportCase
from unicourt.model.pcl_case import PCLCase
from unicourt.model.pcl_party import PCLParty
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.pacer_api import PACERApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class PACER:

    @staticmethod
    def all_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search all courts within the PACER system for a particular case.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).all_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def all_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search all courts within the PACER system for a particular case.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).all_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def all_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search all courts within the PACER system for a particular case.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).all_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def all_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER case filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).all_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def all_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER case filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).all_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def all_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER case filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).all_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def appeal_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for PACER cases filed in U.S. Courts of Appeals.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).appeal_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def appeal_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for PACER cases filed in U.S. Courts of Appeals.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).appeal_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def appeal_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for PACER cases filed in U.S. Courts of Appeals.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).appeal_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def appeal_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER appeals cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).appeal_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def appeal_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER appeals cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).appeal_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def appeal_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party across all PACER appeals cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).appeal_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        federal_bankruptcy_chapter_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for Bankruptcy Courts.

        Search for PACER cases filed in U.S. Bankruptcy Courts.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param federal_bankruptcy_chapter_array: The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11
        :type federal_bankruptcy_chapter_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).bankruptcy_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, federal_bankruptcy_chapter_array = federal_bankruptcy_chapter_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        federal_bankruptcy_chapter_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for Bankruptcy Courts.

        Search for PACER cases filed in U.S. Bankruptcy Courts.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param federal_bankruptcy_chapter_array: The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11
        :type federal_bankruptcy_chapter_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).bankruptcy_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, federal_bankruptcy_chapter_array = federal_bankruptcy_chapter_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        federal_bankruptcy_chapter_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for Bankruptcy Courts.

        Search for PACER cases filed in U.S. Bankruptcy Courts.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param federal_bankruptcy_chapter_array: The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11
        :type federal_bankruptcy_chapter_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).bankruptcy_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, federal_bankruptcy_chapter_array = federal_bankruptcy_chapter_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        ssn_or_ein: Annotated[Optional[Annotated[str, Field(strict=True, max_length=9)]], Field(description="The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.")] = None,
        four_digit_ssn: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER bankruptcy filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param ssn_or_ein: The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.
        :type ssn_or_ein: str
        :param four_digit_ssn: The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.
        :type four_digit_ssn: str
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).bankruptcy_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, ssn_or_ein = ssn_or_ein, four_digit_ssn = four_digit_ssn, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        ssn_or_ein: Annotated[Optional[Annotated[str, Field(strict=True, max_length=9)]], Field(description="The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.")] = None,
        four_digit_ssn: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER bankruptcy filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param ssn_or_ein: The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.
        :type ssn_or_ein: str
        :param four_digit_ssn: The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.
        :type four_digit_ssn: str
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).bankruptcy_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, ssn_or_ein = ssn_or_ein, four_digit_ssn = four_digit_ssn, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        ssn_or_ein: Annotated[Optional[Annotated[str, Field(strict=True, max_length=9)]], Field(description="The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.")] = None,
        four_digit_ssn: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_discharged_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_discharged_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.")] = None,
        case_dismissed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER bankruptcy filings.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param ssn_or_ein: The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.
        :type ssn_or_ein: str
        :param four_digit_ssn: The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified.
        :type four_digit_ssn: str
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param case_discharged_start_date: The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_start_date: datetime
        :param case_discharged_end_date: The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_discharged_end_date: datetime
        :param case_dismissed_start_date: The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
        :type case_dismissed_start_date: datetime
        :param case_dismissed_end_date: The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_dismissed_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).bankruptcy_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, ssn_or_ein = ssn_or_ein, four_digit_ssn = four_digit_ssn, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, case_discharged_start_date = case_discharged_start_date, case_discharged_end_date = case_discharged_end_date, case_dismissed_start_date = case_dismissed_start_date, case_dismissed_end_date = case_dismissed_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def civil_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).civil_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def civil_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).civil_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def civil_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case.")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        nature_of_suits_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case.
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param nature_of_suits_array: The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140
        :type nature_of_suits_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).civil_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, nature_of_suits_array = nature_of_suits_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def civil_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The name suffix (e.g., III, MD).")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The name suffix (e.g., III, MD).
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).civil_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def civil_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The name suffix (e.g., III, MD).")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The name suffix (e.g., III, MD).
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).civil_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def civil_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The name suffix (e.g., III, MD).")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in civil cases filed in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The name suffix (e.g., III, MD).
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).civil_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def criminal_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for criminal cases in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).criminal_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def criminal_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for criminal cases in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).criminal_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def criminal_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for criminal cases in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).criminal_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def criminal_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER criminal cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).criminal_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def criminal_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER criminal cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).criminal_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def criminal_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in PACER criminal cases.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).criminal_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def import_pacer_case_by_court_using_case_number(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The PACER username of the PACER account under which the case should be imported.")],
        case_number: Annotated[str, Field(min_length=3, strict=True, max_length=50, description="The case number of the case to be imported.")],
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the court from which the case is to be imported.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
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
    ) -> SdkResponse[PACERImportCase]:

        """Find PACER Case for a requested Case Number and Court.

        Import the specified case from PACER.    Workflow:     1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.     2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.    Note:     1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.     2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

        :param pacer_user_id: The PACER username of the PACER account under which the case should be imported. (required)
        :type pacer_user_id: str
        :param case_number: The case number of the case to be imported. (required)
        :type case_number: str
        :param court_id: The courtId value of the court from which the case is to be imported. (required)
        :type court_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
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
            response = PACERApi(api_client).import_pacer_case_by_court_using_case_number_with_http_info(pacer_user_id = pacer_user_id, case_number = case_number, court_id = court_id, pacer_client_code = pacer_client_code, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def import_pacer_case_by_court_using_case_number_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The PACER username of the PACER account under which the case should be imported.")],
        case_number: Annotated[str, Field(min_length=3, strict=True, max_length=50, description="The case number of the case to be imported.")],
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the court from which the case is to be imported.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
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
    ) -> ApiResponse[PACERImportCase]:

        """Find PACER Case for a requested Case Number and Court.

        Import the specified case from PACER.    Workflow:     1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.     2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.    Note:     1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.     2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

        :param pacer_user_id: The PACER username of the PACER account under which the case should be imported. (required)
        :type pacer_user_id: str
        :param case_number: The case number of the case to be imported. (required)
        :type case_number: str
        :param court_id: The courtId value of the court from which the case is to be imported. (required)
        :type court_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
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
            return PACERApi(api_client).import_pacer_case_by_court_using_case_number_with_http_info(pacer_user_id = pacer_user_id, case_number = case_number, court_id = court_id, pacer_client_code = pacer_client_code, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def import_pacer_case_by_court_using_case_number_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The PACER username of the PACER account under which the case should be imported.")],
        case_number: Annotated[str, Field(min_length=3, strict=True, max_length=50, description="The case number of the case to be imported.")],
        court_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="The courtId value of the court from which the case is to be imported.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
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

        """Find PACER Case for a requested Case Number and Court.

        Import the specified case from PACER.    Workflow:     1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.     2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.    Note:     1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.     2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

        :param pacer_user_id: The PACER username of the PACER account under which the case should be imported. (required)
        :type pacer_user_id: str
        :param case_number: The case number of the case to be imported. (required)
        :type case_number: str
        :param court_id: The courtId value of the court from which the case is to be imported. (required)
        :type court_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
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
            response = PACERApi(api_client).import_pacer_case_by_court_using_case_number_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, case_number = case_number, court_id = court_id, pacer_client_code = pacer_client_code, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def multi_district_courts_pacer_case_locator_case_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).multi_district_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def multi_district_courts_pacer_case_locator_case_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLCase]:

        """PACER Case Locator Search API for All Courts.

        Search for multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).multi_district_courts_pacer_case_locator_case_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def multi_district_courts_pacer_case_locator_case_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).multi_district_courts_pacer_case_locator_case_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def multi_district_courts_pacer_case_locator_party_search(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> SdkResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).multi_district_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def multi_district_courts_pacer_case_locator_party_search_with_http_info(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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
    ) -> ApiResponse[PCLParty]:

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            return PACERApi(api_client).multi_district_courts_pacer_case_locator_party_search_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def multi_district_courts_pacer_case_locator_party_search_without_preload_content(
        pacer_user_id: Annotated[str, Field(min_length=6, strict=True, max_length=20, description="The username of the PACER account under which the search is to be performed.")],
        pacer_client_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]], Field(description="This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)")] = None,
        case_number: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(description="The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).")] = None,
        jpml_number: Annotated[Optional[StrictInt], Field(description="Master JPML Case Number.")] = None,
        pacer_case_id: Annotated[Optional[StrictInt], Field(description="The PACER-assigned identifier of the target case.")] = None,
        last_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The last name (for an individual) or the entity name (for a business entity) of the target party.")] = None,
        first_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The first name of the target party.")] = None,
        middle_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=40)]], Field(description="The middle name of the target party.")] = None,
        generation: Annotated[Optional[Annotated[str, Field(strict=True, max_length=5)]], Field(description="The suffix (e.g., Jr., III) of the target party's name.")] = None,
        party_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=50)]], Field(description="The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        party_exact_name_match: Annotated[Optional[StrictBool], Field(description="Specify whether the search string must match the name of the target party exactly.")] = None,
        party_role_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=50)]]]], Field(description="The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.")] = None,
        case_title: Annotated[Optional[Annotated[str, Field(strict=True, max_length=255)]], Field(description="The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.")] = None,
        case_office: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1)]], Field(description="The divisional office in which the case was filed.")] = None,
        case_sequence_number: Annotated[Optional[Annotated[int, Field(le=99999, strict=True, ge=0)]], Field(description="The PACER-assigned sequence number of the target case. Ex 12345")] = None,
        case_year: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="The two- or four-digit year in which the target case was filed.")] = None,
        case_type_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr")] = None,
        court_region_id_array: Annotated[Optional[List[Optional[Annotated[str, Field(strict=True, max_length=255)]]]], Field(description="The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae")] = None,
        case_year_from: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or later")] = None,
        case_year_to: Annotated[Optional[Annotated[int, Field(le=2100, strict=True, ge=0)]], Field(description="Limit the results of the search to those cases from the year specified or earlier")] = None,
        case_filed_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_filed_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_start_date: Annotated[Optional[datetime], Field(description="The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        case_terminated_end_date: Annotated[Optional[datetime], Field(description="The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).")] = None,
        sort_parameter_query: Annotated[Optional[Annotated[str, Field(min_length=5, strict=True, max_length=100)]], Field(description="How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC")] = None,
        case_status: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(description="Whether the target case is marked as 'open' or 'closed' within PACER.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page number of the search results to be retrieved.")] = None,
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

        """PACER Case Locator Search API for All Courts.

        Search for the specified party in multidistrict litigation in PACER.

        :param pacer_user_id: The username of the PACER account under which the search is to be performed. (required)
        :type pacer_user_id: str
        :param pacer_client_code: This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/)
        :type pacer_client_code: str
        :param case_number: The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit).
        :type case_number: str
        :param jpml_number: Master JPML Case Number.
        :type jpml_number: int
        :param pacer_case_id: The PACER-assigned identifier of the target case.
        :type pacer_case_id: int
        :param last_name: The last name (for an individual) or the entity name (for a business entity) of the target party.
        :type last_name: str
        :param first_name: The first name of the target party.
        :type first_name: str
        :param middle_name: The middle name of the target party.
        :type middle_name: str
        :param generation: The suffix (e.g., Jr., III) of the target party's name.
        :type generation: str
        :param party_type: The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_type: str
        :param party_exact_name_match: Specify whether the search string must match the name of the target party exactly.
        :type party_exact_name_match: bool
        :param party_role_array: The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
        :type party_role_array: List[Optional[str]]
        :param case_title: The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
        :type case_title: str
        :param case_office: The divisional office in which the case was filed.
        :type case_office: str
        :param case_sequence_number: The PACER-assigned sequence number of the target case. Ex 12345
        :type case_sequence_number: int
        :param case_year: The two- or four-digit year in which the target case was filed.
        :type case_year: int
        :param case_type_array: The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr
        :type case_type_array: List[Optional[str]]
        :param court_region_id_array: The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae
        :type court_region_id_array: List[Optional[str]]
        :param case_year_from: Limit the results of the search to those cases from the year specified or later
        :type case_year_from: int
        :param case_year_to: Limit the results of the search to those cases from the year specified or earlier
        :type case_year_to: int
        :param case_filed_start_date: The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_start_date: datetime
        :param case_filed_end_date: The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_filed_end_date: datetime
        :param case_terminated_start_date: The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_start_date: datetime
        :param case_terminated_end_date: The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
        :type case_terminated_end_date: datetime
        :param sort_parameter_query: How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC
        :type sort_parameter_query: str
        :param case_status: Whether the target case is marked as 'open' or 'closed' within PACER.
        :type case_status: str
        :param page_number: The page number of the search results to be retrieved.
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
            response = PACERApi(api_client).multi_district_courts_pacer_case_locator_party_search_without_preload_content_with_http_info(pacer_user_id = pacer_user_id, pacer_client_code = pacer_client_code, case_number = case_number, jpml_number = jpml_number, pacer_case_id = pacer_case_id, last_name = last_name, first_name = first_name, middle_name = middle_name, generation = generation, party_type = party_type, party_exact_name_match = party_exact_name_match, party_role_array = party_role_array, case_title = case_title, case_office = case_office, case_sequence_number = case_sequence_number, case_year = case_year, case_type_array = case_type_array, court_region_id_array = court_region_id_array, case_year_from = case_year_from, case_year_to = case_year_to, case_filed_start_date = case_filed_start_date, case_filed_end_date = case_filed_end_date, case_terminated_start_date = case_terminated_start_date, case_terminated_end_date = case_terminated_end_date, sort_parameter_query = sort_parameter_query, case_status = case_status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
