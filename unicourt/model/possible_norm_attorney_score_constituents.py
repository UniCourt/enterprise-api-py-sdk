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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PossibleNormAttorneyScoreConstituents(BaseModel):
    """
    PossibleNormAttorneyScoreConstituents
    """ # noqa: E501
    name_similarity_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nameSimilarityScore")
    other_potential_norm_attorneys: Optional[StrictInt] = Field(default=None, alias="otherPotentialNormAttorneys")
    bar_id: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, alias="barId")
    address: Optional[Annotated[str, Field(strict=True, max_length=250)]] = None
    email: Optional[Annotated[str, Field(strict=True, max_length=250)]] = None
    phone: Optional[Annotated[str, Field(strict=True, max_length=250)]] = None
    law_firm: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, alias="lawFirm")
    __properties: ClassVar[List[str]] = ["nameSimilarityScore", "otherPotentialNormAttorneys", "barId", "address", "email", "phone", "lawFirm"]

    @field_validator('bar_id')
    def bar_id_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Matched', 'Mismatched', 'Not_Provided_By_Data_Source']):
            raise ValueError("must be one of enum values ('Matched', 'Mismatched', 'Not_Provided_By_Data_Source')")
        return value

    @field_validator('address')
    def address_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Matched', 'Mismatched', 'Not_Provided_By_Data_Source']):
            raise ValueError("must be one of enum values ('Matched', 'Mismatched', 'Not_Provided_By_Data_Source')")
        return value

    @field_validator('email')
    def email_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Matched', 'Mismatched', 'Not_Provided_By_Data_Source']):
            raise ValueError("must be one of enum values ('Matched', 'Mismatched', 'Not_Provided_By_Data_Source')")
        return value

    @field_validator('phone')
    def phone_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Matched', 'Mismatched', 'Not_Provided_By_Data_Source']):
            raise ValueError("must be one of enum values ('Matched', 'Mismatched', 'Not_Provided_By_Data_Source')")
        return value

    @field_validator('law_firm')
    def law_firm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Matched', 'Mismatched', 'Not_Provided_By_Data_Source']):
            raise ValueError("must be one of enum values ('Matched', 'Mismatched', 'Not_Provided_By_Data_Source')")
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
        """Create an instance of PossibleNormAttorneyScoreConstituents from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PossibleNormAttorneyScoreConstituents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nameSimilarityScore": obj.get("nameSimilarityScore"),
            "otherPotentialNormAttorneys": obj.get("otherPotentialNormAttorneys"),
            "barId": obj.get("barId"),
            "address": obj.get("address"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "lawFirm": obj.get("lawFirm")
        })
        return _obj


