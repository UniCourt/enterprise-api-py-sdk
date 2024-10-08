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

class JurisdictionGeo(BaseModel):
    """
    JurisdictionGeo
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=15, strict=True, max_length=15)]] = 'JurisdictionGeo'
    jurisdiction_geo_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="jurisdictionGeoId")
    country: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    state: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    county: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    city: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    fips_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="fipsCode")
    zip_code_array: Optional[List[Annotated[str, Field(min_length=1, strict=True, max_length=255)]]] = Field(default=None, alias="zipCodeArray")
    created_date: Optional[datetime] = Field(default=None, description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.", alias="createdDate")
    courts_for_jurisdiction_geo_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="courtsForJurisdictionGeoAPI")
    __properties: ClassVar[List[str]] = ["object", "jurisdictionGeoId", "country", "state", "county", "city", "fipsCode", "zipCodeArray", "createdDate", "courtsForJurisdictionGeoAPI"]

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
        """Create an instance of JurisdictionGeo from a JSON string"""
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
        # set to None if county (nullable) is None
        # and model_fields_set contains the field
        if self.county is None and "county" in self.model_fields_set:
            _dict['county'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JurisdictionGeo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'JurisdictionGeo',
            "jurisdictionGeoId": obj.get("jurisdictionGeoId"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "county": obj.get("county"),
            "city": obj.get("city"),
            "fipsCode": obj.get("fipsCode"),
            "zipCodeArray": obj.get("zipCodeArray"),
            "createdDate": obj.get("createdDate"),
            "courtsForJurisdictionGeoAPI": obj.get("courtsForJurisdictionGeoAPI")
        })
        return _obj


