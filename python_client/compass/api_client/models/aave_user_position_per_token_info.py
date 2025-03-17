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
from typing import Optional, Set
from typing_extensions import Self

class AaveUserPositionPerTokenInfo(BaseModel):
    """
    AaveUserPositionPerTokenInfo
    """ # noqa: E501
    atoken_balance: StrictStr = Field(description="The balance of AAVE aTokens (interest-bearing representations of your deposits).")
    stable_debt: StrictStr = Field(description="The amount of the user's debt with a fixed interest rate.")
    variable_debt: StrictStr = Field(description="The amount of the user's debt with a variable interest rate.")
    principal_stable_debt: StrictStr = Field(description="The amount of the user's debt that was part of the initial principal of all loans with a stable interest rate.")
    principal_variable_debt: StrictStr = Field(description="The amount of the user's debt that was part of the initial principal of all loans with a variable interest rate. This is the value stored by AAVE, which may be slightly inaccurate, but reflects what AAVE believes you initially paid.")
    stable_borrow_rate: StrictStr = Field(description="The current average annualised interest rate for all your stable loans in this pool.")
    stable_borrow_rate_for_new_loans: StrictStr = Field(description="The annualised interest rate you would pay on a new stable loan.")
    variable_borrow_rate: StrictStr = Field(description="The current annualised interest rate for variable rate loans in this pool. (This applies to both current and new loans.)")
    liquidity_rate: StrictStr = Field(description="The annualised interest rate for deposited supplies.")
    __properties: ClassVar[List[str]] = ["atoken_balance", "stable_debt", "variable_debt", "principal_stable_debt", "principal_variable_debt", "stable_borrow_rate", "stable_borrow_rate_for_new_loans", "variable_borrow_rate", "liquidity_rate"]

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
        """Create an instance of AaveUserPositionPerTokenInfo from a JSON string"""
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
        """Create an instance of AaveUserPositionPerTokenInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "atoken_balance": obj.get("atoken_balance"),
            "stable_debt": obj.get("stable_debt"),
            "variable_debt": obj.get("variable_debt"),
            "principal_stable_debt": obj.get("principal_stable_debt"),
            "principal_variable_debt": obj.get("principal_variable_debt"),
            "stable_borrow_rate": obj.get("stable_borrow_rate"),
            "stable_borrow_rate_for_new_loans": obj.get("stable_borrow_rate_for_new_loans"),
            "variable_borrow_rate": obj.get("variable_borrow_rate"),
            "liquidity_rate": obj.get("liquidity_rate")
        })
        return _obj


