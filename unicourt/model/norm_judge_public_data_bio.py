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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class NormJudgePublicDataBio(BaseModel):
    """
    NormJudgePublicDataBio
    """ # noqa: E501
    ethnicity: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Ethnic Group of the Judge.")
    birth_city: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The Birth City of the Judge.", alias="birthCity")
    birth_date: Optional[datetime] = Field(default=None, description="The Date of Birth of the Judge.", alias="birthDate")
    birth_state: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The Birth State of the Judge.", alias="birthState")
    death_city: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The Death City of the Judge.", alias="deathCity")
    death_date: Optional[datetime] = Field(default=None, description="The Date of the Death of the Judge.", alias="deathDate")
    death_state: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The Death State of the Judge.", alias="deathState")
    political_affiliation: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The Political Affiliation of the Judge.", alias="politicalAffiliation")
    __properties: ClassVar[List[str]] = ["ethnicity", "birthCity", "birthDate", "birthState", "deathCity", "deathDate", "deathState", "politicalAffiliation"]

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
        """Create an instance of NormJudgePublicDataBio from a JSON string"""
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
        # set to None if ethnicity (nullable) is None
        # and model_fields_set contains the field
        if self.ethnicity is None and "ethnicity" in self.model_fields_set:
            _dict['ethnicity'] = None

        # set to None if birth_city (nullable) is None
        # and model_fields_set contains the field
        if self.birth_city is None and "birth_city" in self.model_fields_set:
            _dict['birthCity'] = None

        # set to None if birth_date (nullable) is None
        # and model_fields_set contains the field
        if self.birth_date is None and "birth_date" in self.model_fields_set:
            _dict['birthDate'] = None

        # set to None if birth_state (nullable) is None
        # and model_fields_set contains the field
        if self.birth_state is None and "birth_state" in self.model_fields_set:
            _dict['birthState'] = None

        # set to None if death_city (nullable) is None
        # and model_fields_set contains the field
        if self.death_city is None and "death_city" in self.model_fields_set:
            _dict['deathCity'] = None

        # set to None if death_date (nullable) is None
        # and model_fields_set contains the field
        if self.death_date is None and "death_date" in self.model_fields_set:
            _dict['deathDate'] = None

        # set to None if death_state (nullable) is None
        # and model_fields_set contains the field
        if self.death_state is None and "death_state" in self.model_fields_set:
            _dict['deathState'] = None

        # set to None if political_affiliation (nullable) is None
        # and model_fields_set contains the field
        if self.political_affiliation is None and "political_affiliation" in self.model_fields_set:
            _dict['politicalAffiliation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormJudgePublicDataBio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ethnicity": obj.get("ethnicity"),
            "birthCity": obj.get("birthCity"),
            "birthDate": obj.get("birthDate"),
            "birthState": obj.get("birthState"),
            "deathCity": obj.get("deathCity"),
            "deathDate": obj.get("deathDate"),
            "deathState": obj.get("deathState"),
            "politicalAffiliation": obj.get("politicalAffiliation")
        })
        return _obj


