# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.case_document import CaseDocument
from typing import Optional, Set
from typing_extensions import Self

class DocketEntryPrimaryDocuments(BaseModel):
    """
    Primary Documents refers to documents that are directly related to a docket entry. Primary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the primary document is one which is attached to the docket number. Because in district for a primary document it can have many attachments associatated to it. PACER Appeal Courts - Here the attachments for a docket entry are the primary documents. Because in appeal for those attachments there is no primary documents.
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=27, strict=True, max_length=27)]] = Field(default='DocketEntryPrimaryDocuments', description="Name of the object")
    page_number: Optional[StrictInt] = Field(default=None, description="Page number for which results where obtained.", alias="pageNumber")
    case_document_array: Optional[Annotated[List[CaseDocument], Field(max_length=100)]] = Field(default=None, alias="caseDocumentArray")
    next_page_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Link to next page of a particular entity in a Case.", alias="nextPageAPI")
    total_pages: Optional[StrictInt] = Field(default=None, description="Total number of pages to obtain all the objects of a party in the Case.", alias="totalPages")
    total_count: Optional[StrictInt] = Field(default=None, description="Total number of parties of the Case. entity in a Case.", alias="totalCount")
    __properties: ClassVar[List[str]] = ["object", "pageNumber", "caseDocumentArray", "nextPageAPI", "totalPages", "totalCount"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DocketEntryPrimaryDocuments from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in case_document_array (list)
        _items = []
        if self.case_document_array:
            for _item in self.case_document_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['caseDocumentArray'] = _items
        # set to None if next_page_api (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_api is None and "next_page_api" in self.model_fields_set:
            _dict['nextPageAPI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocketEntryPrimaryDocuments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'DocketEntryPrimaryDocuments',
            "pageNumber": obj.get("pageNumber"),
            "caseDocumentArray": [CaseDocument.from_dict(_item) for _item in obj["caseDocumentArray"]] if obj.get("caseDocumentArray") is not None else None,
            "nextPageAPI": obj.get("nextPageAPI"),
            "totalPages": obj.get("totalPages"),
            "totalCount": obj.get("totalCount")
        })
        return _obj


