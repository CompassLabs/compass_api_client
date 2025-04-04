# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Chain(str, Enum):
    """
    The chain to use.
    """

    """
    allowed enum values
    """
    BASE_COLON_MAINNET = 'base:mainnet'
    ETHEREUM_COLON_MAINNET = 'ethereum:mainnet'
    ARBITRUM_COLON_MAINNET = 'arbitrum:mainnet'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Chain from a JSON string"""
        return cls(json.loads(json_str))


