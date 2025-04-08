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
from compass.api_client.models.chain import Chain
from compass.api_client.models.multicall_action import MulticallAction
from compass.api_client.models.signed_authorization import SignedAuthorization
from typing import Optional, Set
from typing_extensions import Self

class MulticallExecuteRequest(BaseModel):
    """
    Request model for executing a multicall.
    """ # noqa: E501
    chain: Chain
    sender: StrictStr = Field(description="The address of the transaction sender")
    signed_authorization: SignedAuthorization
    contract_address: StrictStr = Field(description="The address of the multicall contract")
    actions: List[MulticallAction] = Field(description="List of possible actions for multicall")
    __properties: ClassVar[List[str]] = ["chain", "sender", "signed_authorization", "contract_address", "actions"]

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
        """Create an instance of MulticallExecuteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of signed_authorization
        if self.signed_authorization:
            _dict['signed_authorization'] = self.signed_authorization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MulticallExecuteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chain": obj.get("chain"),
            "sender": obj.get("sender") if obj.get("sender") is not None else '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
            "signed_authorization": SignedAuthorization.from_dict(obj["signed_authorization"]) if obj.get("signed_authorization") is not None else None,
            "contract_address": obj.get("contract_address"),
            "actions": [MulticallAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None
        })
        return _obj


