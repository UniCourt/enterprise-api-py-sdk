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
from typing import Optional, Set
from typing_extensions import Self

class NormJudgePublicDataEducationArrayInner(BaseModel):
    """
    NormJudgePublicDataEducationArrayInner
    """ # noqa: E501
    degree: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="The Degree Awarded to the Judge")
    year: Optional[StrictInt] = Field(default=None, description="The year when the degree was awarded.")
    school: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="The University which awarded the degree to the Judge.")
    __properties: ClassVar[List[str]] = ["degree", "year", "school"]

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
        """Create an instance of NormJudgePublicDataEducationArrayInner from a JSON string"""
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
        # set to None if degree (nullable) is None
        # and model_fields_set contains the field
        if self.degree is None and "degree" in self.model_fields_set:
            _dict['degree'] = None

        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        # set to None if school (nullable) is None
        # and model_fields_set contains the field
        if self.school is None and "school" in self.model_fields_set:
            _dict['school'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormJudgePublicDataEducationArrayInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "degree": obj.get("degree"),
            "year": obj.get("year"),
            "school": obj.get("school")
        })
        return _obj


