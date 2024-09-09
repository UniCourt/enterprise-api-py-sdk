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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from unicourt.model.possible_norm_party_score_constituents import PossibleNormPartyScoreConstituents
from typing import Optional, Set
from typing_extensions import Self

class PossibleNormParty(BaseModel):
    """
    PossibleNormParty
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=17, strict=True, max_length=17)]] = Field(default='PossibleNormParty', description="Name of the object")
    norm_party_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="normPartyId")
    norm_party_name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="normPartyName")
    best_match: Optional[StrictBool] = Field(default=False, alias="bestMatch")
    confidence_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="confidenceScore")
    score_constituents: Optional[PossibleNormPartyScoreConstituents] = Field(default=None, alias="scoreConstituents")
    norm_party_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Link to Details For the Party.", alias="normPartyAPI")
    associated_norm_attorneys_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="associatedNormAttorneysAPI")
    associated_norm_law_firms_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="associatedNormLawFirmsAPI")
    associated_norm_judges_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="associatedNormJudgesAPI")
    case_count_analytics_by_norm_party_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="caseCountAnalyticsByNormPartyAPI")
    case_count_analytics_by_opposing_norm_party_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="caseCountAnalyticsByOpposingNormPartyAPI")
    __properties: ClassVar[List[str]] = ["object", "normPartyId", "normPartyName", "bestMatch", "confidenceScore", "scoreConstituents", "normPartyAPI", "associatedNormAttorneysAPI", "associatedNormLawFirmsAPI", "associatedNormJudgesAPI", "caseCountAnalyticsByNormPartyAPI", "caseCountAnalyticsByOpposingNormPartyAPI"]

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
        """Create an instance of PossibleNormParty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of score_constituents
        if self.score_constituents:
            _dict['scoreConstituents'] = self.score_constituents.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PossibleNormParty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PossibleNormParty',
            "normPartyId": obj.get("normPartyId"),
            "normPartyName": obj.get("normPartyName"),
            "bestMatch": obj.get("bestMatch") if obj.get("bestMatch") is not None else False,
            "confidenceScore": obj.get("confidenceScore"),
            "scoreConstituents": PossibleNormPartyScoreConstituents.from_dict(obj["scoreConstituents"]) if obj.get("scoreConstituents") is not None else None,
            "normPartyAPI": obj.get("normPartyAPI"),
            "associatedNormAttorneysAPI": obj.get("associatedNormAttorneysAPI"),
            "associatedNormLawFirmsAPI": obj.get("associatedNormLawFirmsAPI"),
            "associatedNormJudgesAPI": obj.get("associatedNormJudgesAPI"),
            "caseCountAnalyticsByNormPartyAPI": obj.get("caseCountAnalyticsByNormPartyAPI"),
            "caseCountAnalyticsByOpposingNormPartyAPI": obj.get("caseCountAnalyticsByOpposingNormPartyAPI")
        })
        return _obj


