# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.api.uniswap_v3_api import UniswapV3Api


class TestUniswapV3Api(unittest.TestCase):
    """UniswapV3Api unit test stubs"""

    def setUp(self) -> None:
        self.api = UniswapV3Api()

    def tearDown(self) -> None:
        pass

    def test_buy_exactly_v0_uniswap_swap_buy_exactly_post(self) -> None:
        """Test case for buy_exactly_v0_uniswap_swap_buy_exactly_post

        Buy exact amount
        """
        pass

    def test_get_buy_quote_v0_uniswap_quote_buy_exactly_get_post(self) -> None:
        """Test case for get_buy_quote_v0_uniswap_quote_buy_exactly_get_post

        Get quote for buying tokens
        """
        pass

    def test_get_pool_price_v0_uniswap_pool_price_get_post(self) -> None:
        """Test case for get_pool_price_v0_uniswap_pool_price_get_post

        Get the price of a token in a Uniswap pool
        """
        pass

    def test_get_positions_v0_uniswap_liquidity_provision_positions_get_post(self) -> None:
        """Test case for get_positions_v0_uniswap_liquidity_provision_positions_get_post

        Retrieve LP positions for a sender
        """
        pass

    def test_get_sell_quote_v0_uniswap_quote_sell_exactly_get_post(self) -> None:
        """Test case for get_sell_quote_v0_uniswap_quote_sell_exactly_get_post

        Get quote for selling tokens
        """
        pass

    def test_in_range_v0_uniswap_liquidity_provision_in_range_get_post(self) -> None:
        """Test case for in_range_v0_uniswap_liquidity_provision_in_range_get_post

        check if a position is in active tick range
        """
        pass

    def test_increase_liquidity_v0_uniswap_liquidity_provision_increase_post(self) -> None:
        """Test case for increase_liquidity_v0_uniswap_liquidity_provision_increase_post

        Increase an LP position
        """
        pass

    def test_mint_v0_uniswap_liquidity_provision_mint_post(self) -> None:
        """Test case for mint_v0_uniswap_liquidity_provision_mint_post

        Open a new LP position
        """
        pass

    def test_sell_exactly_v0_uniswap_swap_sell_exactly_post(self) -> None:
        """Test case for sell_exactly_v0_uniswap_swap_sell_exactly_post

        Sell exact amount
        """
        pass

    def test_withdraw_v0_uniswap_liquidity_provision_withdraw_post(self) -> None:
        """Test case for withdraw_v0_uniswap_liquidity_provision_withdraw_post

        Withdraw an LP position
        """
        pass


if __name__ == '__main__':
    unittest.main()
