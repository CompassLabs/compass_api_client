# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from compass.api_client.models.chain import Chain
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AaveGetLiquidityChangeRequest(BaseModel):
    """
    AaveGetLiquidityChangeRequest
    """ # noqa: E501
    chain: Chain
    start_block: StrictInt = Field(description="The starting block.")
    end_block: Optional[StrictInt] = None
    asset: Token = Field(description="The symbol of the asset to fetch liquidity index change for. Note the [supported tokens per chain](/#/#token-table).")
    __properties: ClassVar[List[str]] = ["chain", "start_block", "end_block", "asset"]

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
        """Create an instance of AaveGetLiquidityChangeRequest from a JSON string"""
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
        # set to None if end_block (nullable) is None
        # and model_fields_set contains the field
        if self.end_block is None and "end_block" in self.model_fields_set:
            _dict['end_block'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AaveGetLiquidityChangeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chain": obj.get("chain"),
            "start_block": obj.get("start_block"),
            "end_block": obj.get("end_block"),
            "asset": obj.get("asset")
        })
        return _obj


