# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.base_transaction_request_aerodrome_slipstream_sell_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData

class TestBaseTransactionRequestAerodromeSlipstreamSellExactlyCallData(unittest.TestCase):
    """BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData:
        """Test BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData`
        """
        model = BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData()
        if include_optional:
            return BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData(
                chain = 'base:mainnet',
                sender = '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                call_data = {amount_in=1, amount_out_minimum=0, tick_spacing=100, token_in=USDC, token_out=WETH}
            )
        else:
            return BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData(
                chain = 'base:mainnet',
                sender = '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                call_data = {amount_in=1, amount_out_minimum=0, tick_spacing=100, token_in=USDC, token_out=WETH},
        )
        """

    def testBaseTransactionRequestAerodromeSlipstreamSellExactlyCallData(self):
        """Test BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
