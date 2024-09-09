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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.associated_so_s_person import AssociatedSoSPerson
from unicourt.model.contact import Contact
from unicourt.model.sos_associated_norm_organization import SOSAssociatedNormOrganization
from unicourt.model.sos_name_change import SOSNameChange
from typing import Optional, Set
from typing_extensions import Self

class SOSData(BaseModel):
    """
    SOSData
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=7)]] = 'SOSData'
    sos_number: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, alias="sosNumber")
    state_code: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, alias="stateCode")
    fein: Optional[Annotated[str, Field(strict=True, max_length=16)]] = None
    domestic_registration: Optional[StrictBool] = Field(default=True, alias="domesticRegistration")
    registered_date: Optional[datetime] = Field(default=None, alias="registeredDate")
    status: Optional[Annotated[str, Field(strict=True, max_length=10)]] = None
    is_active: Optional[StrictBool] = Field(default=True, alias="isActive")
    inactivation_date: Optional[datetime] = Field(default=None, alias="inactivationDate")
    associated_so_s_person_array: Optional[List[AssociatedSoSPerson]] = Field(default=None, alias="associatedSoSPersonArray")
    contact: Optional[Contact] = None
    name_changes_array: Optional[List[SOSNameChange]] = Field(default=None, alias="nameChangesArray")
    sos_associated_norm_organization_array: Optional[List[SOSAssociatedNormOrganization]] = Field(default=None, alias="sosAssociatedNormOrganizationArray")
    first_fetch_date: Optional[datetime] = Field(default=None, alias="firstFetchDate")
    last_fetch_date: Optional[datetime] = Field(default=None, alias="lastFetchDate")
    last_fetch_date_with_updates: Optional[datetime] = Field(default=None, description="Last Fetch Date of Organization with Updates.", alias="lastFetchDateWithUpdates")
    __properties: ClassVar[List[str]] = ["object", "sosNumber", "stateCode", "fein", "domesticRegistration", "registeredDate", "status", "isActive", "inactivationDate", "associatedSoSPersonArray", "contact", "nameChangesArray", "sosAssociatedNormOrganizationArray", "firstFetchDate", "lastFetchDate", "lastFetchDateWithUpdates"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Active']):
            raise ValueError("must be one of enum values ('Active')")
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
        """Create an instance of SOSData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_so_s_person_array (list)
        _items = []
        if self.associated_so_s_person_array:
            for _item in self.associated_so_s_person_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedSoSPersonArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in name_changes_array (list)
        _items = []
        if self.name_changes_array:
            for _item in self.name_changes_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nameChangesArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sos_associated_norm_organization_array (list)
        _items = []
        if self.sos_associated_norm_organization_array:
            for _item in self.sos_associated_norm_organization_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sosAssociatedNormOrganizationArray'] = _items
        # set to None if sos_number (nullable) is None
        # and model_fields_set contains the field
        if self.sos_number is None and "sos_number" in self.model_fields_set:
            _dict['sosNumber'] = None

        # set to None if fein (nullable) is None
        # and model_fields_set contains the field
        if self.fein is None and "fein" in self.model_fields_set:
            _dict['fein'] = None

        # set to None if registered_date (nullable) is None
        # and model_fields_set contains the field
        if self.registered_date is None and "registered_date" in self.model_fields_set:
            _dict['registeredDate'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if inactivation_date (nullable) is None
        # and model_fields_set contains the field
        if self.inactivation_date is None and "inactivation_date" in self.model_fields_set:
            _dict['inactivationDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SOSData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'SOSData',
            "sosNumber": obj.get("sosNumber"),
            "stateCode": obj.get("stateCode"),
            "fein": obj.get("fein"),
            "domesticRegistration": obj.get("domesticRegistration") if obj.get("domesticRegistration") is not None else True,
            "registeredDate": obj.get("registeredDate"),
            "status": obj.get("status"),
            "isActive": obj.get("isActive") if obj.get("isActive") is not None else True,
            "inactivationDate": obj.get("inactivationDate"),
            "associatedSoSPersonArray": [AssociatedSoSPerson.from_dict(_item) for _item in obj["associatedSoSPersonArray"]] if obj.get("associatedSoSPersonArray") is not None else None,
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "nameChangesArray": [SOSNameChange.from_dict(_item) for _item in obj["nameChangesArray"]] if obj.get("nameChangesArray") is not None else None,
            "sosAssociatedNormOrganizationArray": [SOSAssociatedNormOrganization.from_dict(_item) for _item in obj["sosAssociatedNormOrganizationArray"]] if obj.get("sosAssociatedNormOrganizationArray") is not None else None,
            "firstFetchDate": obj.get("firstFetchDate"),
            "lastFetchDate": obj.get("lastFetchDate"),
            "lastFetchDateWithUpdates": obj.get("lastFetchDateWithUpdates")
        })
        return _obj


