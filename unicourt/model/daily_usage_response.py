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
from unicourt.model.billing_cycle_usage_response_api_calls_billable import BillingCycleUsageResponseApiCallsBillable
from unicourt.model.billing_cycle_usage_response_api_calls_credited import BillingCycleUsageResponseApiCallsCredited
from unicourt.model.billing_cycle_usage_response_api_calls_made import BillingCycleUsageResponseApiCallsMade
from typing import Optional, Set
from typing_extensions import Self

class DailyUsageResponse(BaseModel):
    """
    DailyUsageResponse
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default='DailyUsageResponse', description="Name of the object.")
    usage_start_time: Optional[datetime] = Field(default=None, description="Start time of the usage.", alias="usageStartTime")
    usage_end_time: Optional[datetime] = Field(default=None, description="End time of the usage.", alias="usageEndTime")
    api_usage: Optional[Dict[str, Any]] = Field(default=None, description="Api Usage made in real time.", alias="apiUsage")
    api_calls_made: Optional[BillingCycleUsageResponseApiCallsMade] = Field(default=None, alias="apiCallsMade")
    api_calls_credited: Optional[BillingCycleUsageResponseApiCallsCredited] = Field(default=None, alias="apiCallsCredited")
    api_calls_billable: Optional[BillingCycleUsageResponseApiCallsBillable] = Field(default=None, alias="apiCallsBillable")
    __properties: ClassVar[List[str]] = ["object", "usageStartTime", "usageEndTime", "apiUsage", "apiCallsMade", "apiCallsCredited", "apiCallsBillable"]

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
        """Create an instance of DailyUsageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of api_calls_made
        if self.api_calls_made:
            _dict['apiCallsMade'] = self.api_calls_made.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_calls_credited
        if self.api_calls_credited:
            _dict['apiCallsCredited'] = self.api_calls_credited.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_calls_billable
        if self.api_calls_billable:
            _dict['apiCallsBillable'] = self.api_calls_billable.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DailyUsageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'DailyUsageResponse',
            "usageStartTime": obj.get("usageStartTime"),
            "usageEndTime": obj.get("usageEndTime"),
            "apiUsage": obj.get("apiUsage"),
            "apiCallsMade": BillingCycleUsageResponseApiCallsMade.from_dict(obj["apiCallsMade"]) if obj.get("apiCallsMade") is not None else None,
            "apiCallsCredited": BillingCycleUsageResponseApiCallsCredited.from_dict(obj["apiCallsCredited"]) if obj.get("apiCallsCredited") is not None else None,
            "apiCallsBillable": BillingCycleUsageResponseApiCallsBillable.from_dict(obj["apiCallsBillable"]) if obj.get("apiCallsBillable") is not None else None
        })
        return _obj


