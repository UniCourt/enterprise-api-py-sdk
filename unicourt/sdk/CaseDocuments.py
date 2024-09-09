import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, field_validator
from typing import Optional
from typing_extensions import Annotated
from unicourt.model.case_document import CaseDocument
from unicourt.model.case_document_order_callback import CaseDocumentOrderCallback
from unicourt.model.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse
from unicourt.model.case_document_order_request import CaseDocumentOrderRequest
from unicourt.model.case_documents import CaseDocuments
from unicourt.model.document_download import DocumentDownload
from unicourt.api_client import ApiClient, RequestSerialized
from unicourt.api_response import ApiResponse
from unicourt.rest import RESTResponseType
from unicourt.api.case_documents_api import CaseDocumentsApi
from unicourt.sdk_response import SdkResponse
from unicourt import utils
class CaseDocuments:

    @staticmethod
    def get_case_document_download_by_id(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Document ID which you want to download.")],
        is_preview_document: Annotated[Optional[StrictBool], Field(description="If the document you want to download is a preview of a document.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[DocumentDownload]:

        """Gets downloadable URL for a requested Document ID.

        Gets downloadable URL for a requested Document ID.

        :param case_document_id: Document ID which you want to download. (required)
        :type case_document_id: str
        :param is_preview_document: If the document you want to download is a preview of a document.
        :type is_preview_document: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_case_document_download_by_id_with_http_info(case_document_id = case_document_id, is_preview_document = is_preview_document, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_document_download_by_id_with_http_info(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Document ID which you want to download.")],
        is_preview_document: Annotated[Optional[StrictBool], Field(description="If the document you want to download is a preview of a document.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[DocumentDownload]:

        """Gets downloadable URL for a requested Document ID.

        Gets downloadable URL for a requested Document ID.

        :param case_document_id: Document ID which you want to download. (required)
        :type case_document_id: str
        :param is_preview_document: If the document you want to download is a preview of a document.
        :type is_preview_document: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_document_download_by_id_with_http_info(case_document_id = case_document_id, is_preview_document = is_preview_document, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_document_download_by_id_without_preload_content(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Document ID which you want to download.")],
        is_preview_document: Annotated[Optional[StrictBool], Field(description="If the document you want to download is a preview of a document.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Gets downloadable URL for a requested Document ID.

        Gets downloadable URL for a requested Document ID.

        :param case_document_id: Document ID which you want to download. (required)
        :type case_document_id: str
        :param is_preview_document: If the document you want to download is a preview of a document.
        :type is_preview_document: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_case_document_download_by_id_without_preload_content_with_http_info(case_document_id = case_document_id, is_preview_document = is_preview_document, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_document_order_callback_by_id(
        case_document_order_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Unique Id for the Case Document Order Callback.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseDocumentOrderCallback]:

        """Get Case Document Order Callback for a requested Case Document Order Callback Id.

        Get Case Document Order Callback for a requested Case Document Order Callback Id.

        :param case_document_order_callback_id: Unique Id for the Case Document Order Callback. (required)
        :type case_document_order_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_case_document_order_callback_by_id_with_http_info(case_document_order_callback_id = case_document_order_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_document_order_callback_by_id_with_http_info(
        case_document_order_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Unique Id for the Case Document Order Callback.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseDocumentOrderCallback]:

        """Get Case Document Order Callback for a requested Case Document Order Callback Id.

        Get Case Document Order Callback for a requested Case Document Order Callback Id.

        :param case_document_order_callback_id: Unique Id for the Case Document Order Callback. (required)
        :type case_document_order_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_case_document_order_callback_by_id_with_http_info(case_document_order_callback_id = case_document_order_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_document_order_callback_by_id_without_preload_content(
        case_document_order_callback_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Unique Id for the Case Document Order Callback.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Get Case Document Order Callback for a requested Case Document Order Callback Id.

        Get Case Document Order Callback for a requested Case Document Order Callback Id.

        :param case_document_order_callback_id: Unique Id for the Case Document Order Callback. (required)
        :type case_document_order_callback_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_case_document_order_callback_by_id_without_preload_content_with_http_info(case_document_order_callback_id = case_document_order_callback_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_document_order_callbacks(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of Document Order callbacks. Default status will fetch all callbacks.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseDocumentOrderCallbackListResponse]:

        """Get Case Document Order Callback list for a requested Date.

        Get Case Document Order Callback list for a requested Date.

        :param date: Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of Document Order callbacks. Default status will fetch all callbacks.
        :type status: str
        :param page_number: Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 
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
            response = CaseDocumentsApi(api_client).get_case_document_order_callbacks_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_document_order_callbacks_with_http_info(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of Document Order callbacks. Default status will fetch all callbacks.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseDocumentOrderCallbackListResponse]:

        """Get Case Document Order Callback list for a requested Date.

        Get Case Document Order Callback list for a requested Date.

        :param date: Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of Document Order callbacks. Default status will fetch all callbacks.
        :type status: str
        :param page_number: Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 
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
            return CaseDocumentsApi(api_client).get_case_document_order_callbacks_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_document_order_callbacks_without_preload_content(
        date: Annotated[Optional[datetime], Field(description="Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.")] = None,
        status: Annotated[Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]], Field(description="Status of Document Order callbacks. Default status will fetch all callbacks.")] = None,
        page_number: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Get Case Document Order Callback list for a requested Date.

        Get Case Document Order Callback list for a requested Date.

        :param date: Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.
        :type date: datetime
        :param status: Status of Document Order callbacks. Default status will fetch all callbacks.
        :type status: str
        :param page_number: Page to fetch the Case Document Order Callback list.<br>   - Minimum: 1 
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
            response = CaseDocumentsApi(api_client).get_case_document_order_callbacks_without_preload_content_with_http_info(date = date, status = status, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_documents(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Case ID for which you want the data for.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Filter all the documents those are added to the UniCourt library.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Get all the documents which were added to the case on or after a specific date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date when the document was added to the UniCourt Library.")] = None,
        first_fetch_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date it was fetched from the source site.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort documents with document order.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page for which the result should be retrieved.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseDocuments]:

        """Gets Documents for a requested Case ID.

        Gets Documents for a requested Case ID.

        :param case_id: Case ID for which you want the data for. (required)
        :type case_id: str
        :param in_library: Filter all the documents those are added to the UniCourt library.
        :type in_library: bool
        :param after_first_fetch_date: Get all the documents which were added to the case on or after a specific date.
        :type after_first_fetch_date: datetime
        :param library_date: Sort all the documents based on the date when the document was added to the UniCourt Library.
        :type library_date: datetime
        :param first_fetch_date: Sort all the documents based on the date it was fetched from the source site.
        :type first_fetch_date: datetime
        :param sort_by: Sort documents with document order.
        :type sort_by: str
        :param page_number: The page for which the result should be retrieved.
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
            response = CaseDocumentsApi(api_client).get_case_documents_with_http_info(case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, first_fetch_date = first_fetch_date, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_case_documents_with_http_info(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Case ID for which you want the data for.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Filter all the documents those are added to the UniCourt library.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Get all the documents which were added to the case on or after a specific date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date when the document was added to the UniCourt Library.")] = None,
        first_fetch_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date it was fetched from the source site.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort documents with document order.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page for which the result should be retrieved.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseDocuments]:

        """Gets Documents for a requested Case ID.

        Gets Documents for a requested Case ID.

        :param case_id: Case ID for which you want the data for. (required)
        :type case_id: str
        :param in_library: Filter all the documents those are added to the UniCourt library.
        :type in_library: bool
        :param after_first_fetch_date: Get all the documents which were added to the case on or after a specific date.
        :type after_first_fetch_date: datetime
        :param library_date: Sort all the documents based on the date when the document was added to the UniCourt Library.
        :type library_date: datetime
        :param first_fetch_date: Sort all the documents based on the date it was fetched from the source site.
        :type first_fetch_date: datetime
        :param sort_by: Sort documents with document order.
        :type sort_by: str
        :param page_number: The page for which the result should be retrieved.
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
            return CaseDocumentsApi(api_client).get_case_documents_with_http_info(case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, first_fetch_date = first_fetch_date, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_case_documents_without_preload_content(
        case_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Case ID for which you want the data for.")],
        in_library: Annotated[Optional[StrictBool], Field(description="Filter all the documents those are added to the UniCourt library.")] = None,
        after_first_fetch_date: Annotated[Optional[datetime], Field(description="Get all the documents which were added to the case on or after a specific date.")] = None,
        library_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date when the document was added to the UniCourt Library.")] = None,
        first_fetch_date: Annotated[Optional[datetime], Field(description="Sort all the documents based on the date it was fetched from the source site.")] = None,
        sort_by: Annotated[Optional[Annotated[str, Field(min_length=10, strict=True, max_length=20)]], Field(description="Sort documents with document order.")] = None,
        page_number: Annotated[Optional[StrictInt], Field(description="The page for which the result should be retrieved.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Gets Documents for a requested Case ID.

        Gets Documents for a requested Case ID.

        :param case_id: Case ID for which you want the data for. (required)
        :type case_id: str
        :param in_library: Filter all the documents those are added to the UniCourt library.
        :type in_library: bool
        :param after_first_fetch_date: Get all the documents which were added to the case on or after a specific date.
        :type after_first_fetch_date: datetime
        :param library_date: Sort all the documents based on the date when the document was added to the UniCourt Library.
        :type library_date: datetime
        :param first_fetch_date: Sort all the documents based on the date it was fetched from the source site.
        :type first_fetch_date: datetime
        :param sort_by: Sort documents with document order.
        :type sort_by: str
        :param page_number: The page for which the result should be retrieved.
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
            response = CaseDocumentsApi(api_client).get_case_documents_without_preload_content_with_http_info(case_id = case_id, in_library = in_library, after_first_fetch_date = after_first_fetch_date, library_date = library_date, first_fetch_date = first_fetch_date, sort_by = sort_by, page_number = page_number, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_document_by_id(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Specific Case Dcoument ID for which you want the data for.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseDocument]:

        """Gets details for a requested Document ID.

        Gets details for a requested Document ID.

        :param case_document_id: Specific Case Dcoument ID for which you want the data for. (required)
        :type case_document_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_document_by_id_with_http_info(case_document_id = case_document_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def get_document_by_id_with_http_info(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Specific Case Dcoument ID for which you want the data for.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseDocument]:

        """Gets details for a requested Document ID.

        Gets details for a requested Document ID.

        :param case_document_id: Specific Case Dcoument ID for which you want the data for. (required)
        :type case_document_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).get_document_by_id_with_http_info(case_document_id = case_document_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def get_document_by_id_without_preload_content(
        case_document_id: Annotated[str, Field(min_length=18, strict=True, max_length=18, description="Specific Case Dcoument ID for which you want the data for.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Gets details for a requested Document ID.

        Gets details for a requested Document ID.

        :param case_document_id: Specific Case Dcoument ID for which you want the data for. (required)
        :type case_document_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).get_document_by_id_without_preload_content_with_http_info(case_document_id = case_document_id, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def order_case_document(
        case_document_order_request: Annotated[Optional[CaseDocumentOrderRequest], Field(description="If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SdkResponse[CaseDocumentOrderCallback]:

        """Add Case Document Order for requested Document Ids.

        Add Case Document Order for requested Document Ids. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Document Order request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseDocumentOrder\">  WebSocket Callbacks Documentation </a>

        :param case_document_order_request: If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. 
        :type case_document_order_request: CaseDocumentOrderRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).order_case_document_with_http_info(case_document_order_request = case_document_order_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)

    @staticmethod
    def order_case_document_with_http_info(
        case_document_order_request: Annotated[Optional[CaseDocumentOrderRequest], Field(description="If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CaseDocumentOrderCallback]:

        """Add Case Document Order for requested Document Ids.

        Add Case Document Order for requested Document Ids. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Document Order request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseDocumentOrder\">  WebSocket Callbacks Documentation </a>

        :param case_document_order_request: If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. 
        :type case_document_order_request: CaseDocumentOrderRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            return CaseDocumentsApi(api_client).order_case_document_with_http_info(case_document_order_request = case_document_order_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)

    @staticmethod
    def order_case_document_without_preload_content(
        case_document_order_request: Annotated[Optional[CaseDocumentOrderRequest], Field(description="If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
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

        """Add Case Document Order for requested Document Ids.

        Add Case Document Order for requested Document Ids. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Document Order request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/UniCourt-Enterprise-Callback-Async-API-Spec/#caseDocumentOrder\">  WebSocket Callbacks Documentation </a>

        :param case_document_order_request: If the Case Document Order is for Preview, then the value for ``isPreviewOnly`` should be ``true`` else ``false``. 
        :type case_document_order_request: CaseDocumentOrderRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        with utils.api_client() as api_client:
            response = CaseDocumentsApi(api_client).order_case_document_without_preload_content_with_http_info(case_document_order_request = case_document_order_request, _request_timeout = _request_timeout, _request_auth = _request_auth, _content_type = _content_type, _headers = _headers, _host_index = _host_index)
            return (response.data, response.status_code)
