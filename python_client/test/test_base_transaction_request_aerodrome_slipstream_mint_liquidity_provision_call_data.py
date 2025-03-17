# coding: utf-8

"""
    Compass API

    <div class=\"mt-6 flex justify-center\">     <a href=\"/auth/get_bearer_token\"         class=\"inline-flex justify-center py-2 px-6 border border-transparent rounded-md shadow-sm bg-blue-600 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors\">         Get Bearer Token     </a> </div>   <h3>With this API you can:</h3> <ul> <li><strong>Execute complex DeFi transactions:&nbsp; </strong>Swap, lend, borrow, stake, LP, and more, with high-level on-chain actions.</li> <li><strong>Stay secure &amp; non-custodial</strong> &ndash; Transactions are signed locally, and you retain full control.</li> <li><strong>Build AI &amp; automation workflows</strong> &ndash; Power AI agents, trading bots, yield products and DeFi applications with programmatic transaction execution. Integrate seamlessly into existing workflows.</li> <li><strong>Interact across multiple protocols &amp; chains</strong>&nbsp;&ndash; Spot, lending, staking on Ethereum, Arbitrum, Base. Many more to come!</li> </ul>  <h3 id=\"quick-links\" class=\"docs-chapter-header\"><a class=\"not-prose group hover:text-compass-pink transition-colors flex w-fit\" href=\"https://www.compasslabs.ai/api-docs#quick-links\">Quick links</a></h3> <ul> <li><a href=\"https://api.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">API reference</a></li> <li><a href=\"https://github.com/CompassLabs/compass_api_examples\" target=\"_blank\" rel=\"noopener\">5 min quickstart</a></li> <li><a href=\"https://discord.gg/qjP8dCYZ58\" target=\"_blank\" rel=\"noopener\">Discord</a></li> <li><a href=\"https://www.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">Compass Labs</a></li> </ul>

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData

class TestBaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData(unittest.TestCase):
    """BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData:
        """Test BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData`
        """
        model = BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData()
        if include_optional:
            return BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData(
                chain = 'ethereum:mainnet',
                sender = '',
                call_data = compass.api_client.models.aerodrome_slipstream_mint_liquidity_provision_call_data.AerodromeSlipstreamMintLiquidityProvisionCallData(
                    token0 = '1INCH', 
                    token1 = '1INCH', 
                    tick_spacing = 56, 
                    tick_lower = 56, 
                    tick_upper = 56, 
                    amount0_desired = null, 
                    amount1_desired = null, 
                    amount0_min = null, 
                    amount1_min = null, 
                    recipient = '', )
            )
        else:
            return BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData(
                chain = 'ethereum:mainnet',
                sender = '',
                call_data = compass.api_client.models.aerodrome_slipstream_mint_liquidity_provision_call_data.AerodromeSlipstreamMintLiquidityProvisionCallData(
                    token0 = '1INCH', 
                    token1 = '1INCH', 
                    tick_spacing = 56, 
                    tick_lower = 56, 
                    tick_upper = 56, 
                    amount0_desired = null, 
                    amount1_desired = null, 
                    amount0_min = null, 
                    amount1_min = null, 
                    recipient = '', ),
        )
        """

    def testBaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData(self):
        """Test BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
