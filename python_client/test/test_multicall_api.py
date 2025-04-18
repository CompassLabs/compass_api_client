# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.api.multicall_api import MulticallApi


class TestMulticallApi(unittest.TestCase):
    """MulticallApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MulticallApi()

    def tearDown(self) -> None:
        pass

    def test_multicall_authorization(self) -> None:
        """Test case for multicall_authorization

        Get EIP-7702 Authorization
        """
        pass

    def test_multicall_execute(self) -> None:
        """Test case for multicall_execute

        Execute Tx Batching
        """
        pass


if __name__ == '__main__':
    unittest.main()
