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
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.matched_object import MatchedObject
from typing import Optional, Set
from typing_extensions import Self

class NormAttorneySearchResult(BaseModel):
    """
    NormAttorneySearchResult
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=24, strict=True, max_length=24)]] = 'NormAttorneySearchResult'
    norm_attorney_id: Optional[Annotated[str, Field(min_length=17, strict=True, max_length=18)]] = Field(default=None, alias="normAttorneyId")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    first_fetch_date: Optional[datetime] = Field(default=None, alias="firstFetchDate")
    last_fetch_date: Optional[datetime] = Field(default=None, alias="lastFetchDate")
    has_associated_public_data: Optional[StrictBool] = Field(default=None, alias="hasAssociatedPublicData")
    norm_attorney_details_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="normAttorneyDetailsAPI")
    matched_object_array: Optional[List[MatchedObject]] = Field(default=None, alias="matchedObjectArray")
    __properties: ClassVar[List[str]] = ["object", "normAttorneyId", "name", "firstFetchDate", "lastFetchDate", "hasAssociatedPublicData", "normAttorneyDetailsAPI", "matchedObjectArray"]

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
        """Create an instance of NormAttorneySearchResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in matched_object_array (list)
        _items = []
        if self.matched_object_array:
            for _item in self.matched_object_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchedObjectArray'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormAttorneySearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'NormAttorneySearchResult',
            "normAttorneyId": obj.get("normAttorneyId"),
            "name": obj.get("name"),
            "firstFetchDate": obj.get("firstFetchDate"),
            "lastFetchDate": obj.get("lastFetchDate"),
            "hasAssociatedPublicData": obj.get("hasAssociatedPublicData"),
            "normAttorneyDetailsAPI": obj.get("normAttorneyDetailsAPI"),
            "matchedObjectArray": [MatchedObject.from_dict(_item) for _item in obj["matchedObjectArray"]] if obj.get("matchedObjectArray") is not None else None
        })
        return _obj


