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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from compass.api_client.models.amount0_desired import Amount0Desired
from compass.api_client.models.amount0_min import Amount0Min
from compass.api_client.models.amount1_desired import Amount1Desired
from compass.api_client.models.amount1_min import Amount1Min
from compass.api_client.models.chain import Chain
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AerodromeSlipstreamMintLiquidityProvisionRequest(BaseModel):
    """
    Request model for minting a new liquidity position.
    """ # noqa: E501
    token0: Token = Field(description="The symbol of the first token in the pair Note the [supported tokens per chain](/#/#token-table).")
    token1: Token = Field(description="The symbol of the second token in the pair Note the [supported tokens per chain](/#/#token-table).")
    tick_spacing: Annotated[int, Field(strict=True, ge=1)] = Field(description="The tick spacing of the pool")
    tick_lower: StrictInt = Field(description="The lower tick of the range to mint the position in")
    tick_upper: StrictInt = Field(description="The upper tick of the range to mint the position in")
    amount0_desired: Amount0Desired
    amount1_desired: Amount1Desired
    amount0_min: Amount0Min
    amount1_min: Amount1Min
    recipient: Optional[StrictStr] = None
    chain: Chain
    sender: StrictStr = Field(description="The address of the transaction sender")
    __properties: ClassVar[List[str]] = ["token0", "token1", "tick_spacing", "tick_lower", "tick_upper", "amount0_desired", "amount1_desired", "amount0_min", "amount1_min", "recipient", "chain", "sender"]

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
        """Create an instance of AerodromeSlipstreamMintLiquidityProvisionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount0_desired
        if self.amount0_desired:
            _dict['amount0_desired'] = self.amount0_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount1_desired
        if self.amount1_desired:
            _dict['amount1_desired'] = self.amount1_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount0_min
        if self.amount0_min:
            _dict['amount0_min'] = self.amount0_min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount1_min
        if self.amount1_min:
            _dict['amount1_min'] = self.amount1_min.to_dict()
        # set to None if recipient (nullable) is None
        # and model_fields_set contains the field
        if self.recipient is None and "recipient" in self.model_fields_set:
            _dict['recipient'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AerodromeSlipstreamMintLiquidityProvisionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token0": obj.get("token0"),
            "token1": obj.get("token1"),
            "tick_spacing": obj.get("tick_spacing"),
            "tick_lower": obj.get("tick_lower"),
            "tick_upper": obj.get("tick_upper"),
            "amount0_desired": Amount0Desired.from_dict(obj["amount0_desired"]) if obj.get("amount0_desired") is not None else None,
            "amount1_desired": Amount1Desired.from_dict(obj["amount1_desired"]) if obj.get("amount1_desired") is not None else None,
            "amount0_min": Amount0Min.from_dict(obj["amount0_min"]) if obj.get("amount0_min") is not None else None,
            "amount1_min": Amount1Min.from_dict(obj["amount1_min"]) if obj.get("amount1_min") is not None else None,
            "recipient": obj.get("recipient"),
            "chain": obj.get("chain"),
            "sender": obj.get("sender") if obj.get("sender") is not None else '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'
        })
        return _obj


