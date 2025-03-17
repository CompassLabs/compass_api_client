# coding: utf-8

"""
    Compass API

      <h3>With this API you can:</h3> <ul> <li><strong>Execute complex DeFi transactions:&nbsp; </strong>Swap, lend, borrow, stake, LP, and more, with high-level on-chain actions.</li> <li><strong>Stay secure &amp; non-custodial</strong> &ndash; Transactions are signed locally, and you retain full control.</li> <li><strong>Build AI &amp; automation workflows</strong> &ndash; Power AI agents, trading bots, yield products and DeFi applications with programmatic transaction execution. Integrate seamlessly into existing workflows.</li> <li><strong>Interact across multiple protocols &amp; chains</strong>&nbsp;&ndash; Spot, lending, staking on Ethereum, Arbitrum, Base. Many more to come!</li> </ul>  <h3 id=\"quick-links\" class=\"docs-chapter-header\"><a class=\"not-prose group hover:text-compass-pink transition-colors flex w-fit\" href=\"https://www.compasslabs.ai/api-docs#quick-links\">Quick links</a></h3> <ul> <li><a href=\"https://api.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">API reference</a></li> <li><a href=\"https://github.com/CompassLabs/compass_api_examples\" target=\"_blank\" rel=\"noopener\">5 min quickstart</a></li> <li><a href=\"https://discord.gg/qjP8dCYZ58\" target=\"_blank\" rel=\"noopener\">Discord</a></li> <li><a href=\"https://www.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">Compass Labs</a></li> </ul>

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.api.aerodrome_slipstream_api import AerodromeSlipstreamApi


class TestAerodromeSlipstreamApi(unittest.TestCase):
    """AerodromeSlipstreamApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AerodromeSlipstreamApi()

    def tearDown(self) -> None:
        pass

    def test_process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_liquidity_provision_increase_post

        Increase an LP position
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_liquidity_provision_mint_post

        Open a new LP position
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_liquidity_provision_positions_get_post

        Get the number of LP positions for a given sender
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_liquidity_provision_withdraw_post

        Withdraw a LP position
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_pool_price_get_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_pool_price_get_post

        Get the current price of a pool (how many token0 you can buy for 1 token1). This is only the instantaneous price; during any trade the price will change. Use the quote endpoint to get a more realistic idea of the ratios of the two assets you could trade.
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_swap_buy_exactly_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_swap_buy_exactly_post

        Trade the amount of a token it takes to end up with a specified quantity of the other token
        """
        pass

    def test_process_request_v0_aerodrome_slipstream_swap_sell_exactly_post(self) -> None:
        """Test case for process_request_v0_aerodrome_slipstream_swap_sell_exactly_post

        Trade a specific amount of a token into another.
        """
        pass


if __name__ == '__main__':
    unittest.main()
