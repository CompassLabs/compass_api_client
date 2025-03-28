# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.api.aave_v3_api import AaveV3Api


class TestAaveV3Api(unittest.TestCase):
    """AaveV3Api unit test stubs"""

    def setUp(self) -> None:
        self.api = AaveV3Api()

    def tearDown(self) -> None:
        pass

    def test_borrow_v0_aave_borrow_post(self) -> None:
        """Test case for borrow_v0_aave_borrow_post

        Borrow
        """
        pass

    def test_get_asset_price_v0_aave_asset_price_get_post(self) -> None:
        """Test case for get_asset_price_v0_aave_asset_price_get_post

        Token prices
        """
        pass

    def test_get_liquidity_change_v0_aave_liquidity_change_get_post(self) -> None:
        """Test case for get_liquidity_change_v0_aave_liquidity_change_get_post

        Liquidity index
        """
        pass

    def test_get_user_position_per_token_v0_aave_user_position_per_token_get_post(self) -> None:
        """Test case for get_user_position_per_token_v0_aave_user_position_per_token_get_post

        Positions - per token
        """
        pass

    def test_get_user_position_summary_v0_aave_user_position_summary_get_post(self) -> None:
        """Test case for get_user_position_summary_v0_aave_user_position_summary_get_post

        Positions - total
        """
        pass

    def test_repay_v0_aave_repay_post(self) -> None:
        """Test case for repay_v0_aave_repay_post

        Repay loans
        """
        pass

    def test_supply_v0_aave_supply_post(self) -> None:
        """Test case for supply_v0_aave_supply_post

        Supply/Lend
        """
        pass

    def test_withdraw_v0_aave_withdraw_post(self) -> None:
        """Test case for withdraw_v0_aave_withdraw_post

        Unstake
        """
        pass


if __name__ == '__main__':
    unittest.main()
