# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.api.aerodrome_basic_api import AerodromeBasicApi


class TestAerodromeBasicApi(unittest.TestCase):
    """AerodromeBasicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AerodromeBasicApi()

    def tearDown(self) -> None:
        pass

    def test_add_liquidity_eth_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post(self) -> None:
        """Test case for add_liquidity_eth_v0_aerodrome_basic_liquidity_provision_add_liquidity_eth_post

        Provide liquidity using WETH
        """
        pass

    def test_add_liquidity_v0_aerodrome_basic_liquidity_provision_add_liquidity_post(self) -> None:
        """Test case for add_liquidity_v0_aerodrome_basic_liquidity_provision_add_liquidity_post

        Provide liquidity
        """
        pass

    def test_eth_for_token_v0_aerodrome_basic_swap_eth_for_token_post(self) -> None:
        """Test case for eth_for_token_v0_aerodrome_basic_swap_eth_for_token_post

        Swap from ETH
        """
        pass

    def test_remove_liquidity_eth_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post(self) -> None:
        """Test case for remove_liquidity_eth_v0_aerodrome_basic_liquidity_provision_remove_liquidity_eth_post

        Remove liquidity using WETH
        """
        pass

    def test_remove_liquidity_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post(self) -> None:
        """Test case for remove_liquidity_v0_aerodrome_basic_liquidity_provision_remove_liquidity_post

        Remove liquidity
        """
        pass

    def test_swap_tokens_v0_aerodrome_basic_swap_tokens_post(self) -> None:
        """Test case for swap_tokens_v0_aerodrome_basic_swap_tokens_post

        Swap
        """
        pass

    def test_token_for_eth_v0_aerodrome_basic_swap_token_for_eth_post(self) -> None:
        """Test case for token_for_eth_v0_aerodrome_basic_swap_token_for_eth_post

        Swap token for ETH
        """
        pass


if __name__ == '__main__':
    unittest.main()
