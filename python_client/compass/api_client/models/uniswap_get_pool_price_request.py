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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from compass.api_client.models.chain import Chain
from compass.api_client.models.fee_enum import FeeEnum
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class UniswapGetPoolPriceRequest(BaseModel):
    """
    UniswapGetPoolPriceRequest
    """ # noqa: E501
    chain: Chain
    token_in: Token = Field(description="The symbol of a token in the pool<br> Note the [supported tokens per chain](/#/#token-table).<br>")
    token_out: Token = Field(description="The symbol of a token in the pool<br> Note the [supported tokens per chain](/#/#token-table).<br>")
    fee: FeeEnum = Field(description="The fee of the pool")
    __properties: ClassVar[List[str]] = ["chain", "token_in", "token_out", "fee"]

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
        """Create an instance of UniswapGetPoolPriceRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniswapGetPoolPriceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chain": obj.get("chain"),
            "token_in": obj.get("token_in"),
            "token_out": obj.get("token_out"),
            "fee": obj.get("fee")
        })
        return _obj


