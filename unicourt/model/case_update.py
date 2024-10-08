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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.case import Case
from unicourt.model.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from unicourt.model.exception import Exception
from typing import Optional, Set
from typing_extensions import Self

class CaseUpdate(BaseModel):
    """
    CaseUpdate
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=10, strict=True, max_length=10)]] = Field(default='CaseUpdate', description="Name of the object.")
    case_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="Unique Id for a Case in UniCourt.", alias="caseId")
    status: Optional[Annotated[str, Field(min_length=7, strict=True, max_length=11)]] = Field(default=None, description="Status of the request.")
    requested_date: Optional[datetime] = Field(default=None, description="The date and time when the case was last requested for update ", alias="requestedDate")
    case_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="caseAPI")
    pacer_options: Optional[CaseUpdatePacerOptionsResponse] = Field(default=None, alias="pacerOptions")
    exception: Optional[Exception] = None
    case: Optional[Case] = None
    __properties: ClassVar[List[str]] = ["object", "caseId", "status", "requestedDate", "caseAPI", "pacerOptions", "exception", "case"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COMPLETE', 'FAILURE', 'IN_PROGRESS', 'DELAYED']):
            raise ValueError("must be one of enum values ('COMPLETE', 'FAILURE', 'IN_PROGRESS', 'DELAYED')")
        return value

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
        """Create an instance of CaseUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pacer_options
        if self.pacer_options:
            _dict['pacerOptions'] = self.pacer_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exception
        if self.exception:
            _dict['exception'] = self.exception.to_dict()
        # override the default output from pydantic by calling `to_dict()` of case
        if self.case:
            _dict['case'] = self.case.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CaseUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'CaseUpdate',
            "caseId": obj.get("caseId"),
            "status": obj.get("status"),
            "requestedDate": obj.get("requestedDate"),
            "caseAPI": obj.get("caseAPI"),
            "pacerOptions": CaseUpdatePacerOptionsResponse.from_dict(obj["pacerOptions"]) if obj.get("pacerOptions") is not None else None,
            "exception": Exception.from_dict(obj["exception"]) if obj.get("exception") is not None else None,
            "case": Case.from_dict(obj["case"]) if obj.get("case") is not None else None
        })
        return _obj


