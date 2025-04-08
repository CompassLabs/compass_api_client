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
from typing import Any, ClassVar, Dict, List
from compass.api_client.models.amount0_desired1 import Amount0Desired1
from compass.api_client.models.amount0_min1 import Amount0Min1
from compass.api_client.models.amount1_desired1 import Amount1Desired1
from compass.api_client.models.amount1_min1 import Amount1Min1
from typing import Optional, Set
from typing_extensions import Self

class UniswapIncreaseLiquidityProvisionParams(BaseModel):
    """
    UniswapIncreaseLiquidityProvisionParams
    """ # noqa: E501
    token_id: StrictInt = Field(description="Token ID of the NFT representing the liquidity provisioned position.")
    amount0_desired: Amount0Desired1
    amount1_desired: Amount1Desired1
    amount0_min: Amount0Min1
    amount1_min: Amount1Min1
    __properties: ClassVar[List[str]] = ["token_id", "amount0_desired", "amount1_desired", "amount0_min", "amount1_min"]

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
        """Create an instance of UniswapIncreaseLiquidityProvisionParams from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniswapIncreaseLiquidityProvisionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token_id": obj.get("token_id"),
            "amount0_desired": Amount0Desired1.from_dict(obj["amount0_desired"]) if obj.get("amount0_desired") is not None else None,
            "amount1_desired": Amount1Desired1.from_dict(obj["amount1_desired"]) if obj.get("amount1_desired") is not None else None,
            "amount0_min": Amount0Min1.from_dict(obj["amount0_min"]) if obj.get("amount0_min") is not None else None,
            "amount1_min": Amount1Min1.from_dict(obj["amount1_min"]) if obj.get("amount1_min") is not None else None
        })
        return _obj


