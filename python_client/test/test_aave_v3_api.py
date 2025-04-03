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

    def test_aave_asset_price(self) -> None:
        """Test case for aave_asset_price

        Token prices
        """
        pass

    def test_aave_borrow(self) -> None:
        """Test case for aave_borrow

        Borrow
        """
        pass

    def test_aave_liquidity_change(self) -> None:
        """Test case for aave_liquidity_change

        Liquidity index
        """
        pass

    def test_aave_repay(self) -> None:
        """Test case for aave_repay

        Repay loans
        """
        pass

    def test_aave_supply(self) -> None:
        """Test case for aave_supply

        Supply/Lend
        """
        pass

    def test_aave_user_position_per_token(self) -> None:
        """Test case for aave_user_position_per_token

        Positions - per token
        """
        pass

    def test_aave_user_position_summary(self) -> None:
        """Test case for aave_user_position_summary

        Positions - total
        """
        pass

    def test_aave_withdraw(self) -> None:
        """Test case for aave_withdraw

        Unstake
        """
        pass


if __name__ == '__main__':
    unittest.main()
