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
from unicourt.model.bar_record_preview import BarRecordPreview
from unicourt.model.case_timeline import CaseTimeline
from typing import Optional, Set
from typing_extensions import Self

class AssociatedNormAttorney(BaseModel):
    """
    AssociatedNormAttorney
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=22)]] = 'AssociatedNormAttorney'
    norm_attorney_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Link to details for the Attorney.", alias="normAttorneyAPI")
    norm_attorney_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="normAttorneyId")
    case_timeline: Optional[CaseTimeline] = Field(default=None, alias="caseTimeline")
    name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    first_name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="firstName")
    middle_name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="middleName")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="lastName")
    case_search_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Link to related cases for this association.", alias="caseSearchAPI")
    case_count: Optional[StrictInt] = Field(default=None, alias="caseCount")
    state_bar_data_array: Optional[List[BarRecordPreview]] = Field(default=None, alias="stateBarDataArray")
    __properties: ClassVar[List[str]] = ["object", "normAttorneyAPI", "normAttorneyId", "caseTimeline", "name", "firstName", "middleName", "lastName", "caseSearchAPI", "caseCount", "stateBarDataArray"]

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
        """Create an instance of AssociatedNormAttorney from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of case_timeline
        if self.case_timeline:
            _dict['caseTimeline'] = self.case_timeline.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in state_bar_data_array (list)
        _items = []
        if self.state_bar_data_array:
            for _item in self.state_bar_data_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stateBarDataArray'] = _items
        # set to None if middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.middle_name is None and "middle_name" in self.model_fields_set:
            _dict['middleName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssociatedNormAttorney from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'AssociatedNormAttorney',
            "normAttorneyAPI": obj.get("normAttorneyAPI"),
            "normAttorneyId": obj.get("normAttorneyId"),
            "caseTimeline": CaseTimeline.from_dict(obj["caseTimeline"]) if obj.get("caseTimeline") is not None else None,
            "name": obj.get("name"),
            "firstName": obj.get("firstName"),
            "middleName": obj.get("middleName"),
            "lastName": obj.get("lastName"),
            "caseSearchAPI": obj.get("caseSearchAPI"),
            "caseCount": obj.get("caseCount"),
            "stateBarDataArray": [BarRecordPreview.from_dict(_item) for _item in obj["stateBarDataArray"]] if obj.get("stateBarDataArray") is not None else None
        })
        return _obj


