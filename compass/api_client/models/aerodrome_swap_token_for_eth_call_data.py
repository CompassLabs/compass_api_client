# coding: utf-8

"""
    Compass API

      #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.  Below is the documentation of our endpoints. It's a great first step to explore.  

    The version of the OpenAPI document: 0.0.1
    Contact: contact@compasslabs.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from compass.api_client.models.amount_in2 import AmountIn2
from compass.api_client.models.amount_out_min1 import AmountOutMin1
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AerodromeSwapTokenForEthCallData(BaseModel):
    """
    AerodromeSwapTokenForEthCallData
    """ # noqa: E501
    token_in: Token = Field(description="The symbol of the token to swap from<br> Note the supported tokens per chain:<br>**ethereum:mainnet**: ['1INCH', 'AAVE', 'BAL', 'cbBTC', 'cbETH', 'CRV', 'crvUSD', 'DAI', 'ENS', 'ETHx', 'FRAX', 'FXS', 'GHO', 'KNC', 'LDO', 'LINK', 'LUSD', 'MKR', 'osETH', 'PYUSD', 'rETH', 'RPL', 'rsETH', 'sDAI', 'SNX', 'STG', 'sUSDe', 'tBTC', 'UNI', 'USDC', 'USDe', 'USDS', 'USDT', 'WBTC', 'weETH', 'WETH', 'wstETH']<br>**arbitrum:mainnet**: ['AAVE', 'ARB', 'DAI', 'EURS', 'FRAX', 'GHO', 'LINK', 'LUSD', 'MAI', 'rETH', 'USDC', 'USDCe', 'USDT', 'WBTC', 'weETH', 'WETH', 'wstETH']<br>**base:mainnet**: ['1INCH', 'AERO', 'ARB', 'BAL', 'cbBTC', 'cbETH', 'CRV', 'crvUSD', 'DAI', 'EUR', 'LUSD', 'MKR', 'osETH', 'rETH', 'SNX', 'STG', 'tBTC', 'USDC', 'UNI', 'USDT', 'VIRTUAL', 'WBTC', 'weETH', 'WETH', 'wstETH']<br>")
    amount_in: AmountIn2
    amount_out_min: AmountOutMin1
    stable: StrictBool = Field(description="If true, try to trade on a stable pool with a bonding curve of K=x^3y+y^3x. If false, try to trade on a volatile pool with a bonding curve of K=xy")
    to: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["token_in", "amount_in", "amount_out_min", "stable", "to"]

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
        """Create an instance of AerodromeSwapTokenForEthCallData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount_in
        if self.amount_in:
            _dict['amount_in'] = self.amount_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_out_min
        if self.amount_out_min:
            _dict['amount_out_min'] = self.amount_out_min.to_dict()
        # set to None if to (nullable) is None
        # and model_fields_set contains the field
        if self.to is None and "to" in self.model_fields_set:
            _dict['to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AerodromeSwapTokenForEthCallData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token_in": obj.get("token_in"),
            "amount_in": AmountIn2.from_dict(obj["amount_in"]) if obj.get("amount_in") is not None else None,
            "amount_out_min": AmountOutMin1.from_dict(obj["amount_out_min"]) if obj.get("amount_out_min") is not None else None,
            "stable": obj.get("stable"),
            "to": obj.get("to")
        })
        return _obj


