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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PartyAttorneyAssociation(BaseModel):
    """
    PartyAttorneyAssociation
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=24, strict=True, max_length=24)]] = Field(default='PartyAttorneyAssociation', description="Name of the object")
    party_attorney_association_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="ID of the association", alias="partyAttorneyAssociationId")
    attorney_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.", alias="attorneyId")
    party_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.", alias="partyId")
    is_visible: Optional[StrictBool] = Field(default=None, description="Signifies if this party attorney relationship is currently isVisible or not for the case.", alias="isVisible")
    __properties: ClassVar[List[str]] = ["object", "partyAttorneyAssociationId", "attorneyId", "partyId", "isVisible"]

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
        """Create an instance of PartyAttorneyAssociation from a JSON string"""
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
        """Create an instance of PartyAttorneyAssociation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PartyAttorneyAssociation',
            "partyAttorneyAssociationId": obj.get("partyAttorneyAssociationId"),
            "attorneyId": obj.get("attorneyId"),
            "partyId": obj.get("partyId"),
            "isVisible": obj.get("isVisible")
        })
        return _obj


