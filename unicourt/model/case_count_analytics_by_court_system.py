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
from unicourt.model.case_count_analytics_by_court_geo import CaseCountAnalyticsByCourtGeo
from unicourt.model.court_system import CourtSystem
from typing import Optional, Set
from typing_extensions import Self

class CaseCountAnalyticsByCourtSystem(BaseModel):
    """
    CaseCountAnalyticsByCourtSystem
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=31)]] = 'CaseCountAnalyticsByCourtSystem'
    case_count: Optional[StrictInt] = Field(default=None, alias="caseCount")
    case_search_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="link to cases for this criteria.", alias="caseSearchAPI")
    court_system: Optional[CourtSystem] = Field(default=None, alias="courtSystem")
    geo: Optional[CaseCountAnalyticsByCourtGeo] = Field(default=None, alias="Geo")
    __properties: ClassVar[List[str]] = ["object", "caseCount", "caseSearchAPI", "courtSystem", "Geo"]

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
        """Create an instance of CaseCountAnalyticsByCourtSystem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of court_system
        if self.court_system:
            _dict['courtSystem'] = self.court_system.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo
        if self.geo:
            _dict['Geo'] = self.geo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CaseCountAnalyticsByCourtSystem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'CaseCountAnalyticsByCourtSystem',
            "caseCount": obj.get("caseCount"),
            "caseSearchAPI": obj.get("caseSearchAPI"),
            "courtSystem": CourtSystem.from_dict(obj["courtSystem"]) if obj.get("courtSystem") is not None else None,
            "Geo": CaseCountAnalyticsByCourtGeo.from_dict(obj["Geo"]) if obj.get("Geo") is not None else None
        })
        return _obj


