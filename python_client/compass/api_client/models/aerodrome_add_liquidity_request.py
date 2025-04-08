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
from typing_extensions import Annotated
from compass.api_client.models.amount_a_desired import AmountADesired
from compass.api_client.models.amount_a_min import AmountAMin
from compass.api_client.models.amount_b_desired import AmountBDesired
from compass.api_client.models.amount_b_min import AmountBMin
from compass.api_client.models.chain import Chain
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AerodromeAddLiquidityRequest(BaseModel):
    """
    AerodromeAddLiquidityRequest
    """ # noqa: E501
    token_a: Token = Field(description="The symbol of the token to provide liquidity for Note the [supported tokens per chain](/#/#token-table).")
    token_b: Token = Field(description="The symbol of the token to provide liquidity for Note the [supported tokens per chain](/#/#token-table).")
    stable: StrictBool = Field(description="If true, try to provide liquidity on a stable pool with a bonding curve of K=x^3y+y^3x. If false, try to provide liquidity on a volatile pool with a bonding curve of K=xy")
    amount_a_desired: AmountADesired
    amount_b_desired: AmountBDesired
    amount_a_min: AmountAMin
    amount_b_min: AmountBMin
    to: Optional[StrictStr] = None
    deadline: Optional[Annotated[int, Field(strict=True, ge=0)]]
    chain: Chain
    sender: StrictStr = Field(description="The address of the transaction sender")
    __properties: ClassVar[List[str]] = ["token_a", "token_b", "stable", "amount_a_desired", "amount_b_desired", "amount_a_min", "amount_b_min", "to", "deadline", "chain", "sender"]

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
        """Create an instance of AerodromeAddLiquidityRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount_a_desired
        if self.amount_a_desired:
            _dict['amount_a_desired'] = self.amount_a_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_b_desired
        if self.amount_b_desired:
            _dict['amount_b_desired'] = self.amount_b_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_a_min
        if self.amount_a_min:
            _dict['amount_a_min'] = self.amount_a_min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_b_min
        if self.amount_b_min:
            _dict['amount_b_min'] = self.amount_b_min.to_dict()
        # set to None if to (nullable) is None
        # and model_fields_set contains the field
        if self.to is None and "to" in self.model_fields_set:
            _dict['to'] = None

        # set to None if deadline (nullable) is None
        # and model_fields_set contains the field
        if self.deadline is None and "deadline" in self.model_fields_set:
            _dict['deadline'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AerodromeAddLiquidityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token_a": obj.get("token_a"),
            "token_b": obj.get("token_b"),
            "stable": obj.get("stable"),
            "amount_a_desired": AmountADesired.from_dict(obj["amount_a_desired"]) if obj.get("amount_a_desired") is not None else None,
            "amount_b_desired": AmountBDesired.from_dict(obj["amount_b_desired"]) if obj.get("amount_b_desired") is not None else None,
            "amount_a_min": AmountAMin.from_dict(obj["amount_a_min"]) if obj.get("amount_a_min") is not None else None,
            "amount_b_min": AmountBMin.from_dict(obj["amount_b_min"]) if obj.get("amount_b_min") is not None else None,
            "to": obj.get("to"),
            "deadline": obj.get("deadline"),
            "chain": obj.get("chain"),
            "sender": obj.get("sender") if obj.get("sender") is not None else '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'
        })
        return _obj


