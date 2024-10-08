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
from typing import Optional, Set
from typing_extensions import Self

class SOSAssociatedNormOrganization(BaseModel):
    """
    SOSAssociatedNormOrganization
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=29)]] = 'SOSAssociatedNormOrganization'
    norm_organization_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="normOrganizationId")
    norm_organization_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="normOrganizationAPI")
    relationship_type: Optional[Annotated[str, Field(strict=True, max_length=6)]] = Field(default=None, alias="relationshipType")
    name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    from_date: Optional[datetime] = Field(default=None, alias="fromDate")
    to_date: Optional[datetime] = Field(default=None, alias="toDate")
    __properties: ClassVar[List[str]] = ["object", "normOrganizationId", "normOrganizationAPI", "relationshipType", "name", "fromDate", "toDate"]

    @field_validator('relationship_type')
    def relationship_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Parent', 'Child']):
            raise ValueError("must be one of enum values ('Parent', 'Child')")
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
        """Create an instance of SOSAssociatedNormOrganization from a JSON string"""
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
        # set to None if norm_organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.norm_organization_id is None and "norm_organization_id" in self.model_fields_set:
            _dict['normOrganizationId'] = None

        # set to None if norm_organization_api (nullable) is None
        # and model_fields_set contains the field
        if self.norm_organization_api is None and "norm_organization_api" in self.model_fields_set:
            _dict['normOrganizationAPI'] = None

        # set to None if to_date (nullable) is None
        # and model_fields_set contains the field
        if self.to_date is None and "to_date" in self.model_fields_set:
            _dict['toDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SOSAssociatedNormOrganization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'SOSAssociatedNormOrganization',
            "normOrganizationId": obj.get("normOrganizationId"),
            "normOrganizationAPI": obj.get("normOrganizationAPI"),
            "relationshipType": obj.get("relationshipType"),
            "name": obj.get("name"),
            "fromDate": obj.get("fromDate"),
            "toDate": obj.get("toDate")
        })
        return _obj


