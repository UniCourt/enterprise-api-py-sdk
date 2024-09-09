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
from unicourt.model.billing_cycle_usage_response_api_calls_billable import BillingCycleUsageResponseApiCallsBillable
from unicourt.model.billing_cycle_usage_response_api_calls_credited import BillingCycleUsageResponseApiCallsCredited
from unicourt.model.billing_cycle_usage_response_api_calls_made import BillingCycleUsageResponseApiCallsMade
from unicourt.model.billing_cycle_usage_response_billing_cycle import BillingCycleUsageResponseBillingCycle
from typing import Optional, Set
from typing_extensions import Self

class BillingCycleUsageResponse(BaseModel):
    """
    BillingCycleUsageResponse
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=25, strict=True, max_length=25)]] = Field(default='BillingCycleUsageResponse', description="Name of the object.")
    billing_cycle: Optional[BillingCycleUsageResponseBillingCycle] = Field(default=None, alias="billingCycle")
    days: Optional[Dict[str, Any]] = Field(default=None, description="Billing cycle days.")
    api_usage: Optional[Dict[str, Any]] = Field(default=None, description="Billing cycle apiUsage.", alias="apiUsage")
    api_calls_made: Optional[BillingCycleUsageResponseApiCallsMade] = Field(default=None, alias="apiCallsMade")
    api_calls_credited: Optional[BillingCycleUsageResponseApiCallsCredited] = Field(default=None, alias="apiCallsCredited")
    api_calls_billable: Optional[BillingCycleUsageResponseApiCallsBillable] = Field(default=None, alias="apiCallsBillable")
    total_cases_tracked: Optional[StrictInt] = Field(default=None, description="Total number of successful case tracks.", alias="totalCasesTracked")
    __properties: ClassVar[List[str]] = ["object", "billingCycle", "days", "apiUsage", "apiCallsMade", "apiCallsCredited", "apiCallsBillable", "totalCasesTracked"]

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
        """Create an instance of BillingCycleUsageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_cycle
        if self.billing_cycle:
            _dict['billingCycle'] = self.billing_cycle.to_dict()
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
        """Create an instance of BillingCycleUsageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'BillingCycleUsageResponse',
            "billingCycle": BillingCycleUsageResponseBillingCycle.from_dict(obj["billingCycle"]) if obj.get("billingCycle") is not None else None,
            "days": obj.get("days"),
            "apiUsage": obj.get("apiUsage"),
            "apiCallsMade": BillingCycleUsageResponseApiCallsMade.from_dict(obj["apiCallsMade"]) if obj.get("apiCallsMade") is not None else None,
            "apiCallsCredited": BillingCycleUsageResponseApiCallsCredited.from_dict(obj["apiCallsCredited"]) if obj.get("apiCallsCredited") is not None else None,
            "apiCallsBillable": BillingCycleUsageResponseApiCallsBillable.from_dict(obj["apiCallsBillable"]) if obj.get("apiCallsBillable") is not None else None,
            "totalCasesTracked": obj.get("totalCasesTracked")
        })
        return _obj


