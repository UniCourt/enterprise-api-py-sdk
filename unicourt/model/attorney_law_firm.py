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

class AttorneyLawFirm(BaseModel):
    """
    Name of the attorney's law firm as provided by Court. This can be null as some Courts do not provide this as a separate field.
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=15, strict=True, max_length=15)]] = Field(default='AttorneyLawFirm', description="Name of the object")
    attorney_law_firm_id: Optional[Annotated[str, Field(min_length=17, strict=True, max_length=18)]] = Field(default=None, description="ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.", alias="attorneyLawFirmId")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=250)]] = Field(default=None, description="Name of the law firm as provided by Court.")
    is_visible: Optional[StrictBool] = Field(default=None, description="Signifies if the attorney as this attorney type is currently isVisible or not for the case.", alias="isVisible")
    first_fetch_date: Optional[Annotated[str, Field(min_length=25, strict=True, max_length=25)]] = Field(default=None, description="Is the date when the document was first fetched from the court site.", alias="firstFetchDate")
    last_fetch_date: Optional[Annotated[str, Field(min_length=25, strict=True, max_length=25)]] = Field(default=None, description="Is the date when the document was last fetched from the court site.", alias="lastFetchDate")
    __properties: ClassVar[List[str]] = ["object", "attorneyLawFirmId", "name", "isVisible", "firstFetchDate", "lastFetchDate"]

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
        """Create an instance of AttorneyLawFirm from a JSON string"""
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
        # set to None if attorney_law_firm_id (nullable) is None
        # and model_fields_set contains the field
        if self.attorney_law_firm_id is None and "attorney_law_firm_id" in self.model_fields_set:
            _dict['attorneyLawFirmId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AttorneyLawFirm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'AttorneyLawFirm',
            "attorneyLawFirmId": obj.get("attorneyLawFirmId"),
            "name": obj.get("name"),
            "isVisible": obj.get("isVisible"),
            "firstFetchDate": obj.get("firstFetchDate"),
            "lastFetchDate": obj.get("lastFetchDate")
        })
        return _obj


