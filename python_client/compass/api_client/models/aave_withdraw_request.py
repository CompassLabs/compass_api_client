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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from compass.api_client.models.amount3 import Amount3
from compass.api_client.models.chain import Chain
from compass.api_client.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class AaveWithdrawRequest(BaseModel):
    """
    AaveWithdrawRequest
    """ # noqa: E501
    asset: Token = Field(description="The symbol of the underlying asset to withdraw.<br> Note the [supported tokens per chain](/#/#token-table).<br>")
    amount: Amount3
    recipient: StrictStr = Field(description="The address of the recipient of the withdrawn funds.")
    chain: Chain
    sender: StrictStr = Field(description="The address of the transaction sender")
    __properties: ClassVar[List[str]] = ["asset", "amount", "recipient", "chain", "sender"]

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
        """Create an instance of AaveWithdrawRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AaveWithdrawRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asset": obj.get("asset"),
            "amount": Amount3.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "recipient": obj.get("recipient"),
            "chain": obj.get("chain"),
            "sender": obj.get("sender")
        })
        return _obj


