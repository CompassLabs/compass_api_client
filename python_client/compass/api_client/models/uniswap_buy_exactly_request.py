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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from compass.api_client.models.amount_in_maximum import AmountInMaximum
from compass.api_client.models.amount_out import AmountOut
from compass.api_client.models.chain import Chain
from compass.api_client.models.fee_enum import FeeEnum
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class UniswapBuyExactlyRequest(BaseModel):
    """
    Request model for buying exactly an amount of tokens.
    """ # noqa: E501
    token_in: Token = Field(description="The symbol of the token to swap from Note the [supported tokens per chain](/#/#token-table).")
    token_out: Token = Field(description="The symbol of the token to swap to Note the [supported tokens per chain](/#/#token-table).")
    fee: FeeEnum = Field(description="The swap fee of the pool")
    amount_out: AmountOut
    amount_in_maximum: AmountInMaximum
    wrap_eth: Optional[StrictBool] = Field(default=False, description="Whether to wrap ETH to WETH, only use when swapping WETH into something")
    chain: Chain
    sender: StrictStr = Field(description="The address of the transaction sender")
    __properties: ClassVar[List[str]] = ["token_in", "token_out", "fee", "amount_out", "amount_in_maximum", "wrap_eth", "chain", "sender"]

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
        """Create an instance of UniswapBuyExactlyRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount_out
        if self.amount_out:
            _dict['amount_out'] = self.amount_out.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_in_maximum
        if self.amount_in_maximum:
            _dict['amount_in_maximum'] = self.amount_in_maximum.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniswapBuyExactlyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token_in": obj.get("token_in"),
            "token_out": obj.get("token_out"),
            "fee": obj.get("fee"),
            "amount_out": AmountOut.from_dict(obj["amount_out"]) if obj.get("amount_out") is not None else None,
            "amount_in_maximum": AmountInMaximum.from_dict(obj["amount_in_maximum"]) if obj.get("amount_in_maximum") is not None else None,
            "wrap_eth": obj.get("wrap_eth") if obj.get("wrap_eth") is not None else False,
            "chain": obj.get("chain"),
            "sender": obj.get("sender") if obj.get("sender") is not None else '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'
        })
        return _obj


