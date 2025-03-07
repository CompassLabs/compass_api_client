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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class UnsignedTransaction(BaseModel):
    """
    UnsignedTransaction
    """ # noqa: E501
    chain_id: StrictInt = Field(description="The chain id of the transaction", alias="chainId")
    data: StrictStr = Field(description="The data of the transaction")
    var_from: StrictStr = Field(description="The sender of the transaction", alias="from")
    gas: StrictInt = Field(description="The gas of the transaction")
    to: StrictStr = Field(description="The recipient of the transaction")
    value: StrictInt = Field(description="The value of the transaction")
    nonce: StrictInt = Field(description="The nonce of the address")
    max_fee_per_gas: StrictInt = Field(description="The max fee per gas of the transaction", alias="maxFeePerGas")
    max_priority_fee_per_gas: StrictInt = Field(description="The max priority fee per gas of the transaction", alias="maxPriorityFeePerGas")
    __properties: ClassVar[List[str]] = ["chainId", "data", "from", "gas", "to", "value", "nonce", "maxFeePerGas", "maxPriorityFeePerGas"]

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
        """Create an instance of UnsignedTransaction from a JSON string"""
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
        """Create an instance of UnsignedTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chainId": obj.get("chainId"),
            "data": obj.get("data"),
            "from": obj.get("from"),
            "gas": obj.get("gas"),
            "to": obj.get("to"),
            "value": obj.get("value"),
            "nonce": obj.get("nonce"),
            "maxFeePerGas": obj.get("maxFeePerGas"),
            "maxPriorityFeePerGas": obj.get("maxPriorityFeePerGas")
        })
        return _obj


