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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.nature_of_suit import NatureOfSuit
from unicourt.model.source_cause_of_action import SourceCauseOfAction
from unicourt.model.source_charge import SourceCharge
from unicourt.model.source_page_data import SourcePageData
from typing import Optional, Set
from typing_extensions import Self

class SourceCaseData(BaseModel):
    """
    Source data in the court website.
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=14, strict=True, max_length=14)]] = Field(default='SourceCaseData', description="Name of the object")
    source_court: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Courtrhouse as provided by Court.", alias="sourceCourt")
    source_case_type: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Case Type for a case which is provided by the Court.", alias="sourceCaseType")
    source_charge_array: Optional[List[SourceCharge]] = Field(default=None, description="Array of Charges for a case which is provided by the Court.", alias="sourceChargeArray")
    nature_of_suit_array: Optional[List[NatureOfSuit]] = Field(default=None, description="Array of Charges for a case which is provided by the Court.", alias="natureOfSuitArray")
    source_cause_of_action_array: Optional[List[SourceCauseOfAction]] = Field(default=None, description="Array of Cause Of Action for a case which is provided by the Court.", alias="sourceCauseOfActionArray")
    source_case_status: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Case Status as provided by Court.", alias="sourceCaseStatus")
    source_page_data: Optional[List[SourcePageData]] = Field(default=None, alias="sourcePageData")
    __properties: ClassVar[List[str]] = ["object", "sourceCourt", "sourceCaseType", "sourceChargeArray", "natureOfSuitArray", "sourceCauseOfActionArray", "sourceCaseStatus", "sourcePageData"]

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
        """Create an instance of SourceCaseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in source_charge_array (list)
        _items = []
        if self.source_charge_array:
            for _item in self.source_charge_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sourceChargeArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nature_of_suit_array (list)
        _items = []
        if self.nature_of_suit_array:
            for _item in self.nature_of_suit_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['natureOfSuitArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in source_cause_of_action_array (list)
        _items = []
        if self.source_cause_of_action_array:
            for _item in self.source_cause_of_action_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sourceCauseOfActionArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in source_page_data (list)
        _items = []
        if self.source_page_data:
            for _item in self.source_page_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sourcePageData'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceCaseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'SourceCaseData',
            "sourceCourt": obj.get("sourceCourt"),
            "sourceCaseType": obj.get("sourceCaseType"),
            "sourceChargeArray": [SourceCharge.from_dict(_item) for _item in obj["sourceChargeArray"]] if obj.get("sourceChargeArray") is not None else None,
            "natureOfSuitArray": [NatureOfSuit.from_dict(_item) for _item in obj["natureOfSuitArray"]] if obj.get("natureOfSuitArray") is not None else None,
            "sourceCauseOfActionArray": [SourceCauseOfAction.from_dict(_item) for _item in obj["sourceCauseOfActionArray"]] if obj.get("sourceCauseOfActionArray") is not None else None,
            "sourceCaseStatus": obj.get("sourceCaseStatus"),
            "sourcePageData": [SourcePageData.from_dict(_item) for _item in obj["sourcePageData"]] if obj.get("sourcePageData") is not None else None
        })
        return _obj


