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
from compass.api_client.models.amount_eth_desired import AmountEthDesired
from compass.api_client.models.amount_eth_min import AmountEthMin
from compass.api_client.models.amount_token_desired import AmountTokenDesired
from compass.api_client.models.amount_token_min import AmountTokenMin
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AerodromeLiquidityProvisionEthCallData(BaseModel):
    """
    AerodromeLiquidityProvisionEthCallData
    """ # noqa: E501
    token: Token = Field(description="The symbol of the token to provide liquidity for alongside WETH.<br> Note the [supported tokens per chain](/#/#token-table).<br>")
    stable: StrictBool = Field(description="If true, try to provide liquidity on a stable pool with a bonding curve of K=x^3y+y^3x. If false, try to provide liquidity on a volatile pool with a bonding curve of K=xy")
    amount_token_desired: AmountTokenDesired
    amount_eth_desired: AmountEthDesired
    amount_token_min: AmountTokenMin
    amount_eth_min: AmountEthMin
    to: Optional[StrictStr] = None
    deadline: Optional[Annotated[int, Field(strict=True, ge=0)]]
    __properties: ClassVar[List[str]] = ["token", "stable", "amount_token_desired", "amount_eth_desired", "amount_token_min", "amount_eth_min", "to", "deadline"]

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
        """Create an instance of AerodromeLiquidityProvisionEthCallData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount_token_desired
        if self.amount_token_desired:
            _dict['amount_token_desired'] = self.amount_token_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_eth_desired
        if self.amount_eth_desired:
            _dict['amount_eth_desired'] = self.amount_eth_desired.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_token_min
        if self.amount_token_min:
            _dict['amount_token_min'] = self.amount_token_min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_eth_min
        if self.amount_eth_min:
            _dict['amount_eth_min'] = self.amount_eth_min.to_dict()
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
        """Create an instance of AerodromeLiquidityProvisionEthCallData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token": obj.get("token"),
            "stable": obj.get("stable"),
            "amount_token_desired": AmountTokenDesired.from_dict(obj["amount_token_desired"]) if obj.get("amount_token_desired") is not None else None,
            "amount_eth_desired": AmountEthDesired.from_dict(obj["amount_eth_desired"]) if obj.get("amount_eth_desired") is not None else None,
            "amount_token_min": AmountTokenMin.from_dict(obj["amount_token_min"]) if obj.get("amount_token_min") is not None else None,
            "amount_eth_min": AmountEthMin.from_dict(obj["amount_eth_min"]) if obj.get("amount_eth_min") is not None else None,
            "to": obj.get("to"),
            "deadline": obj.get("deadline")
        })
        return _obj


